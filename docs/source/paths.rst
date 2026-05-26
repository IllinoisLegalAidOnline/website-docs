===================================
Google Analytics and Path Changes
===================================

Query to Run
------------

.. code-block:: sql

    -- 1. Published node canonical paths (/node/NID)
    SELECT
        CONCAT('/node/', n.nid)                             AS path,
        n.nid                                               AS nid,
        'node_id'                                           AS path_type,
        n.title                                             AS title,
        n.type                                              AS content_type,
        'published'                                         AS status,
        n.langcode                                          AS langcode
    FROM node_field_data n
    WHERE n.status = 1

    UNION

    -- 2. Current aliases of published nodes
    SELECT
        pa.alias                                            AS path,
        n.nid                                               AS nid,
        'current_alias'                                     AS path_type,
        n.title                                             AS title,
        n.type                                              AS content_type,
        'published'                                         AS status,
        n.langcode                                          AS langcode
    FROM path_alias pa
    JOIN node_field_data n
        ON pa.path = CONCAT('/node/', n.nid)
        AND n.status = 1
    WHERE pa.status = 1

    UNION

    -- 3. Redirects pointing directly at a published node
    SELECT
        CONCAT('/', r.redirect_source__path)                AS path,
        n.nid                                               AS nid,
        'redirect'                                          AS path_type,
        n.title                                             AS title,
        n.type                                              AS content_type,
        'published'                                         AS status,
        n.langcode                                          AS langcode
    FROM redirect r
    JOIN node_field_data n
        ON r.redirect_redirect__uri = CONCAT('internal:/node/', n.nid)
        AND n.status = 1

    UNION

    -- 4. Aliases of unpublished nodes that redirect to a published node
    --    e.g. /legal-information/buying-and-keeping-used-car -> nid 95401
    SELECT
        pa.alias                                            AS path,
        n_target.nid                                        AS nid,
        'redirect_via_unpublished'                          AS path_type,
        n_target.title                                      AS title,
        n_target.type                                       AS content_type,
        'published'                                         AS status,
        n_target.langcode                                   AS langcode
    FROM node_field_data n_unpub
    JOIN path_alias pa
        ON pa.path = CONCAT('/node/', n_unpub.nid)
        AND pa.status = 1
    JOIN redirect r
        ON r.redirect_source__path = CONCAT('node/', n_unpub.nid)
    JOIN node_field_data n_target
        ON r.redirect_redirect__uri = CONCAT('internal:/node/', n_target.nid)
        AND n_target.status = 1
    WHERE n_unpub.status = 0
      AND n_target.nid != n_unpub.nid

    ORDER BY nid, path_type, path;


Integration with Tableau Prep Builder
--------------------------------------

The resulting query should be exported to CSV and attached as the ``path_cms`` datasource.


Comparison to CMSdata
----------------------

This dataset has all of the same data as the CMS data. It also contains all of the redirects.
This is helpful to see the overall impact of revamping content, consolidating articles, and
keeping an accurate trend view.

The original CMSdata set is also available for analysis.

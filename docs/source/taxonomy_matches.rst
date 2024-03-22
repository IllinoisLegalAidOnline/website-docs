=============================
Taxonomy matches for metrics
=============================

Taxonomy matches require a database download and then a custom query to create a table that contains, for each piece of legal content:

* The taxonomy term(s) it is attached to
* Every piece of content that shares that taxonomy term.

For example, node ID 114316 is tagged to taxonomy term 537291. So are 147991, 147996, and 148236. Just these alone results in the following rows:

+--------------+----------------+------------+
| Term ID      | From ID        | To ID      |
+==============+================+============+
| 537291       | 147991         | 147996     |
+--------------+----------------+------------+
| 537291       | 147991         | 148236     |
+--------------+----------------+------------+
| 537291       | 147996         | 147991     |
+--------------+----------------+------------+
| 537291       | 147996         | 148236     |
+--------------+----------------+------------+
| 537291       | 148236         | 147991     |
+--------------+----------------+------------+
| 537291       | 148236         | 147996     |
+--------------+----------------+------------+

The queries to generate the datasets are below.

To retrieve content associated to each other based on legal issues
===================================================================

.. code-block::

   SELECT
   t1.field_legal_issues_target_id,
   t1.entity_id AS entity_id,
   t2.entity_id AS other_entity_id
   FROM
     node__field_legal_issues AS t1
   INNER JOIN node__field_legal_issues AS t2 ON t1.field_legal_issues_target_id = t2.field_legal_issues_target_id AND t1.entity_id != t2.entity_id
   ORDER BY
   t1.field_legal_issues_target_id, t1.entity_id, t2.entity_id;

To retrieve content associated to each other based on navigtional IA term
============================================================================

.. code-block::

   SELECT
   t1.field_navigational_ia_target_id,
   t1.entity_id AS entity_id,
   t2.entity_id AS other_entity_id
   FROM
   node__field_navigational_ia AS t1
   INNER JOIN node__field_navigational_ia AS t2 ON t1.field_navigational_ia_target_id = t2.field_navigational_ia_target_id AND t1.entity_id != t2.entity_id
   ORDER BY
   t1.field_navigational_ia_target_id, t1.entity_id, t2.entity_id

.. note:: Currently, only navigational IA is used in the Tableau sets.

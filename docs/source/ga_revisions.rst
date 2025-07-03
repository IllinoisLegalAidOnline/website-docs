============================
Legal content revisions
============================

For the revisions dashboard, we need to pull historical revision data. This must be pulled directly from a MySQL database instance.

.. note:: Pulling the database requires an Acquia user account with CLI access and a Lando instance with phpMyAdmin installed. To get the database, from the command line:

   * Ensure that the acli is up-to-date by running acli update
   * Run acli drush @ilaodrupal8.prod sql-dump > ~/ilaoprodJuly24 changing the file name date based on the current date
   * Launch lando in the phpmyadmin directory with Lando Start
   * Open phpMyAdmin and drop any existing Acquia database
   * From the commandline, run lando mysql acquia < ~/filename

Getting SME revisions
========================

Getting SME revisions requires running two queries against the MySQL Acquia database and then merging the results into one CSV file named "node_sme_revised.csv"

Get real SME revisions
-------------------------
Step 1 is to get the actual SME revisions. This query returns the node ID and date of SME revision for every instance where the SME revision date was created or updated, essentially creating a SME review history.

.. code-block:: sql

   SELECT distinct entity_id as nid,
   DATE_FORMAT(field_last_substantive_update_value, '%m/%d/%Y %H:%i')
   as sme_review
   FROM `node_revision__field_last_substantive_update`
   where langcode = 'en' and bundle = 'legal_content';


Create SME revisions where none exist
--------------------------------------
Step 2 is to create SME revisions for content that has no SME revision date, based on the assumption that ILAO does not publish content that hasn't been confirmed as legally accurate. For these nodes, we set the SME revision date manually to the date the content was created.

.. code-block:: sql

   Select nid, from_unixtime(created) as sme_review from node_field_data where nid
   not in (
   SELECT entity_id  FROM `node_revision__field_last_substantive_update`
   where langcode = 'en' and bundle = 'legal_content')
   and type = 'legal_content'
   and langcode in ('en','und');

Getting Staff Revisions
==========================
Staff revisions are limited to those where the last reviewed by staff date has been added or changed. It does not include any other type of staff revision. This limits this dataset to substantive updates.


.. code-block:: sql

   SELECT distinct entity_id as node_id, DATE_FORMAT(field_last_revised_value, '%m/%d/%Y %H:%i') as staff_reviewed
   FROM `node_revision__field_last_revised`
   where langcode = 'en' and bundle = 'legal_content';

This query should be exported to a CSV named staff_review_history.csv





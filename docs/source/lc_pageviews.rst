===================
Page view import
===================

Pageviews are the default sort for legal content navigation. Page views are updated via a file upload.

To do the import/export:

* Download the Legal Content UUID report as a CSV file. This includes all published legal content node IDs, their unique UUID, and page path.
* Add the page views. There are two ways to do this:
* Import the page views CSV to the website using the `Google analytics pageviews <https://www.illinoislegalaid.org/google-analytics-pageviews>`_ CSV import tool.
* In Tableau prep builder:

  * Update the legal-content-uuid data source to use the recent export
  * Update the ga-data-global data source to use the most recent ga-data-global file used to do Tableau content metrics reporting
  * Run the flow
  * Open the resulting CSV file and sort by page views descending
  * Save the CSV
  * Upload the CSV to the website.

.. note:: Once imported, this will set up the queue manager to update page views on a scheduled basis. It may take time for this to take effect. If you need a more immediate run, please reach out to Gwen or Mike.





=========================================
Updating pageviews for ordering content
=========================================

Updating the page views is a multi-step process:

* Pull pageviews from Google Analytics
* Pull node ID/UUID data from the CMS
* Pull the legal content report from the CMS
* Run these 3 files through the Tableau GA-pageviews-import to create a single CSV file
* Upload the CSV file on the website
* Wait for the queue manager to run or manually run the queue task.

Pull Pageviews from Google Analytics
=====================================

.. image:: ../assets/ga-for-pageviews.png

Pull CMS data
================

There are 2 reports that need to be run and exported to CSV to update the page views from the CMS:

* UUID report



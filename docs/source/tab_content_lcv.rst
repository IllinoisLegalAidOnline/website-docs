=======================
Tableau - LCV program
=======================

The LCV program report can be found in the `LCV program <https://prod-useast-b.online.tableau.com/#/site/ilaootis/views/contentMetrics/LCVProgram?:iid=2>`_ tab in the Content Metrics workbook.

Prerequisites
==============

The LCV program report relies on:

* Salesforce data related to events & engagements. To be calculated:

  * Each engagement must have node IDs from the content entered **in the Node ID: field as a comma delimited list.** This allows Tableau to associate them back to the CMS report
  * Each engagement must have the total number of articles reviewed entered
  
* An export of the CMS legal content review
* Google Analytics core data

Report
=========
The report shows:

* Organization (defined as the primary affiliation of the contact in Salesforce)
* Contact
* Articles reviewed (from Salesforce)
* Active users (from Google Analytics)
* Page views (from Google Analytics)


The report can be filtered:

* On a Google Analytics date range, to limit the active users and page views to certain months. All months are stored as mm/1/yyyy. For example, to get June and July 2025, you would filter on 6/1/2025 to 7/1/2025.
* On the date complete by the volunteer date range. This filters on the date completed in Salesforce
* Category - primary legal category from the CMS
* Subcategory - this filter will automatically update based on selected Category.




===================================
Prepping content data for Tableau
===================================

The two workbooks (Core data and Illinois) require that data be run through 3 sets of Tableau prep builders:

* Google analytics prep
* CMS data prep
* LSV data prep


Google Analytics Prep
=======================

The Google analytics prep currently works for calendar year 2024 but will require additional prep work for future years. It requires 4 CSV files:

* The all GA4 data from July 1, 2023 - Dec 31, 2023
* A file that contains all of the 2024 data. This is created by taking the raw GA4 export for the current month and combining it with the prior months' cumulative file.
* The Illinois only GA4 data from July 1, 2023 - Dec 31, 2023
* A file that contains all of the 2024 data for Illinois only. This is created by taking the raw GA4 export for the current month and combining it with the prior months' cumulative file.

This is the all-ga-cleanup flow.

When run, it creates two files:

* ga-data-global.csv which then works with the core metrics workbook
* ga-data-illinois.csv which works with the Illinois metrics workbook

CMS data prep
==================

This prep requires two files:

* An export of legal content from the "Find Legal Content" report
* An export of the Navigational IA; open the export from the website and clean up so that only terms with language = "English" are displayed. Remove all but name and term ID columns and copy and paste into a new sheet.

This flow then creates the CMS data CSV that can be used with both workbooks.

This is the cms-data-flow-cleanup flow.


LCV Transforms
=================

This requires two files:

* The ga-data-global file created from the Google analytics prep
* The most recent download from Salesforce of the ILAO LCV events and engagements report

The LCV-reports is then used with the core metrics workbook.

This is the lcv-transforms flow.

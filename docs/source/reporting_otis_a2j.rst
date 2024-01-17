=====================================
Specialized reporting: State Grants
=====================================
The reports below are used for reporting on our Access to Justice(A2J) grants.
Intake by population/legal issue

* `Incarceration intakes by special population <https://www.illinoislegalaid.org/admin/reporting/a2j/otis-incarceration-populations>`_
* `Incarceration intakes based on legal issue <https://www.illinoislegalaid.org/admin/reporting/a2j/otis-incarceration-issues>`_
* `Immigration intakes by special population <https://www.illinoislegalaid.org/admin/reporting/a2j/otis-immigration-populations>`_
* `Immigration intakes based on legal issue <https://www.illinoislegalaid.org/admin/reporting/a2j/otis-immigration-issues>`_

Referrals by population/legal issue

* `Incarceration referrals based on population <https://www.illinoislegalaid.org/admin/reporting/a2j/referrals-incarceration-populations>`_
* `Incarceration referrals based on legal issue <https://www.illinoislegalaid.org/admin/reporting/a2j/referrals-incarceration-issues>`_
* `Immigration referrals based on population <https://www.illinoislegalaid.org/admin/reporting/a2j/referrals-immigration-populations>`_
* `Immigration referrals by legal issue <https://www.illinoislegalaid.org/admin/reporting/a2j/referrals-immigration>`_


Each report can be exported to CSV for advanced manipulation and can be filtered by date.

.. warning::  Reports expect dates to be formatted as yyyy-mm-dd hh:mm:ss. When a date like 3/1/2021 or 2021-03-01 is provided, it assumes a time of 00:00:00. When used as an end date, that means that no results for that day will be included (a date of 3/31/2021 will be interpreted as 3/31/2021 00:00:00; you'd want to use 4/01/2021 to include all of 3/31/2021)

.. note::  These reports do be further refined using the CSV export to filter on county, zip code, and/or organizations.

Referral reports
====================
There are two referral reports per area: one based on special populations and one based on defined legal issues.

The referral report returns:

* Triage ID, this is the unique ID associated with the user's single interaction with Get Legal Help. We make multiple referrals per triage ID so there are multiple rows.
* Referral ID. This is the unique ID associated with the specific referral made.
* Created, date the referral was made
* Triage status. This is almost always Referrals or Program Triage Completed. 
* Intake status. This is either empty (Triage status of Referrals) or Diverted (Intake status of Program triage completed)
* Service
* Organization
* County
* Zip code
* Comma-delimited list of any special populations the user selected
* Initial legal problem is USUALLY the starting point for the user in the taxonomy tree
* Search term here is any text they may have provided; if they picked from the taxonomy on the main Get Legal Help page, this as the initial taxonomy term will match.
* Problem history is their full drill down; this will be blank if the user jumped immediately to triage/referrals without drilling down.
* Household size from the main Get Legal Help page


A referral is included in the legal issues report when:
-----------------------------------------------------------

* Intake status is not etransferred
* Taxonomy term from the legal issues for the triage user entity is, with depth, matches a specified list [this filter searches across all legal issues fields in the triage user record, which covers the various ways we store search terms in Get Legal Help]
  * Matches the date range, if provided, for term filter
* Service language is English (this is required to prevent duplicate records when the organization has been translated)

A referral is included in the population report when:
--------------------------------------------------------

* Intake status is not etransferred
* Has a special population match based on:
  
  * Is an immigrant or is undocumented (immigration)
  * Is in jail or prison OR has a family member in jail or prison (incarceration)

* Matches the date range, if provided, for population filter
* Service language is English (this is required to prevent duplicate records when the organization has been translated)


.. note:: Because a user can match both on special population and on legal issue, the two reports should be combined in Excel and de-duplicated. Each user has a unique triage ID and each referral has a unique ID. To get unique users, de-duplicate on triage ID. To get unique referrals, de-duplicate on referral ID  


Intake Reports
=======================

The report returns:

* Triage ID, this is the unique ID associated with the user's single interaction with Get Legal Help. 
* Created, date the intake was made
* Service
* Organization
* County
* Zip code
* Comma-delimited list of any special populations the user selected
* Initial legal problem is USUALLY the starting point for the user in the taxonomy tree
* Search term here is any text they may have provided; if they picked from the taxonomy on the main Get Legal Help page, this as the initial taxonomy term will match.
* Problem history is their full drill down; this will be blank if the user jumped immediately to triage/referrals without drilling down.
* Ethnicity
* Race
* Gender
* Primary language
* Household size from the main Get Legal Help page
* Adults
* Children


An intake is included in the legal issues report when:
-----------------------------------------------------------

* Intake status is etransferred
* Taxonomy term from the legal issues for the triage user entity is, with depth, matches a specified list [this filter searches across all legal issues fields in the triage user record, which covers the various ways we store search terms in Get Legal Help]
  * Matches the date range, if provided, for term filter
* Service language is English (this is required to prevent duplicate records when the organization has been translated)

A intake is included in the population report when:
--------------------------------------------------------

* Intake status is etransferred
* Has a special population match based on:
  
  * Is an immigrant or is undocumented (immigration)
  * Is in jail or prison OR has a family member in jail or prison (incarceration)

* Matches the date range, if provided, for population filter
* Service language is English (this is required to prevent duplicate records when the organization has been translated)


.. note:: Because a user can match both on special population and on legal issue, the two reports should be combined in Excel and de-duplicated. Each user has a unique triage ID  To get unique users, de-duplicate on triage ID. 

Legal Issues
=====================

We use a taxonomy index with depth filter to filter the intake or referral by legal issue reports. This filter searches across all legal issues fields in the triage user record, which covers the various ways we store search terms in Get Legal Help.


Immigration
---------------

* 514866	Immigration status, work permits and travel papers
* 515866	Paying income taxes as an undocumented immigrant
* 517221	Qualifying for Medicaid as an immigrant
* 517286	Qualifying for Medicare as an immigrant
* 517436	U.S. citizenship
* 517451	Another citizenship issue
* 517456	U.S. citizens' rights
* 517551	Being afraid to return to my home country and seeking asylum or refuge
* 517556	Someone like a boss or boyfriend controlling where I go, what I do and who I talk to (T Visa)
* 517591	Other citizens or immigration issues
  

Incarceration Term List
---------------------------

* 516231	Background checks or criminal records
* 517221	Qualifying for Medicaid as an immigrant
* 517621	Police (arrest, charge, or search)
* 517636	Juvenile justice system or record
* 517681	Criminal records




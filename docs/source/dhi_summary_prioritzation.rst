=============================
User journey: Prioritization
=============================

When a user completes prioritization via the Landbot triage tool, their data is processed and they are given a prioritization results page.

Incoming data
================

.. code-block:: JSON
     {"id":461529266,"problem_profile_id":"621",
     "source":"https:\/\/dev.debthelpillinois.org\/debt-tool",
     "debt_prioritization":
     ["130051","130076","130056","129996","130031","130001","130046","130091","130081",
     "130096","130076","130021","130011","130006","129986","130071","129981","130041"],
     ""
     }
     
For each debt entered in the prioritization area:

* A debt entity is created with a corresponding debt problem entity. The debt problem entity is set to a problem type of "Prioritized"
* The debt entity is created with the debt type that corresponds to what the user indicated as the debt type.


.. note:: If a visitor has gone through prioritization and the system indicates that they have an identity theft issue, there will be a debt created of type "Identity theft" with an associated debt problem entity with a current problem of "Prioritization."

Summary and next steps
==============================

The summmary and next steps page displays at the debt-prioritization url. This page includes:

* A "Based on your response" summary.
* Information on specific debt types entered

Identity theft
-----------------
If the user has a problem type of identity theft and debt type of "prioritized", an alert about tackling identity theft first displays

In litigation
----------------
If the user has a problem type of "active lawsuit" and debt type of "prioritized", an alert about dealingi with an active lawsuit displays immediately after identity theft.

Highest priority debts
-------------------------
If the user has debt types that have a typical priority of "highest," they will appear as cards here. Each card will show:

* Name of the debt type
* Prioritization summary
* Learn more if there is a priority note
* Highest priority label
* Button "Take action now" that returns the user to the debt-tool filtered for the specific debt entity.

High priority debts
-------------------------
If the user has debt types that have a typical priority of "high," they will appear as cards here. Each card will show:

* Name of the debt type
* Prioritization summary
* Learn more if there is a priority note
* High Priority label
* Button "Tackle [debt type]" that returns the user to the debt-tool filtered for the specific debt entity.

Low priority debts
-------------------------
If the user has debt types that have a typical priority of "high," they will appear as cards here. Each card will show:

* Name of the debt type
* Prioritization summary
* Learn more if there is a priority note
* High Priority label
* Button "Get started with [debt type]" that returns the user to the debt-tool filtered for the specific debt entity.

For each category of debt priority, there is a carousel and overflow page if there are more debt entities than the display can hold.

.. note:: If a user selects a debt to work on, the Landbot tool will be updated to prevent them from starting a new prioritization.


   
   


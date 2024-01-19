.. _twilio_functions:

=====================
Twilio Functions
=====================


This documents the functions stored in our Twilio function service "ilao."

All of our Twilio functions are stored in the ilao service in Twilio's functions.

Guided navigation functions used in our Twilio SMS are documented in :ref:`guided_nav_functions` documentation.

Function standards
======================
All function names are written in the word-word-word format.


All passed in parameters are contained in the event object.

OAuth get token
==================
**Function name:**  oauth-get-token

**Parameters:**  none

**Returns:** an access token

**Requires:**  A consumer for our API account and a user account to call.

.. note:: The following functions rely on the OAuth token:

* otis-create-triage-user
* otis-triage-user
* eviction-intake-settings
* otis-get-matches
* eviction-matches

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   otis_global_functions
   otis_eviction_functions
   otis_triage_intake_functions
   otis_guided_nav_functions
   otis_website_data_integration_functions


OTIS get confirmation
======================

**Function name:**  otis-get-confirmation

**Parameters:**  event.intakeSettingsId and event.callbackType

**Requires:**  ILAO API call to get the return message based on the intake settings id and callback type.

**Status:**  This is a placeholder function right now. It returns either the "we call" or "you call" message" as a JSON object.


Callbacks
============

OTIS Get Callback Slots
-------------------------
**Function name:** pilot-get-callback-slots

**Parameters:** 

* event.token
* event.settings_id
* event.language

**Returns:** An object that contains the available callback slots for the matched organization.

**Purpose:** Gathers the available callback slots for the organization the applicant applied

**Widget:** get-callback-times

**Flow:** OTIS appointment scheduler

OTIS Get Callback Slots by Day
---------------------------------
**Function name:** pilot-get-next-days-slots

**Parameters:** 

* event.values
* event.index

**Returns:** An object that contains the available appointment times for the selected day.

**Widget:** get-callback-slots-by-day

**Flow:** OTIS appointment scheduler

OTIS Get Callback Days (Deprecated?)
--------------------------------------
**Function name:**  otis-get-callback-days

**Parameters:**  event.intakeSettingsId

**Requires:**  ILAO API call to get the next [x] days of available intake appointments.

**Status:**  This is a placeholder function right now. It returns a JSON object of days for the user to pick from. Currently, it is using an array of days and a string of days to output. This needs to be revised to return a key value pair that can be rendered while still having useful info for the system.

OTIS Get First Callback Time (Deprecated?)
-----------------------------------------------
**Function name:**  otis-get-first-callback-time

**Parameters:**  event.intakeSettingsId

**Requires:**  ILAO API call to get the range of available hours and the first available date.

**Status:**  This is a placeholder function right now. It returns a JSON object of days for the user to pick from. It currently returns hard-coded text of:

* intro ('Callback times are between x and y');
* first ('The first available is [x]);
* callback-date: Stores the actual date in mm/dd/yyyy format.

OTIS Get Callback Times (Deprecated?)
-----------------------------------------
**Function name:**  otis-get-callback-times

**Parameters:**  event.intakeSettingsId, event.callbackDate

**Requires:**  ILAO API call to get the range of callback slots for a specific date and intake settings pairing.

**Status:**  This is a placeholder function right now. It returns a JSON object of times for the user to pick from. It currently returns hard-coded text of:

* timeArray of available times
* times - string of times to display to user

OTIS Get Callback Type (Deprecated)
----------------------------------------
**Function name:**  otis-get-callback-times

**Parameters:**  event.intakeSettingsId

**Requires:**  ILAO API call to get the callback type for a specific intake settings

**Status:**  This is a placeholder function right now. It returns a string of either "clientCalls" or "weCallClient"


OTIS Zipcode Validate
=======================

**Function name:**  

* pilot-validate-zipcode (current)
* otis-zipcode-validate (deprecated)

**Purpose**: Determines whether a provided zip code is in Illinois or not based on the Illinois regions asset, which is a JSON file from ILAO's region taxonomy and includes the zipcode, city, county, state, fips ID, and county UUID.

**Parameters:**  event.zip

**Requires:**  API call to get region information based on zip code.

**Returns:** An object (location) that contains:

* zip_code (the zip provided by the user)
* county
* state
* fips id for the county (required by Legal Server)

**Status:** Relies on a JSON object in our static assets (/illinois-regions) that contains the IL regional taxonomy data.

**Widget:** 

* validate-zipcode
* validate-zipcode-counselor

**Flow:** OTIS get location


Get housing counselors list
=============================

.. note:: This only appears when an applicant identifies as having an eviction-related issue. During this special triage section, we first ask if the applicant wants information on housing counselors.

**Function:** hud-housing-counselors

**Purpose:** Performs an API call to provide the applicant with a list of local housing counselors.

**Parameters:** event.zip

**Returns:** An object that contains:

* counseling_agencies (limited to agencies that service the user's zip code)
* name (the name of the agency)
* address (the agency's street address)
* city
* phone
* weburl
* counslg_METHOD (the method the applicant can communicate with the agency -- i.e., face-to-face, phone counseling, group counseling, etc.)

**Widget:** get-counseling

**Flow:** OTIS get location


Update triage user database
============================

**Function name:** otis-update-triage-user

**Purpose:** Update the OTIS triage user database with information from the user's triage path.

**Parameters:** event.token

**Returns:** an object that contains a uuid

**Widgets:** 

* update-counseling (Get location)
* update-gn-triage-user (guided navigation)
* update-triage-user-matches (matches)
* update-triage-user-age (intake)
* update-triage-user-demo (intake)
* update-triage-user-income (intake)
* update-triage-user-contact (contact)
* update-triage-you-call (superbot)
* update-triage-we-call (superbot)
* update-triage-on-etransfer (superbot)

**Flows:**

* OTIS get location
* OTIS Guided Navigation
* OTIS matches
* OTIS Intake
* OTIS contact information
* Superbot flows: SuperbotV2 & SuperbotV3


Create triage user
====================

**Function name:** otis-create-triage-user

**Purpose:** Create a new triage user in the database

**Parameters:** event.token

**Returns:** triage_id

**Widget:** create-triage-user

**Flows:** Superbot flows: SuperbotV2 & SuperbotV3


Increase intake counter
==========================

**Function name:**  otis-increase-intake-counter

**Purpose**:  Updates the current count for an intake setings id when a case is successfully transferred to Legal Server.

**Parameters:** event.current_count & event.uuid

**Requires:** JSON API for online intake

**Returns:** Nothing

**Status:** In development.


Geting Guided Navigation Matches 
==================================

.. note:: This function is currently written in the Guided Navigation services. 

.. todo:: Determine which functions need to remain in which service and move them accordingly

**Function names:**  

* get-gn-match-test (current)
* get-gn-match (deprecated)

**Purpose**: Retrieves data from a specified REST API endpoint, filters and processes the data, and return a list of results (list of intake_ids) based on user input.

**Parameters:**

* event.token
* event.user_issue
* event.outcome_field (identified specific legal issue based on the answers the user provided -- example: ilao-HSG-evict-guest-outcome: eviction for guests, summons, court w/in 5 days -> identifies applicants who are being evicted for have guests in their apartment, they have received a summons, and they have court w/in the next 5 days)
* event.rest_export (this value tells the system which case acceptance rest export webform to look in for matches)

**Returns:** intake_id values for all of the matched organizations

**Widget:** get-gn-matches

**Flow:** OTIS matches


Matches (geography)
=====================

**Function names:** 

* pilot-get-matches (current)
* pilot-get-matches-new (not yet)

**Purpose:** Count and respond with matched organizations based on the matched intake_id's from the previous function against the user's geographic area

**Parameters:** 

* event.zip_id
* event.county_id
* event.city_id

**Returns:** List of matched organizations

**Widget:** get-otis-matches

**Flow:** OTIS matches


Matches (names)
================

**Function name: get-names-test

**Purpose:** Gets the names of the matched organizations to provide to the applicant

**Parameters:** 

* event.services.split (service_id)
* event.intakes.split (intake_id)

**Returns:** Names of the matched organizations

**Widget:** matches-get-name

**Flow:** OTIS matches


Get intake settings data
=========================

**Function name:** 

* get-intake-settigns-with-qualifiers (current)
* pilot-get-intake-settings (deprecated)

**Purpose:** Get the intake settings for the selected organization. Also, identify if the organization uses qualifiers.

**Parameters:**

* event.token
* event.intake_id

**Returns:** data object that contains:

* callback_number
* callback_type
* current_count (intake count)
* bypass_intake_message
* oas_msg_disclaimer
* oas_msg_please_Call_value
* oas_msg_we_call_you

**Widget:** get-intake-settings_data

**Flow:** OTIS matches


Validate date functions
========================

Validate month
----------------
**Function name:** otis-validate-month

**Parameters:** event.month

**Returns:** A variable between 0 and 13 that corresponds with the name of a month

**Widgets:** 

* gn-date-month-return
* validate-month

**Flows:** 

* OTIS Guided Navigation
* OTIS Intake

Validate day of month
----------------------
**Function name:** otis-validate-day-of-month

**Parameters:** event.day

**Returns:** A numeric variable that has been checked against the number of possible days in the corresponding month

**Widgets:**

* validate-gn-date-day
* validate-day

**Flows:** 

* OTIS Guided Navigation
* OTIS Intake

Validate year
----------------
**Function name:** otis-validate-year

**Parameters:** event.year

**Returns:** A 4 digit numeric variable. 

.. note:: If the original parameter was 2 digits and those digits were greater than 10, '19' is added to the parameter; if less than 11, '20' is added to the beginning of the parameter to make either 1930 or 2010. 

**Widgets:**

* validate-gn-date-year
* validate-dob-year

**Flows:** 

* OTIS Guided Navigation
* OTIS Intake

**Requires:** 


Calculate age
===============
**Function name:** otis-calculate-age

**Parameters:** 

* event.year
* event.month
* event.day

**Purpose:** Calculates the applicant's age based on the DOB they provided when compared to the current date.

**Returns:** The applicant's age as a value. In the event of an error, it returns a null value

**Widget:** calculate-age

**Flow:** OTIS Intake 


.. todo:: Add functions that gather race, ethnicity, gender, marital status, and income options. Each of these functions also have corresponding functions that validate them. 

Conflict check
================
**Function name:**  otis-conflict-check

**Purpose**: Queries the Legal Server conflict check API for a specific organization to evaluate whether a user has a potential conflict.

**Parameters:** event.firstName, event.lastName

**Requires:**  A username, password, and url for each organization we need to run a conflict check on

**Returns:** An object of score (lowest, low, high, highest)


Send to Legal Server
======================

**Function name:**  otis-send-to-legal-server

**Purpose**: Builds the data package to etransfer to LegalServer

**Parameters:** event object which contains the data for the eTransfer.

+-----------------------+---------------------+------------------------------------------+
| Event property        | LS property         | Description                              |
+=======================+=====================+==========================================+
| flow_id               |                     | Phone number the user texted to.  Used to|
|                       |                     | route between production/test environs   |
+-----------------------+---------------------+------------------------------------------+
| flowPrefix            | externalId          | Combined in the format of flow prefix-   |
+-----------------------+                     +                                          +
| triage_id             |                     | triage_id to crete a unique id           |
+-----------------------+---------------------+------------------------------------------+
| firstName             | firstName           | User's first name                        |
+-----------------------+---------------------+------------------------------------------+
| middleName            | middleName          | Not captured in SMS                      |
+-----------------------+---------------------+------------------------------------------+
| lastName              | lastName            | User's last name                         |
+-----------------------+---------------------+------------------------------------------+
| eTransferOrganization |eTransferOrganization| LegalServer-specific string for org.     |
|                       |                     | Is stored in website LS configuration    |
+-----------------------+---------------------+------------------------------------------+
| nickname              | aliasFirst          | Any entered nickname                     |
+-----------------------+---------------------+------------------------------------------+
| maiden                | aliasLast           | Any entered maiden name                  |
+-----------------------+---------------------+------------------------------------------+
| street                | addressHome.address1| addressHome is an Object containing the  |
+-----------------------+---------------------+                                          +
| city                  | addressHome.city    | street address, city, state, zip and     |
+-----------------------+---------------------+                                          +
| state                 | addressHome.state   | countyFIPS code provided by the user.    |
+-----------------------+---------------------+------------------------------------------+
| user_phone            | phoneHome           | Either the number the user texted from or|
+-----------------------+---------------------+                                          +
|                       |                     | a provided number, removed of any +1     |
+-----------------------+---------------------+------------------------------------------+
| month                 | dateOfBirth         | Date of birth provided by user.  A 0 is  |
+-----------------------+---------------------+                                          +
| day                   |                     | added for any month or day of less than  |
+-----------------------+---------------------+                                          +
| year                  |                     | 10                                       |
+-----------------------+---------------------+------------------------------------------+
| email                 | email               | User provided email addresss             |
+-----------------------+---------------------+------------------------------------------+
| maritalStatus         | maritalStatus       | User selected marital status             |
+-----------------------+---------------------+------------------------------------------+
| ethnicity             | ethicity            | User selected ethnicity; is set to blank |
|                       |                     | if user selects prefer not to respond.   |
+-----------------------+---------------------+------------------------------------------+
| gender                | gender              | User selected gender.                    |
+-----------------------+---------------------+------------------------------------------+
| language              | language            | User selected preferred language         |
+-----------------------+---------------------+------------------------------------------+
| notes                 | notes               | System-generated notes through triage.   |
+-----------------------+---------------------+------------------------------------------+
| household_adults      | numberOfAdults      | User provided number of adults           |
+-----------------------+---------------------+------------------------------------------+
| household_children    | numberOfChildren    | User provided number of children         |
+-----------------------+---------------------+------------------------------------------+
| callbackType          | callbackType        | Client calls or Callback                 |
+-----------------------+---------------------+------------------------------------------+
| callbackDayTime       | callbackDayTime     | Morning or afternoon for callbacks; empty|
|                       |                     | for client calls                         |
+-----------------------+---------------------+------------------------------------------+
| income_[type]         | income              | income is an object that has multiple    |
|                       |                     | objects for each provided income.  Each  |
|                       |                     |                                          |
|                       |                     | item contains a type, amount, & frequency|
+-----------------------+---------------------+------------------------------------------+
| legalProblemCode      | legalProblemCode    | Legal Server problem code                |
+-----------------------+---------------------+------------------------------------------+


Flow prefixes
---------------

  * For eviction, this is ILAOEvict.

.. note:: Some translation is done on fields such as gender, race, to accommodate differences between ILAO's taxonomy terms and Legal Server's supported terms.

Incomes
---------
The following income types are collected and supported:

* Private disability (Disability)
* Investment income (Trust, Interest, or Dividends)
* TANF
* Veterans' benefits
* Unemployment (Unemployment Compensation)
* SSI
* Social Security
* Alimony
* Child Support
* Workers' Compensation
* Pension/401K income [Pension/Retirement (Not Soc. Sec.)]
* Other income (Other)
* Wages/salaries (Employment)
* Self employment (Employment)


Except for unemployment and wages/salary, all income types have a frequency of 12 (monthly). Unemployment has a frequency of 52 (weekly).  Wages have a frequency of 12, 24, 26, or 52 depending on what the user selected.



**Requires:**  API Key for LegalServer instance

**Returns:** Object from Legal Server.  This object contains either an error or the global unique ID.



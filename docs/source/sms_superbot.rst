=============================
SMS Short Code Architecture
=============================

Main Flow
===========
The main flow executes in the following order:

* Gets required tokens to interact with ILAO website
* Gets user's preferred language
* Validate the text entered in the initial call;

  * if it can be matched to Guided Navigation automatically, we do that
  * if it can not be matched to Guided Navigation automatically, we run the Get Legal Issue subflow
  * sets process id as a flow variable
* Run location subflow
* For Illinois users:

  * Create the triage user
  * Run the household flow
  * Run the OTIS Guided Navigation Flow
  * Run the Matches flow
  * Routes matches based on:

    * Intake - continues to intake
    * Self-exit - continues to self-exit message
    * No organizations - continues to content url and get legal help



English uses the refactored code; Spanish and Polish have not been transitioned

.. note:: Twilio limits subflows to 10 unique subflows in a single flow and subflows can not call other subflows. For that reason, we are limited in how our sublflows are configured.


Subflow: Otis Get Location
============================

Purpose: Determines whether the user is in Illinois or not.

Parameters: none
Returns:

first_name
location (from pilot-validate-zipcode function)


Subflow: OTISGuided Navigation
================================

Purpose: Executes a specific Guided Navigation segment

Parameters: process_id
Returns:

* Status
* Profile (the completed Guided Navigation profile)
* Notes
* rest_export
* lsc_code
* content_url
* outcome_variable
* data_value
* search_term
* user_issue !!

Subflow: Get Legal Issue
==========================

Purpose: Validates input from the user and gets the correct process id

Parameters: keyword

Returns: status (success, failed)
If success, returns:

* process_id
* lsc_code
* search_term
* content_url
* rest_export



Subflow: Run household information
===================================

Purpose:  household size and does an initial income check

Parameters:

* uuid of the triage user
* triage id of the triage user
* token

Updates the triage record on OTIS database to:

* last_screen_viewed = sms_household_size
* household size
* number of adults
* number of children
* overincome status

Returns:

* overincome (1 = true; 0 = false)
* household_size
* adults
* children


Subflow: OTIS Intake
==============================

Purpose: collects and validates date of birth

Parameters:
* uuid of the triage user
* token

Updates triage user object:

* last_screen_viewed = sms_date_of_birth
* age


Returns:
* Numeric value of Month, Day, and Year
* Age

Status: Done


Purpose: collects last name, maiden name, and nickname

Returns: last name, maiden name, and nickname

Status: Done

Purpose: Gathers income information and validates income eligilibty

Parameters:
* Organization match
* uuid (of the triage user)
* token

Updates triage user:
* total_income
* overincome
* last_screen_viewed sms_income

Returns:

* total_income
* income_private_disability
* income_investments
* income_tanf
* income_veterans_amount
* income_unemployment
* income_ssi
* income_social_security
* income_alimony
* income_child_support
* income_workers_comp
* income_pension
* income_investments
* income_other_income
* income_wages
* income_self_employment
* wage_frequency


Purpose: Asks and validates demographic information

Parameters: None

Returns:

* marital_status
* preferred_language
* race
* ethnicity
* marital_status

Subflow: Get matches
=======================

Parameters:

* token
* outcome_variable
* rest_export
* user_issue
* zip_id (zip code id)
* county_id
* city_id
* issue_id !!!

Returns:
* orgs, which is an object of

  * count = number of organizations
  * intakeids = list of intakeIds
  * serviceids = list of service ids
  * orgs, whichi is an array of organizations. Each organization includes:

    * id, the uuid of the service
    * callback number
    * node id
    * callback type
    * bypass message
    * disclaimer
    * please call message
    * we call message

* Selected organization id (service id)
* Match accepted status

picked: 0
intake_id: {{widgets.matches-get-name.parsed.organizations[0].intake_id}}
organization: {{widgets.matches-get-name.parsed.organizations[0].organization}}
legalservername: {{widgets.matches-get-name.parsed.organizations[0].legalservername}}
response: {{widgets.match-selected.inbound.Body}}




Sublfow: OTIS appointment scheduler
======================================

Purpose: Schedules an appointment when a callback is available

Parameters:

* Intake settings id
* Token

Returns:

* Callback_selected (user-friendly format)
* Callback_selected_term (taxonomy-friendly format)


Sublfow: OTIS contact information
====================================

Purpose: To gather contact information from the user

Parameters:
* user_phone
* zip_code

Returns:

* Contact phone
* Email
* Street address
* City











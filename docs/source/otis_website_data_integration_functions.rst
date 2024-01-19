==================================
OTIS Data Integration Functions
==================================

Create Triage User
==========================
**Function name:**  otis-create-triage-user

**Purpose**: Builds a data packet and leverages ILAO's Rest API to create a triage user record on ILAO's website.  This executes after we have validated the user's zip code.

**Parameters:**  Event object that contains base data; empty or missing values are set to null. Base data includes:


* referral_source, varies by application
* zip_code, user's provided zip code
* user_phone, phone number the user texted from
* county, the county associated with the zip code
* search, the incoming message texted by the user
* flow_id, the phone number the user texted to
* last_screen_viewed, set to sms-zip-code
* oas_triage_problem

These are hard-coded within the function:

* household_size, set to 1
* triage_status, set to Started
* oas_triage_problem uuid

.. note:: For eviction, the source is either eviction-spanish or eviction-english

**Requires:**  Authentication with ILAO's API

**Returns:** An object containing:

* id, which is the uuid associated with the newly created user.
* triage_id, which is the internal Drupal ID associated with the entity.

**Widget:** create_triage_user

**Flow:** Superbot main flows

* SuperbotV2
* SuperbotV3

OTIS Update Triage User
==========================
**Function name:**  otis-update-triage-user

**Purpose**: Updates a triage user record on ILAO's website based on interactions with the SMS intake system.

**Parameters:**  Event object with data to update; UUID of existing triage user.

**Requires:**  Authentication with ILAO's REST OTIS API

**Returns:** Updated data packet

**Status:** Data packet based on event object generates; API integration not built.


Within Eviction SMS applications
---------------------------------

This function is called when:

* the user declines to proceed to intake

  * last screen viewed = sms-match-offered
  * intake_status = Offered
  * triage status = Program triage completed

* when the user chooses to proceed to intake

  * last screen viewed = sms-match-offered
  * intake_status = Started
  * triage status = Program triage completed
  * intake_organization = UUID of the intake settings associated with the intake
  * triage_problem = UUID of the determined legal issue from ILAO's legal issue taxonomy (in eviction, this is the eviction term).

* when the user has provided household size information

  * last screen viewed =  sms_household_size
  * event object contains household total, number of adults, and number of children

* after we have collected the date of birth and calculated the user's age

  * last_screen_viewed = sms_date_of_birth
  * event object contains age

* after preferred language is set and all demographics data has been collected

  * last_screen_viwed = sms_demographics
  * event object contains demographic data

* after all income has been collected and we've calculated total income and whether the user is over-income

* when the user reaches an endpoint (etransferred, bypassed, exited to content)

  * if the user is diverted,  intake status is set to Diverted and last screen viewed is set to sms_legal_issue_selector
  * if the user is etransferred, intake status is set to etransferred and last_screen_viewed is set to sms-confirmation
  * if the user in Cook County, last screen viewed is set to cook-county-exit
  * if the user is given counseling resources instead of intake, last screen viewed is set to sms-counselors-list
  * if the user has an unsupported legal issue, triage_status is set to Legal Issue and last screen viewed is set to sms-legal-issues

Within General OTIS SMS application
-------------------------------------

In progress



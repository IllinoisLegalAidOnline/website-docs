===========================
Helper functions
===========================

Helper functions are those that are invoked from Landbot to handle data exchanges or integrate with 3rd party tools.


Creditor match
=================

URL: https://debthelpillinois-3927.twil.io/creditor-match
Parameters: 

* name - name of the creditor provided
* score - the match score required to be included in the results; default is .5
* limit - the maximum number of results to return. Default is 10

Returns:

* an array of matches to ILAO's creditor taxonomy, ordered by score descending 

Requires:

* Drupal view creditors-export that contains the name of creditors in the database.
* Twilio

Creditor details
==================
URL: https://debthelpillinois-3927.twil.io/get-creditor-details

Parameters: 

* name - name of the creditor 

.. code-block:: 

   https://debthelpillinois-3927.twil.io/get-creditor-details?name=1st%20Summit%20Bank

Returns an object that includes the type of creditor

.. code-block::

   {
  "type": "original_creditor"
   }

.. note:: This function may be easily expanded if we begin tracking additional creditor metadata. 

Requires:

* Drupal view creditors-export that contains the name of creditors in the database.
* Twilio

Get Location
===============

URL: https://debthelpillinois-3927.twil.io/get-location
Parameters: 

Requires one of:

* fullAddress

.. code-block::

   get-county?fullAddress=120 S La Salle St, Chicago, IL 60603, USA
   
* street, city, state, zip

.. code-block::

   get-county?street=120 S LaSalle St&city=Chicago&state=IL&zip=60603

  

Returns an object that contains:

* city
* county
* zip_code
* zip_code_suffix (where available)

.. code-block::

   {"city":"Aurora","county":"Kane County","zip_code":"60505","zip_code_suffix":"4865"}

Requires:

* Google Geocoding API
* Twilio

Get Court Info
================

URL: https://debthelpillinois-3927.twil.io/get-court-info
Parameters: 

Requires name, which must be what the court name starts with. Valid examples include:

* Adams
* Adams County
* Adams County Courthouse
* Cook County: Second

Returns an object that contains:

* name of the court
* circuit
* district
* court general phone number
* clerk phone number
* address
* city
* state
* zip code
* website url to the Illinois courts directory


.. code-block::

   {
  "name": "Cook County: Second Municipal District - Skokie",
  "circuit": "Cook",
  "court_phone_number": "(847) 470-7200",
  "district": "1",
  "clerk_phone_number": "(312) 603-5030",
  "address": "5600 Old Orchard Road",
  "city": "Skokie",
  "state": "Illinois",
  "zip_code": "60077",
  "website": "https://www.illinoiscourts.gov/courts-directory/83/Cook-County-Second-Municipal-District--Skokie/court/"
   }
   
.. note:: If no clerk phone number is available, the court phone number is used instead. If there is no match, the IL court help website and phone number are returned.

Get Debt Entity
===================

Url: https://debthelpillinois-3927.twil.io/get-debt-entity?debt_id=1&api_key=[apikey]

Requires:

* API key
* debt it


Returns an object that includes:

* name of the debt (name)
* amount of the debt
* creditor name
* creditor type
* the term IDs as an array from the field debt metadata.
* interest rate of the debt
* is_debt_collector on/off
* credit_score
* current_problem - taxonomy term ID for the problem type
* debt type, as a label
* city, from the profile
* county, from the profile
* the term IDs as an array from the field profile metadata
* zip code, from the profile
* debt_problem_id = id of the debt problem tied to the debt
* problem_profile_id = profile id associated with the debt
* debt_county = county associated with the debt
* debt_cook_judicial_distrirct = judicial district identified as First, Second, etc from the debt address
* profile_cook_judicial_distrirct = judicial district identified as First, Second, etc from the profile address

For each term ID in the field debt metadata and field profile metadata:

* a key that matches the variable name from that Term ID,
* a value of True


.. code-block::

    {
  "name": "tee",
  "amount": "",
  "creditor_name": "LVNV Funding LLC",
  "creditor_type": "debt_buyer",
  "field_debt_metadata": [
    "132271",
    "132261",
    "134126"
  ],
  "interest_rate": "",
  "is_debt_collector": "On",
  "last_payment_date": "",
  "status": "Enabled",
  "credit_score": "",
  "current_problem": "130116",
  "debt_type": "Credit card debt",
  "city": "",
  "county": "",
  "field_profile_metadata": [
    "132311"
  ],
  "zip_code": "",
  "debt_problem_id": "1021",
  "problem_profile_id": "766",
  "debt_county": "Cook",
  "debt_cook_judicial_district": "1st",
  "profile_cook_judicial_district": "",
  "debt_is_cc_closed": "True",
  "debt_is_debt_buyer": "True",
  "debt_is_debt_collector": "True",
  "profile_military": "True"
   }
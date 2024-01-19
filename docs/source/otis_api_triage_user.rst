=======================
OTIS API Triage User
=======================

This suite of API functions allow for standard CRUD (create-read-update-delete) operations on the Triage User custom entity.


Get Triage User(s)
=====================
Triage user API supports GET commands to return one or more existing triage users.  The JSON API allows for filtering on field parameters.  See the general documentation on `Drupal.org <https://www.drupal.org/docs/core-modules-and-themes/core-modules/jsonapi-module/filtering>`_ for general information on filtering and :ref:`ilao-api-filters` for filter examples.

.. code-block:: php

    GET /jsonapi/oas_triage_user/oas_triage_user?page[limit]=
    GET /jsonapi/oas_triage_user/oas_triage_user/{{uuid}} returns a specific triage user
    GET /jsonapi/oas_triage_user/oas_triage_user?sort=-changed returns the newest
    GET /jsonapi/oas_triage_user/oas_triage_user?filter[county]=Cook&filter[intake_status]=etransferred


Create Triage User
======================
Creating a triage user requires minimally:



.. code-block:: php

    curl -X POST -H "Content-Type:application/vnd.api+json" -H "authorization: Bearer [token]" -d '{
    "data": {
        "type": "oas_triage_user--oas_triage_user",
        "attributes": {
            "status": true,
            "intake_created": "1970-01-01T00:00:00+00:00",
            "intake_changed": "1970-01-01T00:00:00+00:00",
            "household_size": 5,
            "household_adults": 2,
            "household_children": 3,
            "total_income": 0,
            "total_expenses": 0,
            "total_assets": 0,
            "zip_code": "60603",
            "triage_status": "Started",
            "intake_status": null,
            "lsc_code": null,
            "lsc_subcode": null,
            "referral_source": null,
            "county": "Cook",
            "state": "Illinois",
            "ip_address": "10.159.81.163",
            "last_screen_viewed": null,
            "intake_notes": null,
            "gender": null,
            "race": null,
            "ethnicity": null,
            "marital_status": null,
            "citizenship": null,
            "immigrant_status": null,
            "age": null,
            "primary_language": null,
            "country_of_origin": null,
            "overincome": null,
            "etransfer_attempts": 0,
            "etransfer_failure_reason": null,
            "etransfer_status": null,
            "etransfer_data": {
                "": ""
            },
            "hourly_reminder_sent": null,
            "daily_reminder_sent": null,
            "default_langcode": true,
            "oas_mobile_phone": null,
            "oas_opt_in_sms": null,
            "oas_triage_callback_times": [],
            "oas_triage_help_type": [
                "forms"
            ],
			"oas_triage_search": "Child custody"
        },
        "relationships": {
            "oas_triage_user_type": {
                "data": {
                    "type": "oas_triage_user_type--oas_triage_user_type",
                    "id": "ba7bab21-7cdf-4e07-990d-94fda9655f64"
                }
            },
                      "intake_organization": {
                "data": {
                    "type": "oas_intake_settings--oas_intake_settings",
                    "id": "19f38f98-93f2-4209-adaf-608fd97bb530"
                }
            },
            "oas_limited_populations": {
                "data": []
            },
            "oas_triage_problem": {
                "data": {
                    "type": "taxonomy_term--legal_issues",
                    "id": "7e7404dd-49c1-4261-9c5a-acc1fab27dde"
                }
            },
            "oas_triage_problem_history": {
                "data": []
            }
        }
    }
   }' [base url]/jsonapi/oas_triage_user/oas_triage_user


Response
----------

Returns data object containing:

* Type
* ID (the uuid of the triage user created)
* Links
* Attributes (the data of the triage user)




Update triage user
====================

.. code-block:: html

   curl -X PATCH -H "Content-Type:application/vnd.api+json" -H "Authorization: Bearer [token]"-d '{
   "data": {
        "type": "oas_triage_user--oas_triage_user",
        "id": "e08ff647-362f-4428-bcaf-8b45191a8df7",
        "attributes": {
            "household_size": 6,
            "household_children": 4
        }
    }
    }' [baseurl]/jsonapi/oas_triage_user/oas_triage_user/[uuid]

.. note:: The id is required in the url and in the data object.

Response
-------------

Returns data object containing:

* Type
* ID (the uuid of the triage user created)
* Links
* Attributes (the data of the triage user)

Sample Response
-----------------

.. code-block:: json

      {"type":"oas_triage_user--oas_triage_user",
      "id":"049d25f6-1d81-4c05-9455-002c47387007",

     "links":
     {"self":
        {"href":"https://d8dev.illinoislegalaid.org/jsonapi/oas_triage_user/oas_triage_user/049d25f6-1d81-4c05-9455-002c47387007"}},
     "attributes":
     {"drupal_internal__id":3486826,
     "langcode":"en",
     "status":true,
     "created":"2021-04-19T20:06:34+00:00",
     "changed":"2021-04-19T20:06:34+00:00",
     "intake_created":"2021-03-18T00:00:00+00:00",
     "intake_changed":"2021-03-18T00:00:00+00:00",
     "zip_code":"60603",
     "household_size":"7",
     "overincome":null,
    "ip_address":"10.159.81.163",
    "last_screen_viewed":null,
    "county":"Cook","state":"Illinois",
    "household_adults":4,"household_children":3,
    "total_income":0,"total_expenses":0,"total_assets":0,
    "triage_status":"Started","intake_status":null,"lsc_code":null,"lsc_subcode":null,
    "referral_source":"Twilio-Master","intake_notes":null,
     "gender":null,"race":null,"ethnicity":null,"marital_status":null,
     "citizenship":null,"immigrant_status":null,"age":null,
     "primary_language":null,"country_of_origin":null,"etransfer_attempts":0,"
     etransfer_failure_reason":null,"etransfer_status":null,"etransfer_data":{"":""},"
     hourly_reminder_sent":null,"daily_reminder_sent":null,"referral_source_id":{"":""},
     "default_langcode":true,"oas_mobile_phone":"6308811337",
     "oas_opt_in_sms":true,"oas_triage_callback_times":[],
     "oas_triage_help_type":["forms"],
     "oas_triage_search":"Child custody"},
     "relationships":{"oas_triage_user_type":   {"data":
     {"type":"oas_triage_user_type--oas_triage_user_type",
     "id":"ba7bab21-7cdf-4e07-990d-94fda9655f64"},
     "links":{"related":
     {"href":"https://d8dev.illinoislegalaid.org/jsonapi/oas_triage_user/oas_triage_user/049d25f6-1d81-4c05-9455-002c47387007/oas_triage_user_type"},
     "self":
     {"href":"https://d8dev.illinoislegalaid.org/jsonapi/oas_triage_user/oas_triage_user/049d25f6-1d81-4c05-9455-002c47387007/relationships/oas_triage_user_type"}}},"
     user_id":{"data":{"type":"user--user","id":"fc541bd0-bc81-46ef-9f2a-cf443556659e"},
     "links":{"related":
     {"href":"https://d8dev.illinoislegalaid.org/jsonapi/oas_triage_user/oas_triage_user/049d25f6-1d81-4c05-9455-002c47387007/user_id"},
     "self":{"href":"https://d8dev.illinoislegalaid.org/jsonapi/oas_triage_user/oas_triage_user/049d25f6-1d81-4c05-9455-002c47387007/relationships/user_id"}}},"intake_organization":{"data":{"type":
     "oas_intake_settings--oas_intake_settings","id":"19f38f98-93f2-4209-adaf-608fd97bb530"},"
     links":{"related":{"href":"https://d8dev.illinoislegalaid.org/jsonapi/oas_triage_user/oas_triage_user/049d25f6-1d81-4c05-9455-002c47387007/intake_organization"},"self":{"href":"https://d8dev.illinoislegalaid.org/jsonapi/oas_triage_user/oas_triage_user/049d25f6-1d81-4c05-9455-002c47387007/relationships/intake_organization"}}},
     "oas_limited_populations":{"data":[],
     "links":{"related":
     {"href":"https://d8dev.illinoislegalaid.org/jsonapi/oas_triage_user/oas_triage_user/049d25f6-1d81-4c05-9455-002c47387007/oas_limited_populations"},
     "self":{"href":"https://d8dev.illinoislegalaid.org/jsonapi/oas_triage_user/oas_triage_user/049d25f6-1d81-4c05-9455-002c47387007/relationships/oas_limited_populations"}}},
     "oas_triage_problem":
     {"data":
     {"type":"taxonomy_term--legal_issues","id":"7e7404dd-49c1-4261-9c5a-acc1fab27dde"},
     "links":
     {"related":
     {"href":"https://d8dev.illinoislegalaid.org/jsonapi/oas_triage_user/oas_triage_user/049d25f6-1d81-4c05-9455-002c47387007/oas_triage_problem"},
     "self":{"href":"https://d8dev.illinoislegalaid.org/jsonapi/oas_triage_user/oas_triage_user/049d25f6-1d81-4c05-9455-002c47387007/relationships/oas_triage_problem"}}},
     "oas_triage_problem_history":
     {"data":[],
     "links":
     {"related":
     {"href":"https://d8dev.illinoislegalaid.org/jsonapi/oas_triage_user/oas_triage_user/049d25f6-1d81-4c05-9455-002c47387007/oas_triage_problem_history"},
     "self":{"href":"https://d8dev.illinoislegalaid.org/jsonapi/oas_triage_user/oas_triage_user/049d25f6-1d81-4c05-9455-002c47387007/relationships/oas_triage_problem_history"}}}}}

Delete triage user
=====================

   curl -X DELETE [baseurl]/jsonapi/oas_triage_user/oas_triage_user/[uuid]









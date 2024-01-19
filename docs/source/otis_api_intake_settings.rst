===========================
OTIS API Intake Settings
===========================



This suite of API functions allow for standard CRUD (create-read-update-delete) operations on the Intake settings custom entity. The intake settings custom entity contains data that describes a specific organization's service's intake settings, such as income limits, special populations allowed, legal issues associated with the intake settings, callback settings, and messages.


Get Intake Setting
=====================
The API supports GET commands to return one or more existing intake settings.  The JSON API allows for filtering on field parameters.  See the general documentation on `Drupal.org <https://www.drupal.org/docs/core-modules-and-themes/core-modules/jsonapi-module/filtering>`_ for general information on filtering and :ref:`ilao-api-filters` for filter examples.

.. code-block:: php

    GET /jsonapi/oas_intake_settings/oas_intake_settings?page[limit]=
    GET /jsonapi/oas_triage_user/oas_triage_user/{{uuid}} returns a specific triage user
    GET /jsonapi/oas_triage_user/oas_triage_user?sort=-changed returns the newest
    GET /jsonapi/oas_intake_settings/oas_intake_settings?filter[counties][value]=f81da2b5-dd82-42da-ba4a-75fecfef7760&filter[counties][path]=field_counties.id&filter[foo][condition][value][]=1821&filter[foo][condition][value][]=1811&filter[foo][condition][path]=drupal_internal__id&filter[foo][condition][operator]=IN returns the eviction intake setting that matches the county ID and has either an intake settings id of 1821 or 1811.

Response
----------

Returns data object containing:

* Type
* ID (the uuid of the triage user created)
* Links
* Attributes (the data of the intake setting)
* Relationships  (the related entities of the intake setting)

Sample Response
------------------

.. code-block:: json

   {
    "jsonapi": {
        "version": "1.0",
        "meta": {
            "links": {
                "self": {
                    "href": "http://jsonapi.org/format/1.0/"
                }
            }
        }
    },
    "data": [
        {
            "type": "oas_intake_settings--oas_intake_settings",
            "id": "13d32856-e611-4ef8-a501-f111795e6db7",
            "links": {
                "self": {
                    "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7"
                }
            },
            "attributes": {
                "drupal_internal__id": 1821,
                "langcode": "en",
                "status": false,
                "name": "LOLLA housing",
                "created": "2021-04-28T21:51:03+00:00",
                "changed": "2021-05-18T18:46:51+00:00",
                "entity_type": "node",
                "current_count": 0,
                "enabled": false,
                "collect_marital_status": true,
                "collect_immigration": false,
                "collect_citizenship": false,
                "collect_country": false,
                "collect_language": true,
                "collect_gender": true,
                "collect_race": true,
                "collect_ethnicity": true,
                "collect_income": true,
                "collect_assets": false,
                "collect_expenses": false,
                "apply_income_limit": true,
                "apply_asset_limit": false,
                "collect_expenses_over_income": false,
                "allow_prisoners": false,
                "maximum_allowed_income": 80,
                "maximum_allowed_assets": null,
                "personal_exemption_amount": null,
                "intake_limit": 0,
                "reset_limit_frequency": 30,
                "minimum_minor_age": 18,
                "minimum_senior_age": 60,
                "callback_number": "855-601-9474",
                "callback_type": "we_call_client",
                "cms_vendor": null,
                "default_langcode": true,
                "content_translation_source": "und",
                "content_translation_outdated": false,
                "content_translation_created": "2021-04-28T21:51:03+00:00",
                "content_translation_changed": "2021-04-30T18:38:08+00:00",
                "field_bypass_intake_message": {
                    "value": "<p>Please call [OAS:name] at [OAS:phone] for immediate assistance. Tell them you were referred by Illinois Legal Aid Online.</p>\r\n",
                    "format": "basic_html",
                    "processed": "<p>Please call [OAS:name] at [OAS:phone] for immediate assistance. Tell them you were referred by Illinois Legal Aid Online.</p>"
                },
                "field_extended_service_area_yn": false,
                "field_include_exclude_by_type": "counties",
                "field_maximum_callbacks_per_slot": 2,
                "field_same_legal_issues": true,
                "field_same_service_area_as_locat": true,
                "field_statewide": false,
                "oas_help_citizenship_status": {
                    "value": "<p>Your citizenship status help figure out what service you qualify for. If you were born in the United States, got citizenship through a parent or are naturalized, then you are a U.S. citizen. If you have a green card that lets you live and work in the U.S., then you are a Legal Permanent Resident. If you are a victim of domestic abuse, then you may qualify for protection under the Violence Against Women Act (VAWA).</p>\r\n",
                    "format": "basic_html",
                    "processed": "<p>Your citizenship status help figure out what service you qualify for. If you were born in the United States, got citizenship through a parent or are naturalized, then you are a U.S. citizen. If you have a green card that lets you live and work in the U.S., then you are a Legal Permanent Resident. If you are a victim of domestic abuse, then you may qualify for protection under the Violence Against Women Act (VAWA).</p>"
                },
                "oas_help_country_of_origin": {
                    "value": "<p>Please enter the country where you were born. Knowing your home country will help legal aid to better serve you.</p>\r\n",
                    "format": "basic_html",
                    "processed": "<p>Please enter the country where you were born. Knowing your home country will help legal aid to better serve you.</p>"
                },
                "oas_help_ethnicity": {
                    "value": "<p>Please enter your ethnicity. Knowing your ethnicity will help legal aid to better serve you and your community.</p>\r\n",
                    "format": "basic_html",
                    "processed": "<p>Please enter your ethnicity. Knowing your ethnicity will help legal aid to better serve you and your community.</p>"
                },
                "oas_help_gender": {
                    "value": "<p>Please enter whether you are married, single or divorced. If you have never been married, then you are single. If you are living with your spouse, you are married. If you have lived apart from your spouse for more than 6 months or do not know where your spouse is, then you are separated.</p>\r\n",
                    "format": "basic_html",
                    "processed": "<p>Please enter whether you are married, single or divorced. If you have never been married, then you are single. If you are living with your spouse, you are married. If you have lived apart from your spouse for more than 6 months or do not know where your spouse is, then you are separated.</p>"
                },
                "oas_help_immigration_status": {
                    "value": "<p>Your immigration status help figure out what service you qualify for. If you were born in the United States, got citizenship through a parent or are naturalized, then you are a U.S. citizen. If you have a green card that lets you live and work in the U.S., then you are a Legal Permanent Resident. If you are a victim of domestic abuse, then you may qualify for protection under the Violence Against Women Act (VAWA).</p>\r\n",
                    "format": "basic_html",
                    "processed": "<p>Your immigration status help figure out what service you qualify for. If you were born in the United States, got citizenship through a parent or are naturalized, then you are a U.S. citizen. If you have a green card that lets you live and work in the U.S., then you are a Legal Permanent Resident. If you are a victim of domestic abuse, then you may qualify for protection under the Violence Against Women Act (VAWA).</p>"
                },
                "oas_help_language": {
                    "value": "<p>Please enter the language you speak at home. Knowing your language will help legal aid to better serve you.</p>\r\n",
                    "format": "basic_html",
                    "processed": "<p>Please enter the language you speak at home. Knowing your language will help legal aid to better serve you.</p>"
                },
                "oas_help_marital_status": {
                    "value": "<p>Please enter whether you are married, single or divorced. If you have never been married, then you are single. If you are living with your spouse, you are married. If you have lived apart from your spouse for more than 6 months or do not know where your spouse is, then you are separated.</p>\r\n",
                    "format": "basic_html",
                    "processed": "<p>Please enter whether you are married, single or divorced. If you have never been married, then you are single. If you are living with your spouse, you are married. If you have lived apart from your spouse for more than 6 months or do not know where your spouse is, then you are separated.</p>"
                },
                "oas_help_race": {
                    "value": "<p>Please enter your race. Knowing your race will help legal aid to better serve you and your community.</p>\r\n",
                    "format": "basic_html",
                    "processed": "<p>Please enter your race. Knowing your race will help legal aid to better serve you and your community.</p>"
                },
                "oas_household_definition": {
                    "value": "<p>Children and adults should be counted as follows:</p>\r\n\r\n<ul>\r\n\t<li>Count yourself</li>\r\n\t<li>Count each child living with you who is under 18 years;</li>\r\n\t<li>Count your spouse if they live in your home. Do not count your spouse if you are asking for legal help against them.</li>\r\n\t<li>Count each adult that you have one or more children with and who lives in the same home as you. Do not count this adult if you are asking for legal help against them. Do not count this adult if you have no access to their income.</li>\r\n\t<li>Count each adult who lives in your home but does not pay for rent or food and does not share any children with you</li>\r\n</ul>\r\n",
                    "format": "basic_html",
                    "processed": "<p>Children and adults should be counted as follows:</p>\n\n<ul><li>Count yourself</li>\n\t<li>Count each child living with you who is under 18 years;</li>\n\t<li>Count your spouse if they live in your home. Do not count your spouse if you are asking for legal help against them.</li>\n\t<li>Count each adult that you have one or more children with and who lives in the same home as you. Do not count this adult if you are asking for legal help against them. Do not count this adult if you have no access to their income.</li>\n\t<li>Count each adult who lives in your home but does not pay for rent or food and does not share any children with you</li>\n</ul>"
                },
                "oas_msg_already_applied": {
                    "value": "<p>You can not use this online form if you are already a client with [OAS:name] for this problem. Please call [OAS:call-back-number] for more information.</p>\r\n",
                    "format": "basic_html",
                    "processed": "<p>You can not use this online form if you are already a client with [OAS:name] for this problem. Please call [OAS:call-back-number] for more information.</p>"
                },
                "oas_msg_current_client": {
                    "value": "<p>You can not use this online form if you are already a client with [OAS:name] for this problem. Please call [OAS:call-back-number] for more information.</p>\r\n",
                    "format": "basic_html",
                    "processed": "<p>You can not use this online form if you are already a client with [OAS:name] for this problem. Please call [OAS:call-back-number] for more information.</p>"
                },
                "oas_msg_disclaimer": null,
                "oas_msg_please_call": {
                    "value": "Please call [OAS:Name] at [OAS:Phone] between 9:00am&nbsp;- 4:00pm&nbsp;Monday, Wednesday, and Friday or Tuesday and&nbsp;Thursday and between 9:00am - 6:00pm.",
                    "format": "full_html",
                    "processed": "Please call  at  between 9:00am - 4:00pm Monday, Wednesday, and Friday or Tuesday and Thursday and between 9:00am - 6:00pm."
                },
                "oas_msg_we_call_you": {
                    "value": "To get help, you <b>must speak with the staff</b> at [OAS:Name]. If they do not reach you in the next week, please call [[855-601-9474]] between the hours of 9:00 am and 3:30 pm Monday through Friday. Tell them you applied online.",
                    "format": "full_html",
                    "processed": "To get help, you <b>must speak with the staff</b> at . If they do not reach you in the next week, please call [[855-601-9474]] between the hours of 9:00 am and 3:30 pm Monday through Friday. Tell them you applied online."
                }
            },
            "relationships": {
                "oas_intake_settings_type": {
                    "data": {
                        "type": "oas_intake_settings_type--oas_intake_settings_type",
                        "id": "57eb487c-b45f-46df-88ed-eaa85c8c0465"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/oas_intake_settings_type"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/relationships/oas_intake_settings_type"
                        }
                    }
                },
                "user_id": {
                    "data": {
                        "type": "user--user",
                        "id": "5d8a1c93-17a0-4b0c-9ff4-3b057b6dc488"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/user_id"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/relationships/user_id"
                        }
                    }
                },
                "entity_id": {
                    "data": {
                        "type": "node--location_services",
                        "id": "81c1d425-1bf1-4611-9a92-ad8566fd3fea"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/entity_id"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/relationships/entity_id"
                        }
                    }
                },
                "content_translation_uid": {
                    "data": {
                        "type": "user--user",
                        "id": "5d8a1c93-17a0-4b0c-9ff4-3b057b6dc488"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/content_translation_uid"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/relationships/content_translation_uid"
                        }
                    }
                },
                "field_cities": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/field_cities"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/relationships/field_cities"
                        }
                    }
                },
                "field_counties": {
                    "data": [
                        {
                            "type": "taxonomy_term--region",
                            "id": "2bc153ae-29d8-4d0e-8abb-623f6fcefae0"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "5d51d669-3adc-4063-8384-2cb64666df1e"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "6c720514-f64d-4955-9b03-4949c4c7c4ab"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "6beb3364-097b-4514-8c3a-9911ba5ff634"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "ed1f9847-893a-48f4-945a-432b4a71890b"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "5737e434-3176-44a6-9996-e85b055a33ed"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "98f7817f-7d06-44df-acdc-d18b4a375288"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "3fcfba49-74bf-43a5-a649-c945befa7d71"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "f331b710-b461-4a81-980d-468452a19c7d"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "753be63b-b98d-4610-8157-ebaa1c27d48e"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "e902b073-793e-4b06-8c18-885ff2230160"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "ed01d348-3b9c-42cf-bb4f-c994d2894540"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "91f438c9-41f8-49c5-a8e9-b041e9417df2"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "e1d971eb-cc81-465e-bfb5-741a20f35822"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "ba34a85d-88d0-49f1-b922-5e45e955befb"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "21bbcfec-956f-4e0c-8b33-3cab233bc423"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "0654eaae-ced2-45ab-8cff-91bd8eea515b"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "ac3187c2-2630-4314-ad56-e6c1e2438f9e"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "d13033b4-5c28-4458-a7b8-5e51e4a8e8e1"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "7e5c799c-8b59-455c-9c20-80649621d72b"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "cfd89cba-277d-4ef2-b6ae-bd75f63c6560"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "69b6019f-290d-4bbc-8bb3-ac9de4ea393a"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "448e0672-f4ee-4490-8027-74e7122cde71"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "89b4a396-34d8-4e13-add5-a4f244285027"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "f81da2b5-dd82-42da-ba4a-75fecfef7760"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "e0d03264-33fe-451c-9aa4-7944b729d2f5"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "47c238a4-ad8f-4623-b645-3305b7488339"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "df96a293-fe57-4940-b175-0870c3240331"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "59e6ff2b-acf4-421a-a78d-138224f1eff3"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "9e47ccb6-c9fd-4436-987d-6dc10cd6c646"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "c4885642-df96-4f86-8788-e7e489f6de29"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "ece7ca28-aac0-487f-a098-74b163593342"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "efb45015-10c3-4639-975f-48cd6db203de"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "3ed4870e-b238-446f-a840-bbef4ad3c253"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "b698b866-9a12-42ff-862f-60baadfd618e"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "388bd23b-996b-4476-8fe4-bf3fdb75ca7f"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "f5812717-6795-4d4a-a108-b0b2b7d13d50"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "09c75e15-bdb3-4c64-9b79-1149870cdc08"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "4ec167bc-3cee-4dd3-96c4-44914fad8759"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "c0efc8a8-3591-4cad-b3d7-d15d42f9952b"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "bb2b8be3-b796-4c13-9576-48679b932a4c"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "fc455d3e-2332-4e9e-8013-f76cdb12eb83"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "4b3aa167-8291-4ec2-8974-55e5561258ec"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "fe7d117f-3564-4285-811e-27bb68dc5382"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "82044a8f-abe0-4522-801c-82be064d4594"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "f25276cc-890f-49d8-99c7-521f0246d884"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "71c00c8b-0bd0-4fc6-8f3f-9878dc4851fc"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "8a7c7ac4-fecd-4a1c-a011-f07005c10e2b"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "1616bab3-6014-4970-bbc5-7face3e84389"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "3d90181c-b8a5-49e3-b64e-d8f2dab78d45"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "2e4691e7-16a3-4442-8e47-2cf1522dfb72"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "565f1bac-905f-47d1-8072-c6786a8dc3ba"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "e78a959e-6bb9-4ea9-865d-397032769217"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "0355f1ee-d4cc-4001-8501-49a1ff98a6f5"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "ec2d4ef3-bcb4-4984-91f7-902a35a5de4c"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "ded3cea9-0024-47cc-8ffe-71db1d31b431"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "095a37d4-5e42-4d44-ac62-1fbf36a89ad9"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "28e4e22f-09fd-461e-8061-90dca86c6260"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "2a1ca9e9-934f-4e3d-8c1c-b3b2334e25d1"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "47266499-fbe6-4e3b-932f-cc2870f6229e"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "abc00203-fee7-43d9-95a2-51ce07761a29"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "4549199d-a8a8-4006-bced-4eb96047c913"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "71c4db57-aa26-4310-933c-b5882a4b8f81"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "ac273e74-ee3e-4f11-b71a-fcd335730961"
                        },
                        {
                            "type": "taxonomy_term--region",
                            "id": "819d510c-4cd9-4d86-bcc0-75856bc52360"
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/field_counties"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/relationships/field_counties"
                        }
                    }
                },
                "field_extended_service_area": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/field_extended_service_area"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/relationships/field_extended_service_area"
                        }
                    }
                },
                "field_legal_issues": {
                    "data": [
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "0f5dfdec-bf0f-490b-9b38-bab871db7cab"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "7ad714fb-d610-4a0d-87ec-9b5946bec20a"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "3d5c2b0d-bf95-4997-bb48-7d6ac6188fee"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "27fadc93-9b6f-4f46-a3cb-0446f079a7cb",
                            "meta": {
                                "arity": 0
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "fb78ab72-8572-449d-be5a-008b051c05e7"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "e46fe9e2-d89b-481c-a00a-8276092182db"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "27fadc93-9b6f-4f46-a3cb-0446f079a7cb",
                            "meta": {
                                "arity": 1
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "398ff1ca-abcf-48b7-86db-69819d319b9f"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "8ea719a9-136c-48e1-a2b4-6f2f20968491"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "f8040c1f-4d0a-480f-9a9e-4017c1000654"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "6471a292-6364-4078-bcc2-46b81a199789"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "110c787b-a802-48a1-9073-86c9d44b508e"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "d0f96f4e-bb9c-40b3-8163-3c588be16245"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "fa92bc5d-2036-4f4a-98d2-056b4fb02ddd"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "1cc27a2d-6e6d-4e6b-b610-2e53e328047c"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "15e034ba-c4a5-4d38-9b1c-7b250c69b261",
                            "meta": {
                                "arity": 0
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "e52c9971-7ff8-47da-b8c7-5c8c6bcd3be1"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "83d267ae-fb1f-4e9f-ae26-cceb98f5dfd3"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "abdc7dc2-9310-4fcb-a9e3-85ab59364490"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "0482a394-7f67-4aff-a8b5-12ddcaba4a68"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "527e2fd3-83b9-4369-86a5-9ce837f4450e"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "97122998-8104-4f51-b3a2-8ccee4042f22"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "459b7c77-9f0e-4ff8-948f-a13989acff63"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "30489cd9-183e-4322-8eec-91a6f0a90fa9"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "b59f58e8-68ae-4ba8-bda4-7a0099d90b2c"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "6067e120-aa11-430a-8045-50d17335d34b"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "3566a439-aba2-419a-8184-a65c69ad544e"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "0dc5c360-4de0-499b-a769-4899a2ddef5f"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "beb8416c-cb25-4dc4-9f0e-9a6f8e23a86a"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "efde7a22-f1bd-4826-ade4-734bc566014f"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "fd9053cc-4f67-43a2-b824-0a5412218e1b"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "1e762e80-0a9f-4bfb-813b-e01677028cd1"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "a94de4ba-0286-41c6-b040-e40e9a05a4a5",
                            "meta": {
                                "arity": 0
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "15e034ba-c4a5-4d38-9b1c-7b250c69b261",
                            "meta": {
                                "arity": 1
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "15e034ba-c4a5-4d38-9b1c-7b250c69b261",
                            "meta": {
                                "arity": 2
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "3d8b1df2-c8df-45e9-a19b-f53a4b927d94"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "5df15921-810a-4ee2-82a6-35293059df57"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "dc10af42-b03c-48da-9a0d-38dd61f3fb72"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "5f0db83b-b300-4b6f-bf84-dfe46e395257"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "ccce2915-de76-4c8b-b791-30df0d9863b0",
                            "meta": {
                                "arity": 0
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "5cd4918d-de2f-4f05-b96c-6a9028dc3c95",
                            "meta": {
                                "arity": 0
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "10b3483a-7045-4bf0-aa08-8c4301ed7d33",
                            "meta": {
                                "arity": 0
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "115adc77-9819-48b4-b225-40cbe0a24199",
                            "meta": {
                                "arity": 0
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "e0552405-c2ee-4d2e-88ff-c44c0331fabd",
                            "meta": {
                                "arity": 0
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "06a13100-d10b-447c-bad8-8bfe0bf0e2b2",
                            "meta": {
                                "arity": 0
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "1eeade01-8a10-41e8-b03e-f7f3d3d8c1cb",
                            "meta": {
                                "arity": 0
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "40d98af0-fdf1-4336-9738-426ef72b193c"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "e59fa961-8e56-42ba-8551-bdb149ea1fea"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "0c8debb3-f602-4d42-83b0-d4f05a7d4847"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "f5d1b6c5-ba5c-4a60-b4d3-2171d59124d7"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "785eb68a-49fc-452b-ac38-00f30dc1a6de"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "db07eb50-0ca6-4e95-80d0-60fc675b4789"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "e3cb3e6a-3bb3-440f-b9f9-7e149236ced6"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "80d8573a-a402-4ef8-86ec-f80c43332783"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "2a2bddba-2d78-4960-9a0a-4e7ba52e0030"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "27fadc93-9b6f-4f46-a3cb-0446f079a7cb",
                            "meta": {
                                "arity": 2
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "15e034ba-c4a5-4d38-9b1c-7b250c69b261",
                            "meta": {
                                "arity": 3
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "a1cf8331-8a9c-48f1-b945-81061ca4734e"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "21c5e64d-7b07-4b18-a911-d084c42b90ec"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "058c6f15-b3cd-4f7f-8c15-ee4be0b4e270"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "a94de4ba-0286-41c6-b040-e40e9a05a4a5",
                            "meta": {
                                "arity": 1
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "47ceec7b-2e6b-4f55-b4a1-74eb76def0d0"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "46a00e87-e1ec-41b5-acb9-452d6484b799"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "b2a63642-b3a2-4ea2-90c2-9084a2969983"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "e3bdc4a9-81cb-43f1-a31c-3c7e7e19083c"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "050b92e0-9271-4767-ba24-d060ebac0d6e"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "c88332c8-8f88-474e-b69a-1e592aa7d5a4"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "329d07f3-a228-4c86-aab3-4461f9177322"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "caefc5a9-1bdc-4e7a-bc46-65356eb43ad0"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "ccce2915-de76-4c8b-b791-30df0d9863b0",
                            "meta": {
                                "arity": 1
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "5cd4918d-de2f-4f05-b96c-6a9028dc3c95",
                            "meta": {
                                "arity": 1
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "10b3483a-7045-4bf0-aa08-8c4301ed7d33",
                            "meta": {
                                "arity": 1
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "115adc77-9819-48b4-b225-40cbe0a24199",
                            "meta": {
                                "arity": 1
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "e0552405-c2ee-4d2e-88ff-c44c0331fabd",
                            "meta": {
                                "arity": 1
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "06a13100-d10b-447c-bad8-8bfe0bf0e2b2",
                            "meta": {
                                "arity": 1
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "1eeade01-8a10-41e8-b03e-f7f3d3d8c1cb",
                            "meta": {
                                "arity": 1
                            }
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/field_legal_issues"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/relationships/field_legal_issues"
                        }
                    }
                },
                "field_oas_callback_hours_fri": {
                    "data": [
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "a18dc723-7c25-4df7-9792-61984df3d8e7"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "313edc76-daff-4075-a88d-7356bdf41019"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "27f444dd-bae0-4835-94ff-22f9521e9799"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "a59db229-4f54-4724-a4aa-4e7e1a4b4255"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "d3b1b4e2-b2d4-4be0-a12e-6bc423bcd3e5"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "1c478e60-677c-4bd8-852c-1212070f5e24"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "de231376-1587-49df-9633-e15fae83b47e"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "d082e675-d5dc-48ea-8425-279a6f19d753"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "e0efe8fa-4ae7-44be-aee4-ea9e64fc571d"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "3133ab27-e6de-44f9-a40c-b70e1b6267ba"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "0f2923ff-6b7a-42cb-a5d1-68ca53f5aec6"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "593d4809-1106-43d5-8f1b-d2a4b812d84d"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "5321fc4b-493a-4643-83e0-16ae77725de4"
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/field_oas_callback_hours_fri"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/relationships/field_oas_callback_hours_fri"
                        }
                    }
                },
                "field_oas_callback_hours_mon": {
                    "data": [
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "a18dc723-7c25-4df7-9792-61984df3d8e7"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "313edc76-daff-4075-a88d-7356bdf41019"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "27f444dd-bae0-4835-94ff-22f9521e9799"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "a59db229-4f54-4724-a4aa-4e7e1a4b4255"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "d3b1b4e2-b2d4-4be0-a12e-6bc423bcd3e5"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "1c478e60-677c-4bd8-852c-1212070f5e24"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "de231376-1587-49df-9633-e15fae83b47e"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "d082e675-d5dc-48ea-8425-279a6f19d753"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "e0efe8fa-4ae7-44be-aee4-ea9e64fc571d"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "3133ab27-e6de-44f9-a40c-b70e1b6267ba"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "0f2923ff-6b7a-42cb-a5d1-68ca53f5aec6"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "593d4809-1106-43d5-8f1b-d2a4b812d84d"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "5321fc4b-493a-4643-83e0-16ae77725de4"
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/field_oas_callback_hours_mon"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/relationships/field_oas_callback_hours_mon"
                        }
                    }
                },
                "field_oas_callback_hours_sat": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/field_oas_callback_hours_sat"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/relationships/field_oas_callback_hours_sat"
                        }
                    }
                },
                "field_oas_callback_hours_sun": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/field_oas_callback_hours_sun"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/relationships/field_oas_callback_hours_sun"
                        }
                    }
                },
                "field_oas_callback_hours_thu": {
                    "data": [
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "a18dc723-7c25-4df7-9792-61984df3d8e7"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "313edc76-daff-4075-a88d-7356bdf41019"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "27f444dd-bae0-4835-94ff-22f9521e9799"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "a59db229-4f54-4724-a4aa-4e7e1a4b4255"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "d3b1b4e2-b2d4-4be0-a12e-6bc423bcd3e5"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "1c478e60-677c-4bd8-852c-1212070f5e24"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "de231376-1587-49df-9633-e15fae83b47e"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "d082e675-d5dc-48ea-8425-279a6f19d753"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "e0efe8fa-4ae7-44be-aee4-ea9e64fc571d"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "3133ab27-e6de-44f9-a40c-b70e1b6267ba"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "0f2923ff-6b7a-42cb-a5d1-68ca53f5aec6"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "593d4809-1106-43d5-8f1b-d2a4b812d84d"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "5321fc4b-493a-4643-83e0-16ae77725de4"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "24de729d-b53e-44e5-9736-af13a6ce1490"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "bb4dad57-ec16-4a44-9ef3-3a9880d779ed"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "39ed2ed4-d30d-4343-80ea-2473eb72c181"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "85d604ab-c6ce-477b-a744-555fb9db1206"
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/field_oas_callback_hours_thu"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/relationships/field_oas_callback_hours_thu"
                        }
                    }
                },
                "field_oas_callback_hours_tue": {
                    "data": [
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "a18dc723-7c25-4df7-9792-61984df3d8e7"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "313edc76-daff-4075-a88d-7356bdf41019"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "27f444dd-bae0-4835-94ff-22f9521e9799"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "a59db229-4f54-4724-a4aa-4e7e1a4b4255"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "d3b1b4e2-b2d4-4be0-a12e-6bc423bcd3e5"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "1c478e60-677c-4bd8-852c-1212070f5e24"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "de231376-1587-49df-9633-e15fae83b47e"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "d082e675-d5dc-48ea-8425-279a6f19d753"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "e0efe8fa-4ae7-44be-aee4-ea9e64fc571d"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "3133ab27-e6de-44f9-a40c-b70e1b6267ba"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "0f2923ff-6b7a-42cb-a5d1-68ca53f5aec6"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "593d4809-1106-43d5-8f1b-d2a4b812d84d"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "5321fc4b-493a-4643-83e0-16ae77725de4"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "24de729d-b53e-44e5-9736-af13a6ce1490"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "bb4dad57-ec16-4a44-9ef3-3a9880d779ed"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "39ed2ed4-d30d-4343-80ea-2473eb72c181"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "85d604ab-c6ce-477b-a744-555fb9db1206"
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/field_oas_callback_hours_tue"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/relationships/field_oas_callback_hours_tue"
                        }
                    }
                },
                "field_oas_callback_hours_wed": {
                    "data": [
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "a18dc723-7c25-4df7-9792-61984df3d8e7"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "313edc76-daff-4075-a88d-7356bdf41019"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "27f444dd-bae0-4835-94ff-22f9521e9799"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "a59db229-4f54-4724-a4aa-4e7e1a4b4255"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "d3b1b4e2-b2d4-4be0-a12e-6bc423bcd3e5"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "1c478e60-677c-4bd8-852c-1212070f5e24"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "de231376-1587-49df-9633-e15fae83b47e"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "d082e675-d5dc-48ea-8425-279a6f19d753"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "e0efe8fa-4ae7-44be-aee4-ea9e64fc571d"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "3133ab27-e6de-44f9-a40c-b70e1b6267ba"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "0f2923ff-6b7a-42cb-a5d1-68ca53f5aec6"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "593d4809-1106-43d5-8f1b-d2a4b812d84d"
                        },
                        {
                            "type": "taxonomy_term--oas_callback_hours",
                            "id": "5321fc4b-493a-4643-83e0-16ae77725de4"
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/field_oas_callback_hours_wed"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/relationships/field_oas_callback_hours_wed"
                        }
                    }
                },
                "field_service_single": {
                    "data": {
                        "type": "node--location_services",
                        "id": "81c1d425-1bf1-4611-9a92-ad8566fd3fea"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/field_service_single"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/relationships/field_service_single"
                        }
                    }
                },
                "field_zipcodes": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/field_zipcodes"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/relationships/field_zipcodes"
                        }
                    }
                },
                "oas_asset_categories": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/oas_asset_categories"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/relationships/oas_asset_categories"
                        }
                    }
                },
                "oas_expense_categories": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/oas_expense_categories"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/relationships/oas_expense_categories"
                        }
                    }
                },
                "oas_income_categories": {
                    "data": [
                        {
                            "type": "ilao_oas_financial_category--income_types",
                            "id": "408755a7-1aa6-48e3-bc90-14120b5892aa"
                        },
                        {
                            "type": "ilao_oas_financial_category--income_types",
                            "id": "d3d833a8-b257-4795-bbba-3c97b1bd3f8d"
                        },
                        {
                            "type": "ilao_oas_financial_category--income_types",
                            "id": "9da91c83-605d-4d03-bde8-a8db02b78683"
                        },
                        {
                            "type": "ilao_oas_financial_category--income_types",
                            "id": "9005b1e7-4c73-42ae-ab10-e528b880975c"
                        },
                        {
                            "type": "ilao_oas_financial_category--income_types",
                            "id": "62e563bd-0780-47b5-b97d-8de9056febbb"
                        },
                        {
                            "type": "ilao_oas_financial_category--income_types",
                            "id": "fa1b2885-a0be-4934-be98-fc36e74e4e78"
                        },
                        {
                            "type": "ilao_oas_financial_category--income_types",
                            "id": "be2d1f09-0d45-4101-b0ca-fdb11870e6b8"
                        },
                        {
                            "type": "ilao_oas_financial_category--income_types",
                            "id": "11fb9826-2031-4231-91bf-95e8f33eb8bd"
                        },
                        {
                            "type": "ilao_oas_financial_category--income_types",
                            "id": "f42ae4b8-2789-4d03-8ea8-1de2385b6ef3"
                        },
                        {
                            "type": "ilao_oas_financial_category--income_types",
                            "id": "fca7cb0d-44a0-491a-be7f-9d8580e1e249"
                        },
                        {
                            "type": "ilao_oas_financial_category--income_types",
                            "id": "3e670824-43f3-4aa3-883d-ba05cbee1f75"
                        },
                        {
                            "type": "ilao_oas_financial_category--income_types",
                            "id": "f0cecdb9-dd03-4b97-962b-632f1a77b816"
                        },
                        {
                            "type": "ilao_oas_financial_category--income_types",
                            "id": "6c372502-330d-470e-8551-8f17d83f1479"
                        },
                        {
                            "type": "ilao_oas_financial_category--income_types",
                            "id": "7fb927f7-c174-40ec-8cd2-fccf17e0e010"
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/oas_income_categories"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/relationships/oas_income_categories"
                        }
                    }
                },
                "oas_income_exempt": {
                    "data": [
                        {
                            "type": "taxonomy_term--intake_populations",
                            "id": "1f55dbb3-22d2-46e3-8f18-c70014519f70"
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/oas_income_exempt"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/relationships/oas_income_exempt"
                        }
                    }
                },
                "oas_income_standard": {
                    "data": {
                        "type": "income_standard--income_standard",
                        "id": "8c130e8d-26b7-47ec-b25b-03718d2656e2"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/oas_income_standard"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings/13d32856-e611-4ef8-a501-f111795e6db7/relationships/oas_income_standard"
                        }
                    }
                }
            }
        }
    ],
    "links": {
        "self": {
            "href": "https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings?filter%5Bcounties%5D%5Bpath%5D=field_counties.id&filter%5Bcounties%5D%5Bvalue%5D=f81da2b5-dd82-42da-ba4a-75fecfef7760&filter%5Bfoo%5D%5Bcondition%5D%5Boperator%5D=IN&filter%5Bfoo%5D%5Bcondition%5D%5Bpath%5D=drupal_internal__id&filter%5Bfoo%5D%5Bcondition%5D%5Bvalue%5D%5B0%5D=1811&filter%5Bfoo%5D%5Bcondition%5D%5Bvalue%5D%5B1%5D=1821"
        }
    }
  }



Create intake setting
======================
Creating an intake setting requires minimally the following attributes:

* name
* reset_limit_frequency.  This should be 1, 7, or 30
* callback_number
* callback_type.  This should be we_call_client or client_calls
* field_bypsss_intake_message.  This can be set to "" but is a required element.
* oas_help_race. This can be set to "" but is a required element.
* oas_help_gender.  This can be set to "" but is a required element.
* oas_help_marital_status.  This can be set to "" but is a required element.
* oas_help_language.  This can be set to "" but is a required element.
* oas_help_immigration_status.  This can be set to "" but is a required element.
* oas_help_ethnicity.  This can be set to "" but is a required element.
* oas_help_country_of_origin.  This can be set to "" but is a required element.
* oas_help_citizenship_status.  This can be set to "" but is a required element.
* oas_msg_current_client
* oas_msg_already_applied


And the following relationships:

* entity_id.  This should be the UUID of the service associated with the intake setting
* field_service_single. This should be the UUID of the service associated with the intake setting

Sample request
----------------

.. code-block:: json

   {
    "data": {
        "type": "oas_intake_settings--oas_intake_settings",
        "attributes": {

            "name": "Gwen test",
            "reset_limit_frequency": 1,
            "callback_number": "630-881-1337",
            "callback_type": "we_call_client",
            "field_bypass_intake_message": "",
            "oas_msg_current_client": "Text",
            "oas_msg_already_applied": "Message",
            "oas_household_definition": "",
            "oas_help_race": "",
            "oas_help_gender": "",
            "oas_help_marital_status": "",
            "oas_help_language": "",
            "oas_help_immigration_status": "",
            "oas_help_ethnicity": "",
            "oas_help_country_of_origin": "",
            "oas_help_citizenship_status": ""
        },
        "relationships": {
            "entity_id": {
                "data": {
                    "type": "node--location_services",
                    "id": "3356a19b-396d-4e9c-8e9c-fa97822b1b1c"
                }
            },
            "field_service_single": {
                "data": {
                    "type": "node--location_services",
                    "id": "3356a19b-396d-4e9c-8e9c-fa97822b1b1c"
                }
            }
        }
    }
  }



Update intake setting
========================

.. code-block:: html

   curl -X PATCH -H "Content-Type:application/vnd.api+json" -H "Authorization: Bearer [token]"-d '{
   "data": {"type":"oas_intake_settings--oas_intake_settings",
      "id": "13d32856-e611-4ef8-a501-f111795e6db7",
      "attributes":
      {"status":false,
       "enabled":false
      }
     }
    }' [baseurl]/jsonapi/oas_triage_user/oas_triage_user/[uuid]

.. note:: The uuid is required in the url and in the data object.




Delete intake setting
=========================

   curl -X DELETE [baseurl]/jsonapi/oas_intake_settings/oas_intake_settings/[uuid]










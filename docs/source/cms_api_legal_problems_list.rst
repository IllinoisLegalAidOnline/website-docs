.. _legal-problems-list-api:

====================================
Content API: Legal Problems List
====================================

Returns a list of legal problem content from the website.

Function call
=================

Method: GET

URLs:

* https://www.illinoislegalaid.org/jsonapi/node/legal_problem (English)
* https://www.illinoislegalaid.org/es/jsonapi/node/legal_problem (Spanish)
* https://www.illinoislegalaid.org/pl/jsonapi/node/legal_problem (Polish)

Parameters
=================
Any parameter supported by the JSONAPI is supported. See the :ref:`ilao-api-filters` for filter examples.


Sample Output
==================

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
            "type": "node--legal_problem",
            "id": "9cff9122-2e2e-404a-b909-bf58955c40a6",
            "links": {
                "self": {
                    "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6?resourceVersion=id%3A2247241"
                }
            },
            "attributes": {
                "drupal_internal__nid": 166811,
                "drupal_internal__vid": 2247241,
                "langcode": "en",
                "revision_timestamp": "2021-04-21T16:59:26+00:00",
                "revision_log": null,
                "status": true,
                "title": "Unemployed",
                "created": "2021-04-21T13:47:25+00:00",
                "changed": "2021-04-21T16:59:26+00:00",
                "promote": false,
                "sticky": false,
                "default_langcode": true,
                "revision_translation_affected": true,
                "moderation_state": null,
                "scheduled_transition_date": [],
                "scheduled_transition_state": [],
                "metatag": null,
                "path": {
                    "alias": null,
                    "pid": null,
                    "langcode": "en"
                },
                "content_translation_source": "und",
                "content_translation_outdated": false,
                "field_content_description": "Information on getting a job, getting unemployment insurance (ui) benefits, and other help for people out of work.",
                "field_disambiguation_description": null,
                "field_legal_position": 0,
                "field_meta_description": "Information on getting a job, getting unemployment insurance (ui) benefits, and other help for people out of work.",
                "field_request_translation": "0",
                "field_stage": null,
                "field_subtype": [
                    "Lost my job"
                ],
                "field_translation_outdated": false
            },
            "relationships": {
                "node_type": {
                    "data": {
                        "type": "node_type--node_type",
                        "id": "79426c1d-1fa1-490c-9afc-9d766550d0f4"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/node_type?resourceVersion=id%3A2247241"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/relationships/node_type?resourceVersion=id%3A2247241"
                        }
                    }
                },
                "revision_uid": {
                    "data": {
                        "type": "user--user",
                        "id": "a230c24c-033c-4bfc-b1bf-5e5266dc0022"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/revision_uid?resourceVersion=id%3A2247241"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/relationships/revision_uid?resourceVersion=id%3A2247241"
                        }
                    }
                },
                "uid": {
                    "data": {
                        "type": "user--user",
                        "id": "a230c24c-033c-4bfc-b1bf-5e5266dc0022"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/uid?resourceVersion=id%3A2247241"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/relationships/uid?resourceVersion=id%3A2247241"
                        }
                    }
                },
                "field_citation": {
                    "data": [
                        {
                            "type": "paragraph--citation",
                            "id": "3521f84a-61c6-434a-a40b-7cdccdfb88d0",
                            "meta": {
                                "target_revision_id": 1415846
                            }
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/field_citation?resourceVersion=id%3A2247241"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/relationships/field_citation?resourceVersion=id%3A2247241"
                        }
                    }
                },
                "field_content_management_tags": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/field_content_management_tags?resourceVersion=id%3A2247241"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/relationships/field_content_management_tags?resourceVersion=id%3A2247241"
                        }
                    }
                },
                "field_frequently_asked_questions": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/field_frequently_asked_questions?resourceVersion=id%3A2247241"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/relationships/field_frequently_asked_questions?resourceVersion=id%3A2247241"
                        }
                    }
                },
                "field_legal_code": {
                    "data": [
                        {
                            "type": "taxonomy_term--legal_server_problem_mappings",
                            "id": "a430a8f4-aba7-4edf-a088-747000bf9b61"
                        },
                        {
                            "type": "taxonomy_term--list_taxonomy",
                            "id": "58afdb52-106a-4628-9bcb-3cba62b3e95c"
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/field_legal_code?resourceVersion=id%3A2247241"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/relationships/field_legal_code?resourceVersion=id%3A2247241"
                        }
                    }
                },
                "field_legal_issues": {
                    "data": [
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "39affc4e-e0e0-4091-addc-c049916dedfc"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "afa23f49-7a9d-4caf-b9ac-63da005dc20a"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "dc2775b1-8496-4c61-aead-c1a7ba9c7057"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "07e93281-c797-430b-afc8-b0f16d4c50db"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "746c32e5-7cab-48b6-94ac-3a84dbb16b56"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "4b215793-795c-417c-b695-af07a83488b9"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "d631f776-74a9-48b3-be06-a1f0dbe190d8"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "56a93890-a647-440a-a894-e901f1ebbd76"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "cb6d0287-0e01-45f2-9932-a62aa2e019db"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "f9972f15-ca99-45ef-a1ee-78551072c802"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "6234d16c-ae20-4f50-8176-0bce8ada55b7"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "4eff1598-3467-42da-89b2-d6c2506fdda9"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "0bf7860f-eb26-4f0d-b842-8b2569343011"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "ef38bc1b-a677-4724-87c7-1d35bc1adcb0"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "1aa45d04-a4d6-46e1-ac02-c80f1699dd2b"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "67c0d30d-db16-4c6e-b21a-616e977ec573"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "c4c213b6-b5e2-4316-919e-9d091e4cf4a4"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "ff1d679d-d21c-4e72-8a80-5d191ebeb78e"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "0045024c-4d49-4ce6-b808-9d082911a4a2"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "88b02ec8-5b14-48b9-bb2a-7a0c0a96586a"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "22c61117-a086-4d5b-873b-a4c46d86555c"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "d21ec8d1-bb7d-456a-8252-cf2aaf26f55c"
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/field_legal_issues?resourceVersion=id%3A2247241"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/relationships/field_legal_issues?resourceVersion=id%3A2247241"
                        }
                    }
                },
                "field_life_area_affected": {
                    "data": [
                        {
                            "type": "taxonomy_term--life_areas",
                            "id": "08cb6833-db67-4b78-a0eb-e7f5a3400c83"
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/field_life_area_affected?resourceVersion=id%3A2247241"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/relationships/field_life_area_affected?resourceVersion=id%3A2247241"
                        }
                    }
                },
                "field_media_image": {
                    "data": null,
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/field_media_image?resourceVersion=id%3A2247241"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/relationships/field_media_image?resourceVersion=id%3A2247241"
                        }
                    }
                },
                "field_possible_solution": {
                    "data": [
                        {
                            "type": "node--legal_solution",
                            "id": "608b2d24-b283-46ec-a8e0-4fb2ec920b2d"
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/field_possible_solution?resourceVersion=id%3A2247241"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/relationships/field_possible_solution?resourceVersion=id%3A2247241"
                        }
                    }
                },
                "field_primary_legal_category": {
                    "data": {
                        "type": "taxonomy_term--legal_issues",
                        "id": "2e7b3842-d298-4935-b281-529ec2db2438"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/field_primary_legal_category?resourceVersion=id%3A2247241"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/relationships/field_primary_legal_category?resourceVersion=id%3A2247241"
                        }
                    }
                },
                "field_primary_prevention": {
                    "data": null,
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/field_primary_prevention?resourceVersion=id%3A2247241"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/relationships/field_primary_prevention?resourceVersion=id%3A2247241"
                        }
                    }
                },
                "field_related_problems": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/field_related_problems?resourceVersion=id%3A2247241"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/relationships/field_related_problems?resourceVersion=id%3A2247241"
                        }
                    }
                },
                "field_related_resources": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/field_related_resources?resourceVersion=id%3A2247241"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/relationships/field_related_resources?resourceVersion=id%3A2247241"
                        }
                    }
                },
                "field_secondary_prevention": {
                    "data": null,
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/field_secondary_prevention?resourceVersion=id%3A2247241"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6/relationships/field_secondary_prevention?resourceVersion=id%3A2247241"
                        }
                    }
                }
            }
        }
    ],
    "links": {
        "self": {
            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_problem"
        }
    }
  }





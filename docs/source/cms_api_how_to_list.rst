.. _legal-howto-list-api:

===========================
Content API:  How To List
===========================


Returns a list of how-to structured content. A solution identifier UUID may be included which will limit the results to those how-to's embedded in that solution.

Function call
===============

Method:  GET

URLS:

* https://www.illinoislegalaid.org/jsonapi/node/legal_how_to (English)
* https://www.illinoislegalaid.org/es/jsonapi/node/legal_how_to (Spanish)
* https://www.illinoislegalaid.org/pl/jsonapi/node/legal_how_to (Polish)

Parameters
=================
Any parameter supported by the JSONAPI is supported. See the :ref:`ilao-api-filters` for filter examples.


Sample response
=================

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
            "type": "node--legal_how_to",
            "id": "faba2f2c-bd13-4474-90a6-160d6605680e",
            "links": {
                "self": {
                    "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/faba2f2c-bd13-4474-90a6-160d6605680e?resourceVersion=id%3A2415496"
                }
            },
            "attributes": {
                "drupal_internal__nid": 166921,
                "drupal_internal__vid": 2415496,
                "langcode": "en",
                "revision_timestamp": "2021-05-12T14:57:11+00:00",
                "revision_log": "Title",
                "status": true,
                "title": "How to apply for unemployment benefits from IDES",
                "created": "2021-05-05T18:56:30+00:00",
                "changed": "2021-05-12T14:57:11+00:00",
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
                "field_content_description": "Explains how to apply for unemployment benefits if you have lost your job. Includes how to continue receiving them every two weeks.",
                "field_last_revised": "2021-05-05T13:56:30-05:00",
                "field_last_substantive_update": "2020-04-20T13:56:30-05:00",
                "field_legal_position": 0,
                "field_meta_description": "Explains how to apply for unemployment benefits if you have lost your job. Includes how to continue receiving them every two weeks.",
                "field_perform_time": "P30M",
                "field_prep_time": "P1H",
                "field_request_translation": "0",
                "field_supply": [],
                "field_text_tool": [],
                "field_total_time": "P1H30M",
                "field_translation_outdated": false,
                "field_yield": null
            },
            "relationships": {
                "node_type": {
                    "data": {
                        "type": "node_type--node_type",
                        "id": "dc161d17-965f-4fb8-830a-15640f00004d"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/faba2f2c-bd13-4474-90a6-160d6605680e/node_type?resourceVersion=id%3A2415496"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/faba2f2c-bd13-4474-90a6-160d6605680e/relationships/node_type?resourceVersion=id%3A2415496"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/faba2f2c-bd13-4474-90a6-160d6605680e/revision_uid?resourceVersion=id%3A2415496"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/faba2f2c-bd13-4474-90a6-160d6605680e/relationships/revision_uid?resourceVersion=id%3A2415496"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/faba2f2c-bd13-4474-90a6-160d6605680e/uid?resourceVersion=id%3A2415496"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/faba2f2c-bd13-4474-90a6-160d6605680e/relationships/uid?resourceVersion=id%3A2415496"
                        }
                    }
                },
                "field_annual_updates": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/faba2f2c-bd13-4474-90a6-160d6605680e/field_annual_updates?resourceVersion=id%3A2415496"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/faba2f2c-bd13-4474-90a6-160d6605680e/relationships/field_annual_updates?resourceVersion=id%3A2415496"
                        }
                    }
                },
                "field_content_management_tags": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/faba2f2c-bd13-4474-90a6-160d6605680e/field_content_management_tags?resourceVersion=id%3A2415496"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/faba2f2c-bd13-4474-90a6-160d6605680e/relationships/field_content_management_tags?resourceVersion=id%3A2415496"
                        }
                    }
                },
                "field_jurisdiction": {
                    "data": [
                        {
                            "type": "paragraph--coverage_area",
                            "id": "217f6909-dc4b-4c88-a4e5-014592d9f7d2",
                            "meta": {
                                "target_revision_id": 1417781
                            }
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/faba2f2c-bd13-4474-90a6-160d6605680e/field_jurisdiction?resourceVersion=id%3A2415496"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/faba2f2c-bd13-4474-90a6-160d6605680e/relationships/field_jurisdiction?resourceVersion=id%3A2415496"
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
                            "id": "afa23f49-7a9d-4caf-b9ac-63da005dc20a",
                            "meta": {
                                "arity": 0
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "dc2775b1-8496-4c61-aead-c1a7ba9c7057",
                            "meta": {
                                "arity": 0
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "746c32e5-7cab-48b6-94ac-3a84dbb16b56",
                            "meta": {
                                "arity": 0
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "afa23f49-7a9d-4caf-b9ac-63da005dc20a",
                            "meta": {
                                "arity": 1
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "dc2775b1-8496-4c61-aead-c1a7ba9c7057",
                            "meta": {
                                "arity": 1
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "746c32e5-7cab-48b6-94ac-3a84dbb16b56",
                            "meta": {
                                "arity": 1
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "afa23f49-7a9d-4caf-b9ac-63da005dc20a",
                            "meta": {
                                "arity": 2
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "dc2775b1-8496-4c61-aead-c1a7ba9c7057",
                            "meta": {
                                "arity": 2
                            }
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "746c32e5-7cab-48b6-94ac-3a84dbb16b56",
                            "meta": {
                                "arity": 2
                            }
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/faba2f2c-bd13-4474-90a6-160d6605680e/field_legal_issues?resourceVersion=id%3A2415496"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/faba2f2c-bd13-4474-90a6-160d6605680e/relationships/field_legal_issues?resourceVersion=id%3A2415496"
                        }
                    }
                },
                "field_primary_legal_category": {
                    "data": {
                        "type": "taxonomy_term--legal_issues",
                        "id": "39affc4e-e0e0-4091-addc-c049916dedfc"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/faba2f2c-bd13-4474-90a6-160d6605680e/field_primary_legal_category?resourceVersion=id%3A2415496"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/faba2f2c-bd13-4474-90a6-160d6605680e/relationships/field_primary_legal_category?resourceVersion=id%3A2415496"
                        }
                    }
                },
                "field_step_sections": {
                    "data": [
                        {
                            "type": "paragraph--legal_step_section",
                            "id": "df3c19cb-b27f-4a04-aa39-95616fd4c49a",
                            "meta": {
                                "target_revision_id": 1417786
                            }
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/faba2f2c-bd13-4474-90a6-160d6605680e/field_step_sections?resourceVersion=id%3A2415496"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/faba2f2c-bd13-4474-90a6-160d6605680e/relationships/field_step_sections?resourceVersion=id%3A2415496"
                        }
                    }
                },
                "field_subject_matter_expert": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/faba2f2c-bd13-4474-90a6-160d6605680e/field_subject_matter_expert?resourceVersion=id%3A2415496"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/faba2f2c-bd13-4474-90a6-160d6605680e/relationships/field_subject_matter_expert?resourceVersion=id%3A2415496"
                        }
                    }
                }
            }
        },
        {
            "type": "node--legal_how_to",
            "id": "8e2ee536-b9d2-4f1a-a58e-8ec72730a57f",
            "links": {
                "self": {
                    "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/8e2ee536-b9d2-4f1a-a58e-8ec72730a57f?resourceVersion=id%3A2415596"
                }
            },
            "attributes": {
                "drupal_internal__nid": 167031,
                "drupal_internal__vid": 2415596,
                "langcode": "en",
                "revision_timestamp": "2021-05-12T16:55:45+00:00",
                "revision_log": null,
                "status": true,
                "title": "How to appeal your unemployment benefits denial",
                "created": "2021-05-12T14:59:36+00:00",
                "changed": "2021-05-12T16:55:45+00:00",
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
                "field_content_description": "Explains how to appeal if your application for unemployment benefits has been denied. Describes the first stage which is appeal to a referee.",
                "field_last_revised": "2021-05-12T09:59:36-05:00",
                "field_last_substantive_update": "2021-05-12T09:59:36-05:00",
                "field_legal_position": 0,
                "field_meta_description": "Explains how to appeal if your application for unemployment benefits has been denied. Describes the first stage which is appeal to a referee.",
                "field_perform_time": "T2H",
                "field_prep_time": "T30M",
                "field_request_translation": "0",
                "field_supply": [],
                "field_text_tool": [],
                "field_total_time": "T2H30M",
                "field_translation_outdated": false,
                "field_yield": null
            },
            "relationships": {
                "node_type": {
                    "data": {
                        "type": "node_type--node_type",
                        "id": "dc161d17-965f-4fb8-830a-15640f00004d"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/8e2ee536-b9d2-4f1a-a58e-8ec72730a57f/node_type?resourceVersion=id%3A2415596"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/8e2ee536-b9d2-4f1a-a58e-8ec72730a57f/relationships/node_type?resourceVersion=id%3A2415596"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/8e2ee536-b9d2-4f1a-a58e-8ec72730a57f/revision_uid?resourceVersion=id%3A2415596"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/8e2ee536-b9d2-4f1a-a58e-8ec72730a57f/relationships/revision_uid?resourceVersion=id%3A2415596"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/8e2ee536-b9d2-4f1a-a58e-8ec72730a57f/uid?resourceVersion=id%3A2415596"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/8e2ee536-b9d2-4f1a-a58e-8ec72730a57f/relationships/uid?resourceVersion=id%3A2415596"
                        }
                    }
                },
                "field_annual_updates": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/8e2ee536-b9d2-4f1a-a58e-8ec72730a57f/field_annual_updates?resourceVersion=id%3A2415596"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/8e2ee536-b9d2-4f1a-a58e-8ec72730a57f/relationships/field_annual_updates?resourceVersion=id%3A2415596"
                        }
                    }
                },
                "field_content_management_tags": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/8e2ee536-b9d2-4f1a-a58e-8ec72730a57f/field_content_management_tags?resourceVersion=id%3A2415596"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/8e2ee536-b9d2-4f1a-a58e-8ec72730a57f/relationships/field_content_management_tags?resourceVersion=id%3A2415596"
                        }
                    }
                },
                "field_jurisdiction": {
                    "data": [
                        {
                            "type": "paragraph--coverage_area",
                            "id": "5c98c7a5-5d8b-416d-8f49-205c02cf9099",
                            "meta": {
                                "target_revision_id": 1418516
                            }
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/8e2ee536-b9d2-4f1a-a58e-8ec72730a57f/field_jurisdiction?resourceVersion=id%3A2415596"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/8e2ee536-b9d2-4f1a-a58e-8ec72730a57f/relationships/field_jurisdiction?resourceVersion=id%3A2415596"
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
                            "id": "4b215793-795c-417c-b695-af07a83488b9"
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/8e2ee536-b9d2-4f1a-a58e-8ec72730a57f/field_legal_issues?resourceVersion=id%3A2415596"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/8e2ee536-b9d2-4f1a-a58e-8ec72730a57f/relationships/field_legal_issues?resourceVersion=id%3A2415596"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/8e2ee536-b9d2-4f1a-a58e-8ec72730a57f/field_primary_legal_category?resourceVersion=id%3A2415596"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/8e2ee536-b9d2-4f1a-a58e-8ec72730a57f/relationships/field_primary_legal_category?resourceVersion=id%3A2415596"
                        }
                    }
                },
                "field_step_sections": {
                    "data": [
                        {
                            "type": "paragraph--legal_step_section",
                            "id": "506036d9-6b13-44d0-a16d-247e65c6e60f",
                            "meta": {
                                "target_revision_id": 1418521
                            }
                        },
                        {
                            "type": "paragraph--legal_step_section",
                            "id": "0870ed81-ba5d-4832-9fd5-cfeb8792e1b4",
                            "meta": {
                                "target_revision_id": 1418526
                            }
                        },
                        {
                            "type": "paragraph--legal_step_section",
                            "id": "c8d51dc5-c775-40f4-b38e-10687ba7555d",
                            "meta": {
                                "target_revision_id": 1418531
                            }
                        },
                        {
                            "type": "paragraph--legal_step_section",
                            "id": "6fd59ec6-57c0-4e8c-b96b-abed78f56525",
                            "meta": {
                                "target_revision_id": 1418536
                            }
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/8e2ee536-b9d2-4f1a-a58e-8ec72730a57f/field_step_sections?resourceVersion=id%3A2415596"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/8e2ee536-b9d2-4f1a-a58e-8ec72730a57f/relationships/field_step_sections?resourceVersion=id%3A2415596"
                        }
                    }
                },
                "field_subject_matter_expert": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/8e2ee536-b9d2-4f1a-a58e-8ec72730a57f/field_subject_matter_expert?resourceVersion=id%3A2415596"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to/8e2ee536-b9d2-4f1a-a58e-8ec72730a57f/relationships/field_subject_matter_expert?resourceVersion=id%3A2415596"
                        }
                    }
                }
            }
        }
    ],
    "links": {
        "self": {
            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_how_to?page%5Blimit%5D=5"
        }
    }
  }





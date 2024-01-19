==========================
Content API:  Legal Step
==========================

Returns one or more Legal Steps. The UUID of the specific Legal Step may be provided.

Function call
=================

Method: GET


If the /[uuid] is left off, all forms will be returned.  See parameters below.


URLs:

* https://www.illinoislegalaid.org/jsonapi/node/legal_step/[uuid] (English)
* https://www.illinoislegalaid.org/es/jsonapi/node/legal_step/[uuid] (Spanish)
* https://www.illinoislegalaid.org/pl/jsonapi/node/legal_step/[uuid] (Polish)

.. note:: For example: https://www.illinoislegalaid.org/jsonapi/node/legal_step/5e640607-35a5-4d8b-a2f9-d3b5e40710f0?resourceVersion=id%3A2358466" will return the "Prepare and gather information for unemployment application" step.


Sample response
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
            "type": "node--legal_step",
            "id": "5e640607-35a5-4d8b-a2f9-d3b5e40710f0",
            "links": {
                "self": {
                    "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/5e640607-35a5-4d8b-a2f9-d3b5e40710f0?resourceVersion=id%3A2358466"
                }
            },
            "attributes": {
                "drupal_internal__nid": 166886,
                "title": "Prepare and gather information for unemployment application",
                "drupal_internal__vid": 2358466,
                "langcode": "en",
                "revision_timestamp": "2021-05-05T19:27:58+00:00",
                "revision_log": null,
                "status": true,
                "created": "2021-05-05T18:57:54+00:00",
                "changed": "2021-05-05T19:27:58+00:00",
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
                "body": null,
                "field_content_description": null,
                "field_legal_position": 0,
                "field_meta_description": null,
                "field_request_translation": "0",
                "field_translation_outdated": false
            },
            "relationships": {
                "node_type": {
                    "data": {
                        "type": "node_type--node_type",
                        "id": "facbbaa1-fabf-43ca-9792-734a4682cbf0"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/5e640607-35a5-4d8b-a2f9-d3b5e40710f0/node_type?resourceVersion=id%3A2358466"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/5e640607-35a5-4d8b-a2f9-d3b5e40710f0/relationships/node_type?resourceVersion=id%3A2358466"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/5e640607-35a5-4d8b-a2f9-d3b5e40710f0/revision_uid?resourceVersion=id%3A2358466"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/5e640607-35a5-4d8b-a2f9-d3b5e40710f0/relationships/revision_uid?resourceVersion=id%3A2358466"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/5e640607-35a5-4d8b-a2f9-d3b5e40710f0/uid?resourceVersion=id%3A2358466"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/5e640607-35a5-4d8b-a2f9-d3b5e40710f0/relationships/uid?resourceVersion=id%3A2358466"
                        }
                    }
                },
                "field_annual_updates": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/5e640607-35a5-4d8b-a2f9-d3b5e40710f0/field_annual_updates?resourceVersion=id%3A2358466"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/5e640607-35a5-4d8b-a2f9-d3b5e40710f0/relationships/field_annual_updates?resourceVersion=id%3A2358466"
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
                            "id": "2e7b3842-d298-4935-b281-529ec2db2438"
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
                            "id": "d5934598-03f4-4c8d-b705-85a3da6822b9"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/5e640607-35a5-4d8b-a2f9-d3b5e40710f0/field_legal_issues?resourceVersion=id%3A2358466"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/5e640607-35a5-4d8b-a2f9-d3b5e40710f0/relationships/field_legal_issues?resourceVersion=id%3A2358466"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/5e640607-35a5-4d8b-a2f9-d3b5e40710f0/field_primary_legal_category?resourceVersion=id%3A2358466"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/5e640607-35a5-4d8b-a2f9-d3b5e40710f0/relationships/field_primary_legal_category?resourceVersion=id%3A2358466"
                        }
                    }
                },
                "field_step_information": {
                    "data": [
                        {
                            "type": "paragraph--step_information",
                            "id": "980d29a7-cc68-48d5-a2a5-f11d0153e936",
                            "meta": {
                                "target_revision_id": 1416716
                            }
                        },
                        {
                            "type": "paragraph--step_information",
                            "id": "5641195b-0e27-4ff3-8a65-b7bc5ac64657",
                            "meta": {
                                "target_revision_id": 1416726
                            }
                        },
                        {
                            "type": "paragraph--step_information",
                            "id": "3e3a5354-e631-43e5-8289-457bb1a6917f",
                            "meta": {
                                "target_revision_id": 1416736
                            }
                        },
                        {
                            "type": "paragraph--step_information",
                            "id": "620ebaa3-5b8d-43ad-9a40-fa2630259274",
                            "meta": {
                                "target_revision_id": 1416746
                            }
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/5e640607-35a5-4d8b-a2f9-d3b5e40710f0/field_step_information?resourceVersion=id%3A2358466"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/5e640607-35a5-4d8b-a2f9-d3b5e40710f0/relationships/field_step_information?resourceVersion=id%3A2358466"
                        }
                    }
                },
                "field_subject_matter_expert": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/5e640607-35a5-4d8b-a2f9-d3b5e40710f0/field_subject_matter_expert?resourceVersion=id%3A2358466"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/5e640607-35a5-4d8b-a2f9-d3b5e40710f0/relationships/field_subject_matter_expert?resourceVersion=id%3A2358466"
                        }
                    }
                }
            }
        },
        {
            "type": "node--legal_step",
            "id": "b741a4d5-f4c5-4370-83d1-b76f6a2f6938",
            "links": {
                "self": {
                    "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/b741a4d5-f4c5-4370-83d1-b76f6a2f6938?resourceVersion=id%3A2358481"
                }
            },
            "attributes": {
                "drupal_internal__nid": 166896,
                "title": "Fill out and submit your unemployment application",
                "drupal_internal__vid": 2358481,
                "langcode": "en",
                "revision_timestamp": "2021-05-05T19:34:08+00:00",
                "revision_log": null,
                "status": true,
                "created": "2021-05-05T19:28:21+00:00",
                "changed": "2021-05-05T19:34:08+00:00",
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
                "body": null,
                "field_content_description": null,
                "field_legal_position": null,
                "field_meta_description": null,
                "field_request_translation": null,
                "field_translation_outdated": false
            },
            "relationships": {
                "node_type": {
                    "data": {
                        "type": "node_type--node_type",
                        "id": "facbbaa1-fabf-43ca-9792-734a4682cbf0"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/b741a4d5-f4c5-4370-83d1-b76f6a2f6938/node_type?resourceVersion=id%3A2358481"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/b741a4d5-f4c5-4370-83d1-b76f6a2f6938/relationships/node_type?resourceVersion=id%3A2358481"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/b741a4d5-f4c5-4370-83d1-b76f6a2f6938/revision_uid?resourceVersion=id%3A2358481"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/b741a4d5-f4c5-4370-83d1-b76f6a2f6938/relationships/revision_uid?resourceVersion=id%3A2358481"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/b741a4d5-f4c5-4370-83d1-b76f6a2f6938/uid?resourceVersion=id%3A2358481"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/b741a4d5-f4c5-4370-83d1-b76f6a2f6938/relationships/uid?resourceVersion=id%3A2358481"
                        }
                    }
                },
                "field_annual_updates": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/b741a4d5-f4c5-4370-83d1-b76f6a2f6938/field_annual_updates?resourceVersion=id%3A2358481"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/b741a4d5-f4c5-4370-83d1-b76f6a2f6938/relationships/field_annual_updates?resourceVersion=id%3A2358481"
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
                            "id": "746c32e5-7cab-48b6-94ac-3a84dbb16b56"
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/b741a4d5-f4c5-4370-83d1-b76f6a2f6938/field_legal_issues?resourceVersion=id%3A2358481"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/b741a4d5-f4c5-4370-83d1-b76f6a2f6938/relationships/field_legal_issues?resourceVersion=id%3A2358481"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/b741a4d5-f4c5-4370-83d1-b76f6a2f6938/field_primary_legal_category?resourceVersion=id%3A2358481"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/b741a4d5-f4c5-4370-83d1-b76f6a2f6938/relationships/field_primary_legal_category?resourceVersion=id%3A2358481"
                        }
                    }
                },
                "field_step_information": {
                    "data": [
                        {
                            "type": "paragraph--step_information",
                            "id": "4309a2b9-0e16-463f-b8ca-177ca62e7e21",
                            "meta": {
                                "target_revision_id": 1416756
                            }
                        },
                        {
                            "type": "paragraph--step_information",
                            "id": "429beebd-d7e9-4880-943e-8d2d6dc17f2b",
                            "meta": {
                                "target_revision_id": 1416766
                            }
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/b741a4d5-f4c5-4370-83d1-b76f6a2f6938/field_step_information?resourceVersion=id%3A2358481"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/b741a4d5-f4c5-4370-83d1-b76f6a2f6938/relationships/field_step_information?resourceVersion=id%3A2358481"
                        }
                    }
                },
                "field_subject_matter_expert": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/b741a4d5-f4c5-4370-83d1-b76f6a2f6938/field_subject_matter_expert?resourceVersion=id%3A2358481"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/b741a4d5-f4c5-4370-83d1-b76f6a2f6938/relationships/field_subject_matter_expert?resourceVersion=id%3A2358481"
                        }
                    }
                }
            }
        },
        {
            "type": "node--legal_step",
            "id": "513e366f-abce-43c6-9cdc-e59e9c12b0cf",
            "links": {
                "self": {
                    "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/513e366f-abce-43c6-9cdc-e59e9c12b0cf?resourceVersion=id%3A2358501"
                }
            },
            "attributes": {
                "drupal_internal__nid": 166901,
                "title": "Wait for a response from IDES",
                "drupal_internal__vid": 2358501,
                "langcode": "en",
                "revision_timestamp": "2021-05-05T19:46:44+00:00",
                "revision_log": null,
                "status": true,
                "created": "2021-05-05T19:41:03+00:00",
                "changed": "2021-05-05T19:46:44+00:00",
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
                "body": null,
                "field_content_description": null,
                "field_legal_position": 0,
                "field_meta_description": null,
                "field_request_translation": null,
                "field_translation_outdated": false
            },
            "relationships": {
                "node_type": {
                    "data": {
                        "type": "node_type--node_type",
                        "id": "facbbaa1-fabf-43ca-9792-734a4682cbf0"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/513e366f-abce-43c6-9cdc-e59e9c12b0cf/node_type?resourceVersion=id%3A2358501"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/513e366f-abce-43c6-9cdc-e59e9c12b0cf/relationships/node_type?resourceVersion=id%3A2358501"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/513e366f-abce-43c6-9cdc-e59e9c12b0cf/revision_uid?resourceVersion=id%3A2358501"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/513e366f-abce-43c6-9cdc-e59e9c12b0cf/relationships/revision_uid?resourceVersion=id%3A2358501"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/513e366f-abce-43c6-9cdc-e59e9c12b0cf/uid?resourceVersion=id%3A2358501"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/513e366f-abce-43c6-9cdc-e59e9c12b0cf/relationships/uid?resourceVersion=id%3A2358501"
                        }
                    }
                },
                "field_annual_updates": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/513e366f-abce-43c6-9cdc-e59e9c12b0cf/field_annual_updates?resourceVersion=id%3A2358501"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/513e366f-abce-43c6-9cdc-e59e9c12b0cf/relationships/field_annual_updates?resourceVersion=id%3A2358501"
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
                            "id": "746c32e5-7cab-48b6-94ac-3a84dbb16b56"
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/513e366f-abce-43c6-9cdc-e59e9c12b0cf/field_legal_issues?resourceVersion=id%3A2358501"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/513e366f-abce-43c6-9cdc-e59e9c12b0cf/relationships/field_legal_issues?resourceVersion=id%3A2358501"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/513e366f-abce-43c6-9cdc-e59e9c12b0cf/field_primary_legal_category?resourceVersion=id%3A2358501"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/513e366f-abce-43c6-9cdc-e59e9c12b0cf/relationships/field_primary_legal_category?resourceVersion=id%3A2358501"
                        }
                    }
                },
                "field_step_information": {
                    "data": [
                        {
                            "type": "paragraph--step_information",
                            "id": "60a0180a-4e15-4259-bdca-5dcf8915d5d8",
                            "meta": {
                                "target_revision_id": 1416776
                            }
                        },
                        {
                            "type": "paragraph--step_information",
                            "id": "9001b053-94ab-48ce-baf0-f53de5235008",
                            "meta": {
                                "target_revision_id": 1416786
                            }
                        },
                        {
                            "type": "paragraph--step_information",
                            "id": "190caf5b-d4fd-48c9-987b-5a4088a300c6",
                            "meta": {
                                "target_revision_id": 1416796
                            }
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/513e366f-abce-43c6-9cdc-e59e9c12b0cf/field_step_information?resourceVersion=id%3A2358501"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/513e366f-abce-43c6-9cdc-e59e9c12b0cf/relationships/field_step_information?resourceVersion=id%3A2358501"
                        }
                    }
                },
                "field_subject_matter_expert": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/513e366f-abce-43c6-9cdc-e59e9c12b0cf/field_subject_matter_expert?resourceVersion=id%3A2358501"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/513e366f-abce-43c6-9cdc-e59e9c12b0cf/relationships/field_subject_matter_expert?resourceVersion=id%3A2358501"
                        }
                    }
                }
            }
        },
        {
            "type": "node--legal_step",
            "id": "e3c26aee-3641-4015-8499-1a6b52345c44",
            "links": {
                "self": {
                    "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/e3c26aee-3641-4015-8499-1a6b52345c44?resourceVersion=id%3A2358506"
                }
            },
            "attributes": {
                "drupal_internal__nid": 166906,
                "title": "Certify your unemployment online or by phone",
                "drupal_internal__vid": 2358506,
                "langcode": "en",
                "revision_timestamp": "2021-05-05T19:58:08+00:00",
                "revision_log": null,
                "status": true,
                "created": "2021-05-05T19:46:54+00:00",
                "changed": "2021-05-05T19:58:08+00:00",
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
                "body": null,
                "field_content_description": null,
                "field_legal_position": 0,
                "field_meta_description": null,
                "field_request_translation": null,
                "field_translation_outdated": false
            },
            "relationships": {
                "node_type": {
                    "data": {
                        "type": "node_type--node_type",
                        "id": "facbbaa1-fabf-43ca-9792-734a4682cbf0"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/e3c26aee-3641-4015-8499-1a6b52345c44/node_type?resourceVersion=id%3A2358506"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/e3c26aee-3641-4015-8499-1a6b52345c44/relationships/node_type?resourceVersion=id%3A2358506"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/e3c26aee-3641-4015-8499-1a6b52345c44/revision_uid?resourceVersion=id%3A2358506"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/e3c26aee-3641-4015-8499-1a6b52345c44/relationships/revision_uid?resourceVersion=id%3A2358506"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/e3c26aee-3641-4015-8499-1a6b52345c44/uid?resourceVersion=id%3A2358506"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/e3c26aee-3641-4015-8499-1a6b52345c44/relationships/uid?resourceVersion=id%3A2358506"
                        }
                    }
                },
                "field_annual_updates": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/e3c26aee-3641-4015-8499-1a6b52345c44/field_annual_updates?resourceVersion=id%3A2358506"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/e3c26aee-3641-4015-8499-1a6b52345c44/relationships/field_annual_updates?resourceVersion=id%3A2358506"
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
                            "id": "746c32e5-7cab-48b6-94ac-3a84dbb16b56"
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/e3c26aee-3641-4015-8499-1a6b52345c44/field_legal_issues?resourceVersion=id%3A2358506"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/e3c26aee-3641-4015-8499-1a6b52345c44/relationships/field_legal_issues?resourceVersion=id%3A2358506"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/e3c26aee-3641-4015-8499-1a6b52345c44/field_primary_legal_category?resourceVersion=id%3A2358506"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/e3c26aee-3641-4015-8499-1a6b52345c44/relationships/field_primary_legal_category?resourceVersion=id%3A2358506"
                        }
                    }
                },
                "field_step_information": {
                    "data": [
                        {
                            "type": "paragraph--step_information",
                            "id": "80bc6931-ca83-4a67-8348-b5a07b257a5f",
                            "meta": {
                                "target_revision_id": 1416806
                            }
                        },
                        {
                            "type": "paragraph--step_information",
                            "id": "d83ef54d-6abb-4261-be54-30a5b1029f7e",
                            "meta": {
                                "target_revision_id": 1416816
                            }
                        },
                        {
                            "type": "paragraph--step_information",
                            "id": "09bf220f-2f46-4777-805a-20cb89b79494",
                            "meta": {
                                "target_revision_id": 1416826
                            }
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/e3c26aee-3641-4015-8499-1a6b52345c44/field_step_information?resourceVersion=id%3A2358506"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/e3c26aee-3641-4015-8499-1a6b52345c44/relationships/field_step_information?resourceVersion=id%3A2358506"
                        }
                    }
                },
                "field_subject_matter_expert": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/e3c26aee-3641-4015-8499-1a6b52345c44/field_subject_matter_expert?resourceVersion=id%3A2358506"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/e3c26aee-3641-4015-8499-1a6b52345c44/relationships/field_subject_matter_expert?resourceVersion=id%3A2358506"
                        }
                    }
                }
            }
        },
        {
            "type": "node--legal_step",
            "id": "563ae0c8-b643-4434-bb08-4e308886c021",
            "links": {
                "self": {
                    "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/563ae0c8-b643-4434-bb08-4e308886c021?resourceVersion=id%3A2358511"
                }
            },
            "attributes": {
                "drupal_internal__nid": 166911,
                "title": "Consider appealing if you are denied unemployment benefits",
                "drupal_internal__vid": 2358511,
                "langcode": "en",
                "revision_timestamp": "2021-05-05T20:04:29+00:00",
                "revision_log": null,
                "status": true,
                "created": "2021-05-05T20:01:43+00:00",
                "changed": "2021-05-05T20:04:29+00:00",
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
                "body": null,
                "field_content_description": null,
                "field_legal_position": 0,
                "field_meta_description": null,
                "field_request_translation": null,
                "field_translation_outdated": false
            },
            "relationships": {
                "node_type": {
                    "data": {
                        "type": "node_type--node_type",
                        "id": "facbbaa1-fabf-43ca-9792-734a4682cbf0"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/563ae0c8-b643-4434-bb08-4e308886c021/node_type?resourceVersion=id%3A2358511"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/563ae0c8-b643-4434-bb08-4e308886c021/relationships/node_type?resourceVersion=id%3A2358511"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/563ae0c8-b643-4434-bb08-4e308886c021/revision_uid?resourceVersion=id%3A2358511"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/563ae0c8-b643-4434-bb08-4e308886c021/relationships/revision_uid?resourceVersion=id%3A2358511"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/563ae0c8-b643-4434-bb08-4e308886c021/uid?resourceVersion=id%3A2358511"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/563ae0c8-b643-4434-bb08-4e308886c021/relationships/uid?resourceVersion=id%3A2358511"
                        }
                    }
                },
                "field_annual_updates": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/563ae0c8-b643-4434-bb08-4e308886c021/field_annual_updates?resourceVersion=id%3A2358511"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/563ae0c8-b643-4434-bb08-4e308886c021/relationships/field_annual_updates?resourceVersion=id%3A2358511"
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
                            "id": "746c32e5-7cab-48b6-94ac-3a84dbb16b56"
                        },
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "4b215793-795c-417c-b695-af07a83488b9"
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/563ae0c8-b643-4434-bb08-4e308886c021/field_legal_issues?resourceVersion=id%3A2358511"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/563ae0c8-b643-4434-bb08-4e308886c021/relationships/field_legal_issues?resourceVersion=id%3A2358511"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/563ae0c8-b643-4434-bb08-4e308886c021/field_primary_legal_category?resourceVersion=id%3A2358511"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/563ae0c8-b643-4434-bb08-4e308886c021/relationships/field_primary_legal_category?resourceVersion=id%3A2358511"
                        }
                    }
                },
                "field_step_information": {
                    "data": [
                        {
                            "type": "paragraph--step_information",
                            "id": "f407fc4d-a8cc-4a1e-9b99-f98bf7550464",
                            "meta": {
                                "target_revision_id": 1416836
                            }
                        },
                        {
                            "type": "paragraph--step_information",
                            "id": "9a936446-1d64-4482-8304-7f6afab8fdc3",
                            "meta": {
                                "target_revision_id": 1416846
                            }
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/563ae0c8-b643-4434-bb08-4e308886c021/field_step_information?resourceVersion=id%3A2358511"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/563ae0c8-b643-4434-bb08-4e308886c021/relationships/field_step_information?resourceVersion=id%3A2358511"
                        }
                    }
                },
                "field_subject_matter_expert": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/563ae0c8-b643-4434-bb08-4e308886c021/field_subject_matter_expert?resourceVersion=id%3A2358511"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step/563ae0c8-b643-4434-bb08-4e308886c021/relationships/field_subject_matter_expert?resourceVersion=id%3A2358511"
                        }
                    }
                }
            }
        }
    ],
    "links": {
        "next": {
            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step?page%5Boffset%5D=5&page%5Blimit%5D=5"
        },
        "self": {
            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_step?page%5Blimit%5D=5"
        }
    }
  }

Parameters
=============

Parameters supported by the JSONAPI are allowed. See the :ref:`ilao-api-filters` for filter examples.



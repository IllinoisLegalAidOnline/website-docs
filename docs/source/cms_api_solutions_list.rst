.. _legal-solution-list-api:

==============================
Content API:  Solutions List
==============================


Returns a list of solutions along with nested information on the problem(s) the solution solves.

Function call
==================

Method: GET

URLs:

* https://www.illinoislegalaid.org/jsonapi/node/legal_solution (English)
* https://www.illinoislegalaid.org/es/jsonapi/node/legal_solution (Spanish)
* https://www.illinoislegalaid.org/pl/jsonapi/node/legal_solution (Polish)



Parameters
===============
All parameters are optional.  Any parameter supported by the JSONAPI is supported. See the :ref:`ilao-api-filters` for filter examples.


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
            "type": "node--legal_solution",
            "id": "608b2d24-b283-46ec-a8e0-4fb2ec920b2d",
            "links": {
                "self": {
                    "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d?resourceVersion=id%3A2247236"
                }
            },
            "attributes": {
                "drupal_internal__nid": 166806,
                "drupal_internal__vid": 2247236,
                "langcode": "en",
                "revision_timestamp": "2021-04-21T16:58:57+00:00",
                "revision_log": null,
                "status": false,
                "title": "Apply for unemployment insurance (UI) benefits",
                "created": "2021-04-21T14:14:04+00:00",
                "changed": "2021-04-21T16:58:57+00:00",
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
                "field_alternate_name": null,
                "field_content_description": "Unemployment insurance (UI) can help you replace income from a lost job. It is run by the Illinois Department of Economic Security (IDES). ",
                "field_disambiguation_description": null,
                "field_estimated_time_required": null,
                "field_information_needed": [],
                "field_legal_difficulty": null,
                "field_legal_position": 0,
                "field_meta_description": "Unemployment insurance (UI) can help you replace income from a lost job. It is run by the Illinois Department of Economic Security (IDES). ",
                "field_request_translation": "0",
                "field_translation_outdated": false
            },
            "relationships": {
                "node_type": {
                    "data": {
                        "type": "node_type--node_type",
                        "id": "a3c872a1-5c93-4b3c-80e7-3e82ad17cc38"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/node_type?resourceVersion=id%3A2247236"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/relationships/node_type?resourceVersion=id%3A2247236"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/revision_uid?resourceVersion=id%3A2247236"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/relationships/revision_uid?resourceVersion=id%3A2247236"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/uid?resourceVersion=id%3A2247236"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/relationships/uid?resourceVersion=id%3A2247236"
                        }
                    }
                },
                "field_citation": {
                    "data": [
                        {
                            "type": "paragraph--citation",
                            "id": "c4618314-d7bf-473b-9bda-1845efb11f96",
                            "meta": {
                                "target_revision_id": 1415786
                            }
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/field_citation?resourceVersion=id%3A2247236"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/relationships/field_citation?resourceVersion=id%3A2247236"
                        }
                    }
                },
                "field_content_management_tags": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/field_content_management_tags?resourceVersion=id%3A2247236"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/relationships/field_content_management_tags?resourceVersion=id%3A2247236"
                        }
                    }
                },
                "field_eligibility_rules": {
                    "data": [
                        {
                            "type": "paragraph--structured_text_block",
                            "id": "24adbe9d-d8e4-4654-a247-d8b47c40acca",
                            "meta": {
                                "target_revision_id": 1415816
                            }
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/field_eligibility_rules?resourceVersion=id%3A2247236"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/relationships/field_eligibility_rules?resourceVersion=id%3A2247236"
                        }
                    }
                },
                "field_helpful_organizations": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/field_helpful_organizations?resourceVersion=id%3A2247236"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/relationships/field_helpful_organizations?resourceVersion=id%3A2247236"
                        }
                    }
                },
                "field_howtos": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/field_howtos?resourceVersion=id%3A2247236"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/relationships/field_howtos?resourceVersion=id%3A2247236"
                        }
                    }
                },
                "field_jurisdiction": {
                    "data": [
                        {
                            "type": "paragraph--coverage_area",
                            "id": "08831234-84d7-4509-9e34-7e0f959b8b47",
                            "meta": {
                                "target_revision_id": 1415821
                            }
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/field_jurisdiction?resourceVersion=id%3A2247236"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/relationships/field_jurisdiction?resourceVersion=id%3A2247236"
                        }
                    }
                },
                "field_legal_forms_needed": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/field_legal_forms_needed?resourceVersion=id%3A2247236"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/relationships/field_legal_forms_needed?resourceVersion=id%3A2247236"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/field_legal_issues?resourceVersion=id%3A2247236"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/relationships/field_legal_issues?resourceVersion=id%3A2247236"
                        }
                    }
                },
                "field_legal_organizations": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/field_legal_organizations?resourceVersion=id%3A2247236"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/relationships/field_legal_organizations?resourceVersion=id%3A2247236"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/field_primary_legal_category?resourceVersion=id%3A2247236"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/relationships/field_primary_legal_category?resourceVersion=id%3A2247236"
                        }
                    }
                },
                "field_result": {
                    "data": {
                        "type": "paragraph--structured_text_block",
                        "id": "703f57aa-2637-4232-9222-ea9ccb7005ab",
                        "meta": {
                            "target_revision_id": 1415841
                        }
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/field_result?resourceVersion=id%3A2247236"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/relationships/field_result?resourceVersion=id%3A2247236"
                        }
                    }
                },
                "field_solution_type": {
                    "data": {
                        "type": "taxonomy_term--solution_types",
                        "id": "dd9a8def-d20b-42ee-b82b-cf27c98d2fa1"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/field_solution_type?resourceVersion=id%3A2247236"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d/relationships/field_solution_type?resourceVersion=id%3A2247236"
                        }
                    }
                }
            }
        }
    ],
    "links": {
        "self": {
            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_solution?page%5Blimit%5D=5"
        }
    }
  }


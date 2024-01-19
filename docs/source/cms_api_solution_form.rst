=================================
Content API:  Legal Form
=================================

Returns one or more legal forms.  These are usually included within a solution.

Function call
==============

Method: GET

If the /[uuid] is left off, all forms will be returned.  See parameters below.


URLs:

* https://www.illinoislegalaid.org/jsonapi/node/legal_forms/[uuid] (English)
* https://www.illinoislegalaid.org/es/jsonapi/node/legal_forms/[uuid] (Spanish)
* https://www.illinoislegalaid.org/pl/jsonapi/node/legal_forms[uuid] (Polish)

.. note:: For example:  https://www.illinoislegalaid.org/jsonapi/node/legal_forms/4695292d-0291-4625-94bb-d08ad3aea2c5 will return the LegalForm "Unemployment Notice of Appeal - Board of Review."

Sample response
===================

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
            "type": "node--legal_forms",
            "id": "4695292d-0291-4625-94bb-d08ad3aea2c5",
            "links": {
                "self": {
                    "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_forms/4695292d-0291-4625-94bb-d08ad3aea2c5?resourceVersion=id%3A2465071"
                }
            },
            "attributes": {
                "drupal_internal__nid": 167056,
                "drupal_internal__vid": 2465071,
                "langcode": "en",
                "revision_timestamp": "2021-05-18T14:59:42+00:00",
                "revision_log": null,
                "status": true,
                "title": "Unemployment Notice of Appeal - Board of Review",
                "created": "2021-05-18T14:47:35+00:00",
                "changed": "2021-05-18T14:59:42+00:00",
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
                "field_content_description": "Use this form to file a second appeal of your unemployment benefits denial. This happens after your first appeal is denied by a referee.",
                "field_form_use": null,
                "field_last_revised": "2020-05-24T09:47:35-05:00",
                "field_last_substantive_update": null,
                "field_legal_position": 1,
                "field_meta_description": "Use this form to file a second appeal of your unemployment benefits denial. This happens after your first appeal is denied by a referee.",
                "field_request_translation": "0",
                "field_translation_outdated": false
            },
            "relationships": {
                "node_type": {
                    "data": {
                        "type": "node_type--node_type",
                        "id": "d8f3695d-943c-4945-8eec-e63fdbb8bc44"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_forms/4695292d-0291-4625-94bb-d08ad3aea2c5/node_type?resourceVersion=id%3A2465071"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_forms/4695292d-0291-4625-94bb-d08ad3aea2c5/relationships/node_type?resourceVersion=id%3A2465071"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_forms/4695292d-0291-4625-94bb-d08ad3aea2c5/revision_uid?resourceVersion=id%3A2465071"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_forms/4695292d-0291-4625-94bb-d08ad3aea2c5/relationships/revision_uid?resourceVersion=id%3A2465071"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_forms/4695292d-0291-4625-94bb-d08ad3aea2c5/uid?resourceVersion=id%3A2465071"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_forms/4695292d-0291-4625-94bb-d08ad3aea2c5/relationships/uid?resourceVersion=id%3A2465071"
                        }
                    }
                },
                "field_content_management_tags": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_forms/4695292d-0291-4625-94bb-d08ad3aea2c5/field_content_management_tags?resourceVersion=id%3A2465071"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_forms/4695292d-0291-4625-94bb-d08ad3aea2c5/relationships/field_content_management_tags?resourceVersion=id%3A2465071"
                        }
                    }
                },
                "field_forms_can_be_generated_by": {
                    "data": [
                        {
                            "type": "paragraph--form_prep_program",
                            "id": "942787a5-d5b0-4b28-bc6d-d0740aca2a75",
                            "meta": {
                                "target_revision_id": 1418756
                            }
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_forms/4695292d-0291-4625-94bb-d08ad3aea2c5/field_forms_can_be_generated_by?resourceVersion=id%3A2465071"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_forms/4695292d-0291-4625-94bb-d08ad3aea2c5/relationships/field_forms_can_be_generated_by?resourceVersion=id%3A2465071"
                        }
                    }
                },
                "field_jurisdiction": {
                    "data": [
                        {
                            "type": "paragraph--coverage_area",
                            "id": "1b464155-1f4b-43fe-8860-1088d5028a42",
                            "meta": {
                                "target_revision_id": 1418761
                            }
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_forms/4695292d-0291-4625-94bb-d08ad3aea2c5/field_jurisdiction?resourceVersion=id%3A2465071"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_forms/4695292d-0291-4625-94bb-d08ad3aea2c5/relationships/field_jurisdiction?resourceVersion=id%3A2465071"
                        }
                    }
                },
                "field_legal_issues": {
                    "data": [
                        {
                            "type": "taxonomy_term--legal_issues",
                            "id": "2e7b3842-d298-4935-b281-529ec2db2438"
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
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_forms/4695292d-0291-4625-94bb-d08ad3aea2c5/field_legal_issues?resourceVersion=id%3A2465071"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_forms/4695292d-0291-4625-94bb-d08ad3aea2c5/relationships/field_legal_issues?resourceVersion=id%3A2465071"
                        }
                    }
                },
                "field_primary_category": {
                    "data": {
                        "type": "taxonomy_term--legal_issues",
                        "id": "2e7b3842-d298-4935-b281-529ec2db2438"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_forms/4695292d-0291-4625-94bb-d08ad3aea2c5/field_primary_category?resourceVersion=id%3A2465071"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_forms/4695292d-0291-4625-94bb-d08ad3aea2c5/relationships/field_primary_category?resourceVersion=id%3A2465071"
                        }
                    }
                }
            }
        }
    ],
    "links": {
        "self": {
            "href": "https://www.illinoislegalaid.org/jsonapi/node/legal_forms?page%5Blimit%5D=1"
        }
    }
  }

Parameters
==============
Parameters supported by the JSONAPI are allowed. See the :ref:`ilao-api-filters` for filter examples.




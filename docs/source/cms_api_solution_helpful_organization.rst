==================================================
Content API: Legal Solution Helpful Organization
==================================================


Returns helpful organization content.  When the uuid is provided, returns the specific organization.

.. note:: Helpful organization content is different from the OTIS organization/location/location-services content.  Helpful organizations are organizations attached to specific legal problem content that are not legal organizations.

Function call
================

Method: GET


If the /[uuid] is left off, all forms will be returned.  See parameters below.


URLs:

* https://www.illinoislegalaid.org/jsonapi/node/legal_step/[uuid] (English)
* https://www.illinoislegalaid.org/es/jsonapi/node/legal_step/[uuid] (Spanish)
* https://www.illinoislegalaid.org/pl/jsonapi/node/legal_step/[uuid] (Polish)

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
            "type": "node--helpful_organization",
            "id": "a7071ee6-9eb9-4001-961a-a9b060af3fe2",
            "links": {
                "self": {
                    "href": "https://www.illinoislegalaid.org/jsonapi/node/helpful_organization/a7071ee6-9eb9-4001-961a-a9b060af3fe2?resourceVersion=id%3A2644036"
                }
            },
            "attributes": {
                "drupal_internal__nid": 167456,
                "drupal_internal__vid": 2644036,
                "langcode": "en",
                "revision_timestamp": "2021-06-09T12:38:29+00:00",
                "revision_log": null,
                "status": true,
                "title": "Test Helpful Org",
                "created": "2021-06-09T12:33:11+00:00",
                "changed": "2021-06-09T12:38:29+00:00",
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
                "field_address": {
                    "langcode": "",
                    "country_code": "US",
                    "administrative_area": "IL",
                    "locality": "Chicago",
                    "dependent_locality": null,
                    "postal_code": "60603",
                    "sorting_code": null,
                    "address_line1": "120 S LaSalle Street",
                    "address_line2": "",
                    "organization": null,
                    "given_name": null,
                    "additional_name": null,
                    "family_name": null
                },
                "field_content_description": "Content description",
                "field_h_o_email": "info@illinoislegalaid.org",
                "field_meta_description": "Meta description",
                "field_request_translation": "0",
                "field_telephone": "555-555-5555",
                "field_translation_outdated": false
            },
            "relationships": {
                "node_type": {
                    "data": {
                        "type": "node_type--node_type",
                        "id": "8b1e2e3e-5e47-484c-a208-dfb063b8a380"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/helpful_organization/a7071ee6-9eb9-4001-961a-a9b060af3fe2/node_type?resourceVersion=id%3A2644036"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/helpful_organization/a7071ee6-9eb9-4001-961a-a9b060af3fe2/relationships/node_type?resourceVersion=id%3A2644036"
                        }
                    }
                },
                "revision_uid": {
                    "data": {
                        "type": "user--user",
                        "id": "968d01db-d9d4-41d8-845c-da3d8a8ac18e"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/helpful_organization/a7071ee6-9eb9-4001-961a-a9b060af3fe2/revision_uid?resourceVersion=id%3A2644036"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/helpful_organization/a7071ee6-9eb9-4001-961a-a9b060af3fe2/relationships/revision_uid?resourceVersion=id%3A2644036"
                        }
                    }
                },
                "uid": {
                    "data": {
                        "type": "user--user",
                        "id": "968d01db-d9d4-41d8-845c-da3d8a8ac18e"
                    },
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/helpful_organization/a7071ee6-9eb9-4001-961a-a9b060af3fe2/uid?resourceVersion=id%3A2644036"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/helpful_organization/a7071ee6-9eb9-4001-961a-a9b060af3fe2/relationships/uid?resourceVersion=id%3A2644036"
                        }
                    }
                },
                "field_area_served": {
                    "data": [
                        {
                            "type": "paragraph--coverage_area",
                            "id": "68b6eb1a-8d77-4cc0-936e-8e11a79f7929",
                            "meta": {
                                "target_revision_id": 1429781
                            }
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/helpful_organization/a7071ee6-9eb9-4001-961a-a9b060af3fe2/field_area_served?resourceVersion=id%3A2644036"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/helpful_organization/a7071ee6-9eb9-4001-961a-a9b060af3fe2/relationships/field_area_served?resourceVersion=id%3A2644036"
                        }
                    }
                },
                "field_contact": {
                    "data": [
                        {
                            "type": "paragraph--contact_point",
                            "id": "680c1835-a929-461f-97df-61aeea27c326",
                            "meta": {
                                "target_revision_id": 1429791
                            }
                        }
                    ],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/helpful_organization/a7071ee6-9eb9-4001-961a-a9b060af3fe2/field_contact?resourceVersion=id%3A2644036"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/helpful_organization/a7071ee6-9eb9-4001-961a-a9b060af3fe2/relationships/field_contact?resourceVersion=id%3A2644036"
                        }
                    }
                },
                "field_content_management_tags": {
                    "data": [],
                    "links": {
                        "related": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/helpful_organization/a7071ee6-9eb9-4001-961a-a9b060af3fe2/field_content_management_tags?resourceVersion=id%3A2644036"
                        },
                        "self": {
                            "href": "https://www.illinoislegalaid.org/jsonapi/node/helpful_organization/a7071ee6-9eb9-4001-961a-a9b060af3fe2/relationships/field_content_management_tags?resourceVersion=id%3A2644036"
                        }
                    }
                }
            }
        }
    ],
    "links": {
        "self": {
            "href": "https://www.illinoislegalaid.org/jsonapi/node/helpful_organization"
        }
    }
  }

Parameters
=============
* identifier:  the uuid of the specific helpful organization can be included to return a specific organization.


Additional parameters supported by the JSONAPI are allowed. See the :ref:`ilao-api-filters` for filter examples.

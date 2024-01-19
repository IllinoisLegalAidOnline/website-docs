.. _ilao-api-filters:

========================
Customizing API results
========================

Filters
=======
For more specific examples, see the `Drupal filtering page <https://www.drupal.org/docs/core-modules-and-themes/core-modules/jsonapi-module/filtering>`_.

Each filter includes:

* Path (This is the field information. Note that these can be nested within relationships as well.)
* Condition (The condition to test for)
* Operator (if the operator is = it can be omitted)

Some examples:

* Return portal main page based on node ID: https://www.illinoislegalaid.org/jsonapi/node/portal_main_page?filter[foo][condition][value]=99536&filter[foo][condition][path]=drupal_internal__nid
* https://www.illinoislegalaid.org/jsonapi/oas_intake_settings/oas_intake_settings?filter[counties][value]=f81da2b5-dd82-42da-ba4a-75fecfef7760&filter[counties][path]=field_counties.id&filter[foo][condition][value][]=1821&filter[foo][condition][value][]=1811&filter[foo][condition][path]=drupal_internal__id&filter[foo][condition][operator]=IN Returns all intake settings that patch the specific county UUID and have an intake settings id of 1821 or 1811.



Include
========

Use the include parameter to return related resources.  Examples:

* https://www.illinoislegalaid.org/jsonapi/node/legal_problem?include=field_legal_issues will return the legal issues associated with a specific legal problem.
* https://www.illinoislegalaid.org/jsonapi/node/adrm/ed6914c6-6755-4281-a322-142f1b73cc21?include=field_content_type will include all of the content blocks within an ADRM article.
* https://www.illinoislegalaid.org/jsonapi/node/adrm/ed6914c6-6755-4281-a322-142f1b73cc21?include=field_content_type, field_content_type.paragraph_type will include all of the content blocks within an ADRM article and the paragraph type associated with each paragraphs block in the content type.


.. note:: Paragraphs add a layer of complexity to ILAO's JSON API. These should be included when attempting to render content that requires the full text. Creating REST exports in Views that use the same OAUTH permission may work better for some use cases.




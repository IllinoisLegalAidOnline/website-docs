.. _custom_site_config:

==============================
General search configuration
==============================

Our site search is managed through `Google's API console <https://console.cloud.google.com/gen-app-builder/engines>`_. Gwen and Mike have access to the search engines; please see them if you need something done.


Search Englines
=================

ILAO has 3 search engines:

* ILAO Site search 2025 is used on our English language pages
* ILAO-ES is used on our Spanish language pages


English
----------

Includes all pages from www.illinoislegalaid.org except for:

* anything in the /sites/default folder. This typically includes file content and images.
* anything in the /proxy path. This excludes IICLE content but not the IICLE landing page
* anything in the form-library or form-search paths. These are primarily navigation pages that should not be returned
* Basic pages that are being used to expose guided navigation for translation

The English search results are delivered over an API call. This give us some limited control over the display.

Spanish
----------

Includes all pages from es.illinoislegalaid.org. Pages that ILAO has not exposed for translation are already excluded.

The Spanish search is currently delivered via a widget.










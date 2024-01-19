=========================
Eviction functions
=========================

These functions are used in the eviction SMS project.

Eviction intake settings
==========================
**Function name:**  eviction-intake-settings

**Parameters:**  event.flow_id which is the phone number associated with an executed flow.  This is used to direct requests to production or staging based on a phone number.

**Returns:** An object containing:

* id, the uuid for the intake settings
* callback_number
* node_id, the intake settings ID for the custom entity
* callback_type
* bypass, the bypass message
* disclaimer
* please_call, the please call message
* we_call, the we call the client message
* legalservername, the name specifically required by Legal Server for etransfer
* organization, the organization name from our website to display to the user


**Requires:**  Access to the :ref:`ilao-api` for intake settings.

Eviction legal issues
======================
**Function name:**  eviction-legal-issues

**Parameters:**  event.choice which is the number of the legal issue identified in the eviction studio flow.

**Returns:** An object containing:

* issue (which is the name of the issue)
* issue_id, which is the UUID of the associated legal issues taxonomy term.
* notes, which is a sentence to include in the notes on an etransfer.

**Requires:**  This is hand-coded but future iterations may use the taxonomy piece of the :ref:`ilao-api`.

Eviction content
==================
**Function name:**  eviction-content

**Parameters:**  event.legal_issue, which is an integer representing the user's selected legal issue.

**Returns:** A string which includes the titles and links of relevant content to return.

**Requires:**  This is hand-coded but future iterations may use the :ref:`ilao-api`.

.. note:: This function will be updated to accommodate language codes.

HUD housing counselors
========================

**Function name:**  hud-housing-counselors

**Parameters:**  event.zip, which is the zip code of the user.

**Returns:** An object containing:

* An array of options.  Each option contains:

  * name
  * address
  * city
  * phone
  * weburl
  * methods (counseling methods)
  * services (services offered)

* A total, which is a number reflecting the total number of options.

**Requires:**  Access to the JSON files containing housing data: https://files.consumerfinance.gov/a/assets/hud/jsons/[zipcode].json

.. note:: This function should be updated to return Spanish results when appropriate.


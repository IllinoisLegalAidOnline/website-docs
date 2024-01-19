==============================
Integration with ILOI
==============================

ILOI is the statewide instance of Legal Server where online intakes are sent to be then accepted or rejected by individual organization instances of Legal Server.

Access
=========

To send cases to an Online Triage and Intake System partner, contact Mike Rush for assistance.

Access requires a distinct API key from ILAO to use. Additional configuration, such as custom fields, can be supported as well.


Endpoint
==========

The endpoint is available at https://ilao-8092.twil.io/iloi-endpoint


Expected format
==================

The endpoint expects a body containing the following JSON format.

Minimum
--------------
At minimum, we expect firstName, lastName, phone or email, and key.

.. code:: JSON

   { "firstName":"Test",
   "lastName": "Test",
   "phone":"5555555555",
   "email": "test@example.com",
   "key":"<your-api-key>"
  }

Additional supported data
-----------------------------

.. code:: JSON

 { "firstName":"Test",
  "lastName": "Test",
  "phone":"6308811337",
  "email": "gdaniels@illinoislegalaid.org",
  "phoneNote":"do not call",
  "address1":"120 S LaSalle",
  "address2":"Suite 1000",
  "city":"Chicago",
  "state":"Illinois",
  "zip":"60603",
  "key":"<your-api-key>"}


Notes
----------
Key-value pairs in addition to those contained in the Additional supported data example will be appended to the notes in Legal Server.

.. code:: JSON

  { "firstName":"Test",
  "lastName": "Test",
  "phone":"6308811337",
  "email": "gdaniels@illinoislegalaid.org",
  "phoneNote":"do not call",
  "address1":"120 S LaSalle",
  "address2":"Suite 1000",
  "city":"Chicago",
  "state":"Illinois",
  "zip":"60603",
  "Are you able to leave home":"Yes, with assistance",
  "Do you need assistance applying for social services?":"No",
  "key":"<your-api-key>"
  }

In this instance, the Note would include "Are you able to leave home: Yes with assistance; Do you need assistance applying for social services?: "No".





Response codes
=================

Successful eTransfer
------------------------

Successful eTransfers will return the ID created by LegalServer. This value is unique. It will also include a success status.

.. code:: JSON

   {"uuid": "bb1a89d0-a017-11ee-b63e-0e8d40a13cd5",
   "status": "Success"}


Failured eTranfser
--------------------
Failed eTransfers will contain a 400 bad request error and error message in the response.


Not authorized
-----------------
Not authorized will contain an error equal to 403 and error message in the response.



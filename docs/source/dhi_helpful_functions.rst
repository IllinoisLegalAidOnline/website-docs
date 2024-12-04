===========================
Helper functions
===========================

Helper functions are those that are invoked from Landbot to handle data exchanges or integrate with 3rd party tools.


Creditor match
=================

URL: https://debthelpillinois-3927.twil.io/creditor-match
Parameters: 

* name - name of the creditor provided
* score - the match score required to be included in the results; default is .5

Returns:

* an array of matches to ILAO's creditor taxonomy, ordered by score descending

Requires:

* Drupal view creditors-export that contains the name of creditors in the database.
* Twilio

Get County
===============

URL: https://debthelpillinois-3927.twil.io/get-county
Parameters: 

Requires one of:

* fullAddress

.. code-block::

   get-county?fullAddress=120 S La Salle St, Chicago, IL 60603, USA
   
* street, city, state, zip

.. code-block::

   get-county?street=120 S LaSalle St&city=Chicago&state=IL&zip=60603

  

Returns:

* the name of the county

Requires:

* Google Geocoding API
* Twilio

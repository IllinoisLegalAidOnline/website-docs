===============================
Houston AI Classifier API Docs
===============================

The `Houston.AI classifier <https://houston.ai/api/classify-docs>`_ is an API service that takes text and returns one or more legal problem codes based on the LSC problem code/Legal Server problem code taxonomy. 

Configuration in Drupal
=========================
We have a configuration page that allows us to store:

* Our API key, required to interact with the classifier
* The URL for the classifier API call
* the URL for the problem codes API call
* a default location
* minimum prediction score (this is not used by the API but is used by ILAO to exclude irrelevant results)

Methods
===========
We support invoking:
* /api/classify to post text and get one or more probabilities of a legal problem back.
* /api/problem-codes to download their list of problem codes.

.. todo::

   In a future iteration, we want to provide feedback back to improve the classifier.

Example
===========
A user enters the text "I need a divorce from an abusive spouse"

.. code-block:: json

   {
  "code": {
    "code": "32", 
    "label": "Divorce/Sep./Annul."
  }, 
  "geo": {
    "address": "Illinois, USA", 
    "censusBlock": null, 
    "city": null, 
    "congressionalDistrict": {}, 
    "coordinates": {
      "lat": 40.6331249, 
      "lng": -89.3985283
    }, 
    "county": null, 
    "publicHousingDetails": null, 
    "state": "Illinois", 
    "stateGovernment": {
      "lower": {
        "district": 88, 
        "name": "Keith P. Sommer"
      }, 
      "upper": {
        "district": 44, 
        "name": "William E. Brady"
      }
    }, 
    "zipCode": null
  }, 
  "message": "We are 0.9610651095153742 certain you are experiencing the following issue: 32 Divorce / Separation. \n\nThis is the distribution of other possibilities: [(0.021311676536352332, '42 Neglected/Abused/Dependent'), (0.010688531301630395, '33 Adult Guardianship / Conservatorship'), (0.003257986225328454, '30 Adoption'), (0.0025206869318519514, '31 Custody/Visitation'), (0.0011560094894626138, '37 Domestic Abuse')]", 
  "otherProbabilities": [
    {
      "code": {
        "code": "42", 
        "label": "Neglected/Abused/Dependent"
      }, 
      "probability": 0.021311676536352332
    }, 
    {
      "code": {
        "code": "33", 
        "label": "Adult Guardianship / Conservatorship"
      }, 
      "probability": 0.010688531301630395
    }, 
    {
      "code": {
        "code": "30", 
        "label": "Adoption"
      }, 
      "probability": 0.003257986225328454
    }, 
    {
      "code": {
        "code": "31", 
        "label": "Custody/Visitation"
      }, 
      "probability": 0.0025206869318519514
    }, 
    {
      "code": {
        "code": "37", 
        "label": "Domestic Abuse"
      }, 
      "probability": 0.0011560094894626138
    }
  ], 
  "probability": 0.9610651095153742, 
  "properNouns": [], 
  "sessionId": "ff65f15a-623c-434f-ba3b-02980316453d"}


A call to Houston.ai's classifier returns a JSON structure of the most likely probability and then any other likely probabilities. The code include the numeric LSC problem code and the label for that code.

============================
Intake
============================

When a user successfully completes a program's triage rules, they are provided the matching organization and may begin intake.

.. todo:: Once Guided Navigation is fully implemented, users will be able to chose where to apply to.

Intake process
================

The intake process generally:


* Collects client information including:

  * Name
  * Alias
  * Nicknames
  * Date of birth
  * Demographics information, based on organization preferences, including:

    * Race
    * Ethnicity
    * Gender
    * Marital Status
    * Preferred language

* Collects household size, broken into number of adults and children. Each organization may have their own definition of who to count.
* Collects income information. Some organizations may:

  * Not collect any income information
  * Waive income limits for some populations

* Contact information, including:

  * Phone type
  * Phone number
  * Opt-in for SMS
  * Email address
  * Address

If the user passes validation (see below):

* If the intake settings is set to "We call you," the user is given a list of appointment times.

  * These times are based on the intake settings, the service maximum limit, and the number of slots already filled.
  * The number of slots the user can pick is limited to the lesser of 3 or the number indicated by the program.
  * The user may opt to call the program instead

* If the intake settings is set to "You call us," the user is given a list of times they can call the program.

.. todo:: Currently this shows the callback slots; we will be replacing this to use Office hours instead.



Validation
============

Most partners have income limits.

* For programs with no income limits, the system will not check income
* For programs that waive income limits for some populations, the system will ignore income limits if the user indicated that they are a member of the population.
* For programs that have applicable income limits:

  * The system pulls the income standard to use and the maximum percentage from the intake settings or location_services.
  * The system pulls the income limits from the relevant Income standard entity.
  * The system calculates the user's monthly income based on the collected income information.
  * The system calculates the user's maximum income based on the income standard and household size
  * The system determines if the user is over income (monthly income exceeds maximum income) or not.

If the user is over-income, the user is diverted to referrals.

If the user is not over-income, they continue to the appointment and confirmation piece.



E-Transfer
============

When the user gets to the final intake confirmation screen, their information is sent to the statewide online intake server.

The e-transfer leverages Legal Server' intake API.

.. code-block:: json

   { "firstName": "Test",
    "middleName": "",
    "lastName": "Test",
    "eTransferOrganization": "Land Of Lincoln Legal Assistance Foundation",
    "aliasFirst": "",
    "aliasLast": "",
    "addressHome": {
        "address1": "120 Main Street ",
        "city": "Belleville",
        "state": "IL",
        "zip": "62220",
        "county": "17163"
    },
    "phoneHome": "315555555",
    "phoneHomeNote": "",
    "dateOfBirth": "1989-11-17",
    "email": "test@gmail.com ",
    "maritalStatus": "Separated",
    "race": "Other",
    "ethnicity": "",
    "gender": "Female",
    "language": "en",
    "citizenshipStatus": "",
    "immigrationStatus": "",
    "veteran": "",
    "disabled": "",
    "note": "Select the one that best fits your case:I want a divorce because I am being abused by my spouse. Or I want a divorce because my kids are being abused or in danger.; Do you have a safe phone number we can call you at?:Yes;; We call client; Callback Times:Wednesday, Jun 30, 2021, 12:00pm - 1:00pm;",
    "numberOfAdults": "1",
    "numberOfChildren": "1",
    "callbackType": "Callback",
    "callbackDayTime": "Callback Times:Wednesday, Jun 30, 2021, 12:00pm - 1:00pm",
    "externalID": "ILAOWeb-35825811",
    "incomes": [{"amount":"1100","frequency":12, "type":"Employment"}],
    "adverse_parties": {},
    "program": "",
    "customField": {},
    "jsonPayload": {},
    "legalProblemCode": "32 Divorce/ Separation/ Annulment"
    }

.. note:: In 2022 - 2023, we will begin to leverage the program, adverse_parties, customField, and jsonPayloadItem fields.


Adverse parties
-----------------

The JSON API supports passing Adverse party data. This includes:

* Type, required
* First name
* Last name
* Middle name
* Address (in addr1, addr2, city, state, and zip elements)
* Date of birth
* Social security number
* Gender
* Race

Supported types are:

* Business (not Landlord)
* Child
* Domestic Partner (not Spouse)
* Employer/Work Colleague
* Former Domestic Partner
* Former Spouse
* Landlord (Owner)
* Legal Guardian
* Neighbor
* Other
* Other Family Member
* Parent
* Property Manager
* Spouse

.. note:: ILAO will never collect or eTransfer social security numbers

.. code-block:: JSON

   [
   { "type": "Spouse",
   "first": "Test",
   "last": "Test",
   "middle": "Test",
   "zip": "55555",
   "addr1": "500 Test Boulevard",
   "addr2": "Apartment 333",
   "city": "Bensonville",
    "state": "IL",
    "dob": "2/02/1972",
   "ssn": "555-55-5555",
   "gender": "Male",
   "race": "Other" },
   { "type": "Landlord",
   "business_name": "XYZ Property Management",
   "zip": "55555",
   "addr1": "500 Test Boulevard",
   "addr2": "Apartment 333",
   "city": "Bensonville",
   "state": "IL",
    } ]

Custom Field transfers
=========================

The JSON API supports passing customField data two different ways.

* via "jsonPayload" - using this transfer allows the customField data to transfer directly to the partnering organization's LegalServer

  * To transfer using the custom field's lookup number:
     * "jsonPayload": {custom_field_name_lookup_123":2[space],[any other custom fields]
  * To transfer text into a custom field:
    * "jsonPayload": {custom_field_name_lookup_321":"text"},[any other custom fields]

* By transferring the customField information into ILAO's LegalServer and then matching that customField to the partnering organization's LegalServer

   * "custom_fields":{"ilao_custom_field_name_123":3[space],[any other custom fields]

.. code-block:: JSON


   { "firstName": "Test",
    "middleName": "",
    "lastName": "Test",
    "eTransferOrganization": "Land Of Lincoln Legal Assistance Foundation",
    "aliasFirst": "",
    "aliasLast": "",
    "addressHome": {
        "address1": "120 Main Street ",
        "city": "Belleville",
        "state": "IL",
        "zip": "62220",
        "county": "17163"
    },
    "phoneHome": "315555555",
    "phoneHomeNote": "",
    "dateOfBirth": "1989-11-17",
    "email": "test@gmail.com ",
    "maritalStatus": "Separated",
    "race": "Other",
    "ethnicity": "",
    "gender": "Female",
    "language": "en",
    "citizenshipStatus": "",
    "immigrationStatus": "",
    "veteran": "",
    "disabled": "",
    "note": "Select the one that best fits your case:I want a divorce because I am being abused by my spouse. Or I want a divorce because my kids are being abused or in danger.; Do you have a safe phone number we can call you at?:Yes;; We call client; Callback Times:Wednesday, Jun 30, 2021, 12:00pm - 1:00pm;",
    "numberOfAdults": "1",
    "numberOfChildren": "1",
    "callbackType": "Callback",
    "callbackDayTime": "Callback Times:Wednesday, Jun 30, 2021, 12:00pm - 1:00pm",
    "externalID": "ILAOWeb-35825811",
    "incomes": [{"amount":"1100","frequency":12, "type":"Employment"}],
    "adverse_parties": {},
    "program": "",
    "customField": {"ilao_custom_field_name_123":3 ,"ilao_custom_field_name_321":"Full-time"},
    "jsonPayload": {"custom_field_transfer_123":2 ,"custom_field_transfer_321":"Part-time"},
    "legalProblemCode": "32 Divorce/ Separation/ Annulment"
    }

Reminders
===============

Reminders are sent to completed e-transfers as follows:

* For those users who have a callback scheduled

  * By SMS, 1 hour and 24 hours before appointment if they opted-in to text
  * By email, 1 hour before appointment if they have not opted-in to text

* For those users who are instructred to call the organization:

  * By SMS, 1 day after their application, if they have opted in to text messaging
  * By email, 1 day after their application, if they have not opted in to text messaging




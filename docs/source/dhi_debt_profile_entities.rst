======================
User data structures
======================

Each visitor to the platform may have a profile associated with them. The profile will depend on a) whether they have an account and b) the type of problem(s) they have.


Account or user profile
========================

The account profile is the standard Drupal user account profile. This profile contains the information necessary to log in. This includes:

* username
* UID (user id)
* password
* email
* mobile number
* created (date created)
* changed (date of last change)

.. note: Even visitors who use just a mobile number and passcode to log in will have a fixed UID associated with them


Problem Profile
====================
The problem profile is the container that contains core information about a user's problem. A user may have multiple problem profiles, depending on how many problems they identify and store in the system.

For example, a user may have a a problem profile for "Debts" and a problem profile for "Divorce"; the user may have multiple debt problems but the metadata in the problem profile is shared across all of these.

This custom entity contains the core problem profile information:

+----------------------+-------------------+--------------------------------------+
| Field name           | Type              | Description                          |
+======================+===================+======================================+
| profile_id           | Auto number       | Unique ID for the profile            |
+----------------------+-------------------+--------------------------------------+
| uid                  | integer           | User ID for the account associated   |
|                      |                   | with the profile                     |
+----------------------+-------------------+--------------------------------------+
| type                 | varchar           | Type of problem; this will be the    |
|                      |                   | entity name that contains more       |
|                      |                   | specific data about the problem      |
+----------------------+-------------------+--------------------------------------+
| zip_code             | varchar           | Zip code of the problem              |
+----------------------+-------------------+--------------------------------------+
| created              | timestamp         | Date problem profile created         |
+----------------------+-------------------+--------------------------------------+
| changed              | timestamp         | Date problem profile was last changed|
+----------------------+-------------------+--------------------------------------+
| changed              | timestamp         | Date problem profile was last changed|
+----------------------+-------------------+--------------------------------------+
| terms_accepted_time  | timestamp         | Timestamp when TOS was accepted      |
+----------------------+-------------------+--------------------------------------+
| privacy_policy       | timestamp         | Timestamp when privacy policy was    |
| _accepted            |                   | accepted                             |
+----------------------+-------------------+--------------------------------------+
| in_illinois          | integer           | 0 or 1 depending on whether person   |
|                      |                   | in Illinois                          |
+----------------------+-------------------+--------------------------------------+
| city                 | varchar           | City where the legal problem is      |
|                      |                   | located                              |
+----------------------+-------------------+--------------------------------------+
| county               | varchar           | County of the problem                |
+----------------------+-------------------+--------------------------------------+
| zip_suffix           | varchar           | Suffix for a postal code             |
+----------------------+-------------------+--------------------------------------+
| user_associated_with | int               | User ID of the person tied to the    |
| _profile             |                   | profile                              |
+----------------------+-------------------+--------------------------------------+
| problem_type         | varchar           | String of problem type               |
+----------------------+-------------------+--------------------------------------+
| status               | int               | Drupal system published/not published|
|                      |                   | status                               |
+----------------------+-------------------+--------------------------------------+


Problem type identifies the broad probleme entity involved (like debt problem)

.. note:: The problem profile contains only very high level information to identify the more specific entity that will contain the actual problem information. While we initially are building this platform for debt, we may expand to support other problem types. If the user has a debt problem, the type will be "debt" which would then invoke the debt_problem_entity which contains specific debt problem metadata. If they had a divorce problem, there would be a divorce_problem_entity.



Expert system responses
==========================
This entity tracks data sent to and received back from any expert system (for example, the use of DialogFlow, Guided Navigation, or Landbot to perform filtering or triage)

+----------------------+-------------------+--------------------------------------+
| Field name           | Type              | Description                          |
+======================+===================+======================================+
| ID                   | Auto number       | Unique ID for the data record        |
+----------------------+-------------------+--------------------------------------+
| profile_id           | integer           | Problem profile the expert system    |
|                      | required          | data is associated with              |
+----------------------+-------------------+--------------------------------------+
| expert_system        | varchar           | name or url of the system            |
+----------------------+-------------------+--------------------------------------+
| expert_system_id     | varchar           | id of the expert system path used    |
+----------------------+-------------------+--------------------------------------+
| expert_system_uuid   | varchar           | unique id associated with the        |
|                      |                   | specific instance of the expert      |
|                      |                   | system                               |
+----------------------+-------------------+--------------------------------------+
| response_value       | JSON/text         | JSON representation of data received |
|                      |                   | from the expert system               |
+----------------------+-------------------+--------------------------------------+
| created              | timestamp         | Timestamp of when record created     |
+----------------------+-------------------+--------------------------------------+
| changed              | timestamp         | Timestamp of when record last changed|
+----------------------+-------------------+--------------------------------------+
| uid                  | integer           | User ID of the person associated     |
|                      |                   | with the response, if known          |
+----------------------+-------------------+--------------------------------------+


Example JSON from initial triage (not debt prioritization)
-----------------------------------------------------------

.. code-block:: 

   {{
  "id": 417400267,
  "problem_profile_id": null,
  "source": "https://cdn.landbot.io/landbot-3/preview.html?ts=1733866006523&config=https%3A%2F%2Fstorage.googleapis.com%2Flandbot.pro%2Fv3%2FH-2656275-4RASN8SAA0QV0NNO%2Findex.json",
  "profile_address": "5 E Chestnut St, Coal City, IL 60416, USA",
  "profile_city": "Coal City",
  "profile_county": "Grundy",
  "profile_zip_code": 60416,
  "profile_zip_suffix": null,
  "debt_type": "130051",
  "debt_problem_type": "130116",
  "debt_creditor_name": "Midland Credit Management, Inc.",
  "debt_creditor_type": "collection_agency",
  "debt_is_debt_collector": "True",
  "debt_last_payment_date": "2018/12/11"
  }

Example JSON from initial triage (debt prioritization)
-----------------------------------------------------------
When debt prioritization is included, it returns the term IDs for the types of debts in the debt_prioritization array.

.. code-block::

  {
  "id": 417400267,
  "problem_profile_id": 16,
  "source": "https://cdn.landbot.io/landbot-3/preview.html?ts=1731020055069&config=https%3A%2F%2Fstorage.googleapis.com%2Flandbot.pro%2Fv3%2FH-2646298-YIU9M453YSZ8TGVE%2Findex.json",
  "debt_prioritization": [
    "130006",
    "130016",
    "129996",
    "130101"
  ]
 }

  
  
User solutions
================================

This entity tracks the options for a specific problem.

+----------------------+-------------------+--------------------------------------+
| Field name           | Type              | Description                          |
+======================+===================+======================================+
| entity_id            | auto number       | Unique id for the data record        |
+----------------------+-------------------+--------------------------------------+
| nid                  | integer           | Node id of the option                |
+----------------------+-------------------+--------------------------------------+
| node_type            | varchar           | Type of the node                     |
+----------------------+-------------------+--------------------------------------+
| problem_id           | integer; required | Problem profile associated with the  |
|                      |                   | option                               |
+----------------------+-------------------+--------------------------------------+
| type                 | varchar; required | Problem type                         |
+----------------------+-------------------+--------------------------------------+
| status               | varchar           | Status of the solution               |
+----------------------+-------------------+--------------------------------------+
| created              | timestamp         | Timestamp of when record was created |
+----------------------+-------------------+--------------------------------------+
| changed              | timestamp         | Timestamp of when record was last    |
|                      |                   | changed                              |
+----------------------+-------------------+--------------------------------------+
| uid                  | integer           | User ID of the person associated with|
|                      |                   | the solution                         |
+----------------------+-------------------+--------------------------------------+
| description          | longtext          |                                      |
+----------------------+-------------------+--------------------------------------+



Status
---------
Status options are:

* Available - the system thinks the option may apply
* Unavailable - the system thought the option might have applied but further filtering ruled it out
* Yes - the user has identified this as their preferred option
* No - the user has ruled it out
* Maybe - the user is not sure but wants to hold on to the option
* Complete  - the user has completed the specific option
* In progress - the user is actively working on the option

User option progress
========================

This entity tracks the specific step activity for an option referenced in the user solution data entity.

+----------------------+-------------------+--------------------------------------+
| Field name           | Type              | Description                          |
+======================+===================+======================================+
| entity_id            | number            | Unique id for the data record        |
+----------------------+-------------------+--------------------------------------+
| option_id            | integer; required | Entity ID of the option from user    |
|                      |                   | solution data                        |
+----------------------+-------------------+--------------------------------------+
| step_id              | integer; required | paragraph ID of the step block       | 
+----------------------+-------------------+--------------------------------------+
| status               | varchar           | Status of the solution               |
+----------------------+-------------------+--------------------------------------+
| created              | timestamp         | Timestamp of when record was created |
+----------------------+-------------------+--------------------------------------+
| changed              | timestamp         | Timestamp of when record was last    |
|                      |                   | changed                              |
+----------------------+-------------------+--------------------------------------+
| uid                  | integer           | User ID of the person associated with|
|                      |                   | the solution                         |
+----------------------+-------------------+--------------------------------------+
| description          | longtext          |                                      |
+----------------------+-------------------+--------------------------------------+


Statuses here are:

* Not started
* In progress
* Completed

================================
Problem type specific entities
================================

While the platform is focusing on consumer debt, ILAO envisions replicating this to other types of problems. The entities defined above are generic while those below are tied to specific problem groups.

Consumer debt
=================

Debt problem entity
-----------------------

This entity contains all of the metadata for a user's specific debt problem but not information on specific debts. Specific debt information is in debt entities. A debt problem may have multiple debts attached.

.. note:: We currently envision a 1-1 relationship between debt problem and debts but the system is structured to accommodate the potential 1-many relationship in the future.

+----------------------+-------------------+--------------------------------------+
| Field name           | Type              | Description                          |
+======================+===================+======================================+
| entity_id            | auto number       | Unique entity id                     |
+----------------------+-------------------+--------------------------------------+
| profile_id           | integer           | Profile associated with the problem  |
+----------------------+-------------------+--------------------------------------+
| current_problem      | integer           | Term reference to the problem        |
|                      |                   | taxonomy                             |
+----------------------+-------------------+--------------------------------------+
| current_focus        | integer           | Entity id of the debt being focused  |
|                      |                   | on, if applicable                    |
+----------------------+-------------------+--------------------------------------+
| credit_score         | integer           | Credit score of the individual       |
+----------------------+-------------------+--------------------------------------+
| created              | timestamp         | Timestamp of when the record was     |
|                      |                   | first created in the system          |
+----------------------+-------------------+--------------------------------------+
| changed              | timestamp         | Timestamp of when the record was     |
|                      |                   | last changed in the system           |
+----------------------+-------------------+--------------------------------------+
| uid                  | integer           | User id of the person; 0 if anonymous|
+----------------------+-------------------+--------------------------------------+
| status               | integer           | 0 for unpublished / archived         |
|                      |                   | 1 for new / active                   |
+----------------------+-------------------+--------------------------------------+
| archived             | timestamp         | Timestamp of when a debt problem     |
|                      |                   | was archived                         |
+----------------------+-------------------+--------------------------------------+


Debt entity
-----------------

Debt entities are for specific debts. Different debt types may have different data associated with them. Debt entities are then tied to specific debt profiles.

+----------------------+-------------------+--------------------------------------+
| Field name           | Type              | Description                          |
+======================+===================+======================================+
| debt_id              | auto number       | unique identifier for the debt       |
+----------------------+-------------------+--------------------------------------+
| label                | varchar           | Name of the debt, as defined by user |
+----------------------+-------------------+--------------------------------------+
| debt_problem_id      | integer; required | id of the debt problem entity        |
+----------------------+-------------------+--------------------------------------+
| created              | timestamp         | Timestamp of when the record was     |
|                      |                   | first created in the system          |
+----------------------+-------------------+--------------------------------------+
| changed              | timestamp         | Timestamp of when the record was     |
|                      |                   | last changed in the system           |
+----------------------+-------------------+--------------------------------------+
| amount               | float             | Amount of the debt                   |
+----------------------+-------------------+--------------------------------------+
| last_payment_date    | varchar / date    | Date of last payment                 |
+----------------------+-------------------+--------------------------------------+
| interest_rate        | float             | Interest rate, if known              |
+----------------------+-------------------+--------------------------------------+
| debt_type            | integer           | Term reference to debt type taxonomy |
+----------------------+-------------------+--------------------------------------+
| creditor_name        | varchar           | Name of the creditor, if known       |
+----------------------+-------------------+--------------------------------------+
| creditor_type        | varchar           | Type of creditor                     |
+----------------------+-------------------+--------------------------------------+
| is_debt_collector    | integer/boolean   | 1 or 0; is creditor a debt collector |
+----------------------+-------------------+--------------------------------------+
| status               | integer           | published / not published            |
+----------------------+-------------------+--------------------------------------+
| uid                  | integer           | user ID associated with the debt     |
+----------------------+-------------------+--------------------------------------+         

Debt entities in prioritization
=================================

Debt prioritization does not factor in specific debt details but orders debt types based on general properties. As such, much of the problem and debt data is missing.


When a user completes prioritization, for each debt type included in the prioritization matrix:


* A debt_problem entity is created for each debt type in the prioritization matrix with:

  * profile_id added
  * created and changed timestamps set
  
* A debt entity is created:

  * debt_id is automatically generated
  * debt_problem_id is set to the debt_problem entity just created
  * created and timestamp are set
  * debt_type is set to the taxonomy term prioritized
  * all other fields are ignored
  
* The debt_problem entity is updated to set the current_focus = to the debt entity ID



  







====================
User profile data
====================

Each visitor to the platform may have a profile associated with them. The profile will depend on a) whether they have an account and b) the type of problem(s) they have.

Account or user profile
========================

The account or user profile is the standard Drupal user account profile. This profile contains the information necessary to log in. This includes:

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

For example, a user may have a a problem profile for "Creditors are calling me", a problem profile for "I have a judgment against me", "I am being sued on a debt."

This custom entity contains the core problem profile information:

+----------------------+-------------------+--------------------------------------+
| Field name           | Type              | Description                          |
+======================+===================+======================================+
| profileID            | Auto number       | Unique ID for the profile            |
+----------------------+-------------------+--------------------------------------+
| uid                  | integer           | User ID for the account associated   |
|                      |                   | with the profile                     |
+----------------------+-------------------+--------------------------------------+
| type                 | varchar           | Type of problem; this will be the    |
|                      |                   | entity name that contains more       |
|                      |                   | specific data about the problem      |
+----------------------+-------------------+--------------------------------------+
| entity_id            | integer           | The specific entity of type          |
+----------------------+-------------------+--------------------------------------+
| created              | timestamp         | Date problem profile created         |
+----------------------+-------------------+--------------------------------------+
| changed              | timestamp         | Date problem profile was last changed|
+----------------------+-------------------+--------------------------------------+

.. note:: The problem profile contains only very high level information to identify the more specific entity that will contain the actual problem information. While we initially are building this platform for debt, we may expand to support other problem types. If the user has a debt problem, the type will be "debt" which would then invoke the debt_problem_entity which contains specific debt problem metadata. If they had a divorce problem, there would be a divorce_problem_entity.

Sample data:

+------------+----------+--------------+-----------+-------------+-----------------+
| profileID  | uid      | type         | entity_id | created     | changed         |
+============+==========+==============+===========+================+==============+
| 1          | 2        | debt problem | 21        |1723147452   | 1723147452      |
+------------+----------+--------------+-----------+-------------+-----------------+
| 6          | 2        | debt problem | 26        |1723147452   | 1723147775      |
+------------+----------+--------------+-----------+-------------+-----------------+
| 11         | 4096     | debt problem | 31        |1723147775   | 1723147775      |
+------------+----------+--------------+-----------+-------------+-----------------+
| 11         | 4096     | divorce      | 31        |1723147775   | 1723147775      |
|            |          | problem      |           |             |                 |
+------------+----------+--------------+-----------+-------------+-----------------+

In the above, User 2 has 2 problem profiles, both for debt problems. Those debt problems can be accessed via the debt problem entities 21 and 26. User 4096 has two problem profiles - 1 for debt and 1 for divorce (assuming a future expansion)

Debt problem entity
==========================

This entity contains all of the metadata for a user's specific debt problem but not information on specific debts. Specific debt information is in debt entities. A debt problem may have multiple debts attached.

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
| created              | timestamp         | Timestamp of when the problem was    |
|                      |                   | first created in the system          |
+----------------------+-------------------+--------------------------------------+
| changed              | timestamp         | Timestamp of when the problem was    |
|                      |                   | last changed in the system           |
+----------------------+-------------------+--------------------------------------+

.. warning:: This is being reworked as of 8/8/24. Stop here.

Debt entity
=============

Debt entities are for specific debts. Different debt types may have different data associated with them. Debt entities are then tied to specific debt profiles.

* debt_id - unique id for the debt entity (auto generated)
* problem_profile_id - unique id for the profile assocaited with the debt
* name - name of the debt (as provided by the user)
* created - timestamp
* changed - timestamp
* amount - float
* current stage of the debt - varchar
* interest rate - float
* debt type (from debt type taxonomy)
* creditor name - varchar


Expert system data
==========================
This entity tracks data sent to and received back from any expert system (for example, for collecting debt information, for filtering questions, or option evaluation)

* es_id - expert system unique id (autointeger)
* debt_id - id of the debt (integer)
* profile_id - profile involved (integer)
* data_input - json of data sent to expert system
* expert_system - id of the expert system invoked (varchar)
* data_response - json of data returned from expert system
* created - timestamp
* changed - timestamp


Profile solutions
================================
This entity tracks the solutions for a specific debt profile

* solution_id - unique identifier for the entity
* nid - node id of the selected solution
* profile_id - profile id associated with the solution
* solution_status - selected, available, rejected, unavailable, needs reviewed
  * Selected = user has chosent this option
  * Avaiable - user has gone through any filtering questions and it matched
  * Rejected - user has gone through any filtering questions but has marked it as no
  * Unavailable - user has gone through any filtering question and this option is not an option for this user
  * Needs reviewed - user has not gone through any filtering question; this may be an option but requires more evaluation.
* current_step - current step in the solution
* created - timestamp
* changed - timestamp




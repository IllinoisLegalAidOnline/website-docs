====================
User profile data
====================

Each visitor to the platform may have a profile associated with them. The profile will depend on a) whether they have an account and b) the type of problem(s) they have.

Overview of the workflow
===========================

**1. Account Creation and Initial Setup:**
- **Individual A** visits the platform and decides to create an account. After filling out the necessary information, their account is successfully created, and they are assigned **User ID 2**.
- Once logged in, Individual A is prompted to answer initial questions that help define their situation. They indicate they are facing a legal issue by selecting the problem type: **"I am being sued for a debt."** Additionally, they input their **zip code, 60603**.

**2. Problem Profile Creation:**
- The platform takes the information provided and creates a **Problem Profile** associated with **User ID 2**. This profile includes:
  - **Problem Type:** Debt
  - **Zip Code:** 60603
- Recognizing the nature of the issue, the system also generates a **Debt Problem Entity Record**. This record is directly tied to the problem profile and stores crucial information:
  - **Problem Taxonomy Term:** 16, labeled **"I am being sued on a debt"**.
- The **Problem Profile** is updated to include a reference to the newly created **Debt Problem Entity**.

**3. Integration with DialogFlow:**
- As Individual A navigates through the platform, their **debt problem** and **zip code** are transmitted to **DialogFlow**. Here, the system identifies the appropriate flow, **"Debt lawsuit"**, to manage the conversation.
- At this stage, an **Expert System Response Record** is generated, capturing the JSON data sent from Drupal to DialogFlow. This record is vital for ensuring accurate tracking, troubleshooting, and analytics.

**4. Processing Response Data:**
- When DialogFlow sends a response, it is logged in the existing **Expert System Response Record**. This response contains further details about Individual A’s debt situation.
- The platform’s **Processor Module** is activated to parse the response data. The module updates the debt problem entity by:
  - Creating additional **Debt Entities** if specific debts are identified, each tied back to the **Debt Problem Entity**.
  - Updating the **Debt Problem Entity** with new details, such as the current debt focus, credit score, and other debt-specific information.
  - Identifying potential solutions for Individual A. For each solution identified, a **Profile Option Entity** is created and linked to the **Debt Problem Entity**. Each solution is initially marked as **"Available"**.

**5. Interaction with Expert Systems:**
- As Individual A continues to interact with the platform, they may be presented with additional questions from the expert system.
- Each new interaction generates another **Expert System Response Record** to log the exchange and the response.
- If any potential solutions are deemed unsuitable by the expert system, the associated **Profile Option Entity** is updated to reflect a status of **"Unavailable"**.

**6. Review and Selection of Options:**
- When Individual A reviews the available options, they can mark each one with a status of **Yes, No, or Maybe** based on their preferences.
- The system records these choices and updates the **Profile Option Entity** with the current step and a timestamp reflecting their progress.

**7. Completion of Options:**
- As Individual A works through the steps of a selected option, the system continually updates the **Profile Option Entity** to reflect the current step and the time of the last change.
- Once all steps of an option are completed, the **Profile Option Entity** status is updated to **"Complete,"** signaling that Individual A has finished that particular path.


.. note:: Do we need to track a status for the problem profile (New, Active, Abandoned, Solved)? What would those statuses be?


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
| zip_code             | varchar           | Zip code of the problem              |
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
| type                 | varchar           | entity type of a specific entity     |
|                      |                   | associated with the data stream      |
+----------------------+-------------------+--------------------------------------+
| entity_id            | integer           | id of the entity of TYPE             |
+----------------------+-------------------+--------------------------------------+
| expert_system        | varchar           | name or url of the system            |
+----------------------+-------------------+--------------------------------------+
| expert_system_id     | integer           | id of the expert system path used    |
+----------------------+-------------------+--------------------------------------+
| expert_system_uuid   | varchar           | unique id associated with the        |
|                      |                   | specific instance of the expert      |
|                      |                   | system                               |
+----------------------+-------------------+--------------------------------------+
| input                | JSON/text         | JSON representation of data sent to  |
|                      |                   | expert system                        |
+----------------------+-------------------+--------------------------------------+
| response             | JSON/text         | JSON representation of data received |
|                      |                   | from the expert system               |
+----------------------+-------------------+--------------------------------------+
| created              | timestamp         | Timestamp of when record created     |
+----------------------+-------------------+--------------------------------------+
| changed              | timestamp         | Timestamp of when record last changed|
+----------------------+-------------------+--------------------------------------+



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






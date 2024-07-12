================
Debt profile
================

The debt profile is composed of the following entities:

* debt_profile_user entity
* debt_profile_debt entity

Debt profile user
====================
This custom entity contains the core debt profile information:

* profile_id - unique id for the profile
* uid - user id (0 if anonymous)
* current_problem - from problem type taxonomy
* current_debt_focus - from debt entity if they are currently focusing on 1 specific debt
* credit_score - integer
* created - timestamp
* changed - timestamp


A user may have more than one debt profile depending on what they are focusing on.

Debt entity
=============

Debt entities are for specific debts. Different debt types may have different data associated with them. Debt entities are then tied to specific debt profiles.

* debt_id - unique id for the debt entity (auto generated)
* profile_id - unique id for the profile assocaited with the debt
* name - name of the debt (as provided by the user)
* created - timestamp
* changed - timestamp
* amount - float
* current stage of the debt - varchar
* interest rate - float
* debt type (from debt type taxonomy)
* creditor name - varchar


Debt expert system data
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


Selected debt solutions entity
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


Example
============

User
 Name: John Doe
 User ID: 1
 Debt Profile:
   Profile_ID: 6
   UID: 1
   Current problem: Trouble paying my bills
   Current debt focus: [7, 9]
   Debt entities:
     Debt id: 7
     Name:  My credit card from Chase
     Amount: 5000
     Interest Rate: 17.99%
     Debt type: Credit card
     Creditor name: Chase bank

     Debt id: 9
     Name: Discover card
     Amount: 3000
     Interest rate: 20.7%
     Debt type: Credit card
     Creditor name: Discover

     Debt id: 11
     Name: Surgery bills
     Amount: 25,000
     Interest rate:
     Debt type: Medical debt
     Creditor name: County hospital

  Debt Expert System
    Date: 7/1/2002
    Initial: {Problem-type:Trouble paying bills}
    Response: Here is the JSON packet for the provided data:
    { "debts": [
    {
      "name": "My credit card from Chase",
      "amount": 5000,
      "interest_rate": 17.99,
      "debt_type": "Credit card",
      "creditor_name": "Chase bank"
    },
    {
      "name": "Discover card",
      "amount": 3000,
      "interest_rate": 20.7,
      "debt_type": "Credit card",
      "creditor_name": "Discover"
    },
    {
      "name": "Surgery bills",
      "amount": 25000,
      "interest_rate": null,
      "debt_type": "Medical debt",
      "creditor_name": "County hospital"
    },]}

  Debt solutions
    solution_id = 1
    profile_id = 1
    nid = 45000
    status = selected
    current_step = 1

    solution_id = 2
    profille_id =1
    nid = 45006
    status = rejected
    current_step = 0

    solution_id = 3
    profile_id = 1
    nid = 45010
    status = needs_reviewed
    current_step = 0


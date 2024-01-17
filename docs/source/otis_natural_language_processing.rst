==============================================
Natural language processing of legal problem
==============================================

The current website uses an autocomplete to our legal issues taxonomy to direct a user to the appropriate triage rules or referrals. The accuracy of this is dependent on how the user interacts with the field:

* Users can pick a term from the autocomplete. If they do:

  * and it is the lowest level term in the taxonomy, they are matched to the triage rules
  * and it is not the lowest level term in the taxonomy, they are taken to a screen to filter through the taxonomy to the lowest level, starting with the term they entered.
  
* Users can type text into the autocomplete. If they do:

  * and it is an exact match to a term in the taxonomy, then it is treated as if the user selected the term from the autocomplete
  * and it is not an exact match to a term in the taxonomy, the user is taken to the top of our legal issues taxonomy to filter down to the lowest level problem.
  
The classifiers will be used to improve that last use case, where the user doesn't match to anything in the taxonomy, to at least get the user into a more discrete top level category than the full list of top categories.

Processor Algorithm
=====================

If the user's input is an exact match to the legal issues taxonomy => no change in the current system is made

If the user's input is not an exact match to the legal issues taxonomy:

* User input is passed to both Houston.ai and Spot classifier
* A combined list of results are culled together, ranked and mapped back to ILAO's IA
* The user is presented with a short list of options based on the classifier data.


Examples
------------
These examples require a score of .8 or higher in Houston AI and .6 for LIT Spot

"I am getting evicted from my apartment"

* Houston AI returns private/landlord tenant
* Spot returns:

  * Eviction from a homeless shelter or group home (83.968495156154)
  * Eviction from private rental housing (not public or subsidized) (88.335262899271)
  * Notice and Procedural defenses against an eviction (76.408919436079)
  * Living conditions (habitability) defenses against an eviction (83.987595048243)
  * Title and ownership defenses against an eviction (78.661704605665)
  * Retaliatory Eviction defenses against an eviction (76.335103161464)
* ILAO would offer the user ?

"I want a divorce"

* Houston AI returns Divorce/Sep/Annul
* Spot returns family
* ILAO would drop the user into Divorce

"I was denied unemployment"

* Houston AI returns unemployment compensation
* Spot returns unemployment benefits, compensation, and insurance
* ILAO would drop the user into unemployment benefits

"my spouse beat me up"

* Neither returns anything good
* ILAO would drop the user at the top of the tree
  
"I can't afford my groceries"

* Houston AI returns Bankruptcy/Debtor relief
* Spot returns Food and cash benefits
* ILAO would offer the user multiple options to pick from:

  * Food stamps
  * TANF
  * Bankruptcy
  
  
Technical Implementation
=========================

* Implement classifier module for Houston AI (DEV-2809/DEV-2881)
* Implement classifier module for Spot AI (DEV-2812/DEV-2882)
* Add fields to the legal issues taxonomy to map LSC and NSMI codes against it (DEV-2886)
* Update the legal issues taxonomy to include codes where they should be added (Gwen)
* Write code to invoke the classifier where needed and return the right data sets (DEV-2887)

  

  
  
    
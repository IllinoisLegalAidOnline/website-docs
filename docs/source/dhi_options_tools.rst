============================
Options & Tools Integration
============================

Each tool includes:

* A landbot URL. This URL is then used to 

  * Embed the Landbot in a step in an option when the [tool:nid:embed] token is used
  * Embed the Landbot in a legal resource standalone page
  
* A field name to store profile metadata term references for the tool. Each possible term that the tool can return should be added to the Problem Profile Metadata taxonomy
* The entity the field should be attached to (debt, debt problem, or problem profile)
* Three long text fields that are used to determine what displays when the [tool:nid:response] token is used in a step in an option. The three fields are:

  * Text when the tool has been completed and there is data. This will appear when the user has completed the tool and there is relevant metadata stored. For example, if someone has completed the collection proof tool and is collection proof, the is_collection_proof metadata will exist.
  * Text when the tool has been completed and there is no data. This will appear when the user has completed the tool but there is no relevant metadata stored. For example, if someone has completed the collection proof tool and is not collection proof, the is_collection_proof metadata will not exist.
  * Text when the tool has not been completed. This will appear when the user has not completed the tool.
  

.. warning:: The developers must create the actual field on the entity before data can be stored.
  
Example
===========================

For a tool "Claim detector" with a node ID of 6 that is embedded in the first step of "Settle the case"

On the Tool side
--------------------

In the CMS, the tool is set up as:

* Landbot URL = "someurl.com"
* Field is tool_claims
* Field is attached to debt entity
* Text when the tool has been completed and there is data: "You have identified these potential claims: [current_debt:claims:list]"
* Text when the tool has been completed and there is no data: "You did not identify any potential claims."
* Text when the tool has not been completed: "Please complete the previous step before continuing."

In the option
-----------------

* Step 1 is set up as "Determine if you have any claims. We can help guide you. [tool:6:embed]"
* Step 2 is set up as "Having claims you can raise can help you negotiate a better settlement than if you don't have claims. [tool:6:response]"

.. note:: The **[tool:nid:embed]** creates the embed code, passing in required debt entity, profile entity, and debt problem entity ID automatically. The **[tool:nid:response]** is used to evaluate and update narrative based on the user's response.


What the user sees
---------------------

When the user has not completed the tool:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: html

   <h3>1. Determine if you have any claims<h3>
   <p>Embedded landbot</p>
   <h3>2. Determine your negotiation strategy<h3>
   <p>Having claims you can raise can help you negotiate a better settlement than if you don't have claims. Please complete the previous step before continuing.</p>
   
   
When the user has completed the tool:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* And they have a claim of "Wrong venue"
* And the Wrong venue taxonomy term has Text to show if true of "The creditor filed the case in the wrong venue; this means you can have it dismissed and they must refile in the right county."

.. code-block:: html

   <h3>1. Determine if you have any claims<h3>
   You've completed this step.
   <h3>2. Determine your negotiation strategy<h3>
   <p>Having claims you can raise can help you negotiate a better settlement than if you don't have claims. You have identified these potential claims: The creditor filed the case in the wrong venue; this means you can have it dismissed and they must refile in the right county.</p>
   
* And they have no claims

.. code-block:: html

   <h3>1. Determine if you have any claims<h3>
   You've completed this step.
   <h3>2. Determine your negotiation strategy<h3>
   <p>Having claims you can raise can help you negotiate a better settlement than if you don't have claims. You did not identify any potential claims.</p>



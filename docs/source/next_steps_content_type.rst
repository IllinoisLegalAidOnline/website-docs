.. _NextStepsAuthoring:

=======================================
Authoring NextStep Flows
=======================================

The Next Steps Flow content type is where we create NextStep Flows. These flows are then used to populate our SMS-based NextSteps application and schedule and track messages being sent and received.

A Next Steps Flow must be attached to a single Legal How-to. Once the Legal How-to is selected, a staff member can create messages attached to 1 or more steps associated with that Legal How-to.

.. warning:: Legacy "How-to" content can not be used for this. Only COPE-based Legal How-to's can be used. The system supports both published and unpublished Legal How-tos and Legal Steps while ILAO works through our legal information redesign process.

.. note:: The SMS application will automatically add to the initial message a Welcome mesage that links to the full How-to and append standard opt out and help keywords. ILAO respects all opt-out requests.

.. image:: ../assets/next-step-subscribe.png

Creating a Next Steps Flow
===============================

For each next step flow, you must:

* Give the flow a title. This title should reflect the how-to; it will be displayed in widgets partners use to subscribe people to NextSteps. Some example titles are below:

    * Applying for TANF benefits
    * Appealing a TANF decisions (was receiving benefits)
    * Appealing a TANF decision (was not receiving benefits) - the difference between this and the one above is that there is no option to continue benefits step in the process.

* Tie the flow to an LSC problem code. This is required to align with OTIS partners' systems and allow them to easily filter available flows.
* Attach the appropriate Legal How-to

.. image:: ../assets/nextsteps_header.png

Create the first message for a step
=======================================

Once the Legal How-to is attached, the Step dropdown will populate with the list of steps. **Always start the flow with the first step.** It is easier for authors to visualize if the steps are added in the same order as the How-to.

.. image:: ../assets/nextsteps_firststep.png

.. note:: The initial message is what a subscriber will receive when they are initially placed in the step.

Creating the initial message
-------------------------------
Ideally, messages should be less than 160 characters but can not be more than 1600.  Some examples:

   * The first step before getting an order of protection is to make sure you are safe? Are you safe? Reply Yes or No.
   * Have you filled out an application for cash assistance (TANF)? Reply No if you have not filled out an application. Reply YES if you have filled it out on paper or Reply ONLINE if you applied online.

.. warning:: Avoid using words inside quotation marks in your messages (e.g., "Yes", "No"). Some carriers flag quoted words as spam, which may prevent delivery. Instead, use plain words without quotes.

The initial message should always use the "Send and wait for reply" option to allow the system to process any received text message. The message should include options of Yes, No, and optionally a unique keyword when Yes and No are not sufficient to route the reply. See the Add replies below.

.. note:: The body (plain text) will automatically populate once the content is saved. This is a system field that will take any HTML included in the body and convert it to text-message friendly format.


Select the message type
--------------------------

  * Send and wait for reply - this tells the system to expect a reply from the individual. You'll need to then add replies.
  * Send, no reply - this tells the system to ignore any replies as we don't expect them. This is typically used only on the last step.

.. image:: ../assets/next-step-component.png


Add replies to an initial message
====================================

If your message has a message type of "Send and wait for reply," you must add reply handlers. Reply handlers are limited to processing replies of:

* Yes (will also handle various ways someone may reply Yes, such as Y, Yep, yeah, including in Spanish and Polish)
* No (will also handle various ways someone may reply No, such as N, nope, not, including in Spanish and Polish)
* No match, for cases where someone replies with something the system can't handle or where we have offered a third option. For example, in the TANF example above, a reply of "ONLINE" would be treated as No match.
* No reply, for cases where someone was sent a message but does not reply within Twilio's time out (4 hours).

For each reply:
------------------
If there needs to be a follow up response (most common)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Create a follow up message.

* Follow up messages should:

  * Reassure the subscriber, if appropriate.
  * Provide gentle reminders of what they need to do to move forward, if appropriate
  * Provide information on the action they need to take
  * A timeline for when they can expect a follow up message.

.. warning:: The include field only supports Legal Question and Legal Step content. While those are on hold, do not use that field. Any legal information should be included in the text message and reviewed by the legal content manager for the specific legal issue for accuracy.

Schedule the follow up message to immediately.

If there is no follow up response needed (uncommon)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Leave the body empty
* Set the schedule the message to "No reply"

Instances where this would be used:

* When the reply type is "No reply". In this instance, you probably do not want to send any follow up message.


.. todo:: Consider whether we can handle "No reply" messages in a more automated way.

In either case:
^^^^^^^^^^^^^^^^^

* Indicate if this is the last step in the flow. It is possible that more than one step is a last step, depending on the individual's reply.

.. todo:: Make the survey send automatic.

If this is the last step:

When this is the last step, please include the text https://go.illinoislegalaid.org/flows?nid=[node:nid]&id=[nextstepsuser:id] in the message so that a survey to evaluate the process is sent to the applicant.

.. todo:: Hide the next follow up step/send follow up fields when this is the last step.

If this is not the last step:

* Schedule a next step follow up, if this is not the last step:

  * Pick the step to follow up with next (this can be the current step or a future step)
  * Schedule when to send the next message,in days.
  * Set a maximum number of times to resend the reply follow up. This is used if the subscriber does not reply.

Repeat for each type of reply the system needs to handle for the specific step.


.. image:: ../assets/next-step-replies-add.png


Additional Steps
====================

Repeat the "Create the first message for a step" and "Add Replies" for each step in the flow.

Viewing the NextStep flows
============================

Staff can view the entire NextStep flows to see how the process works. This is helpful to catch any errors in the flow. These views are not exposed to search or navigation.

.. image:: ../assets/next-step-flows-view.png










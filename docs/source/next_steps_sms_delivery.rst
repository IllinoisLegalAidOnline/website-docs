=================================
Next Steps SMS Subscriptions
=================================

Overview
==============

When a user is subscribed to a NextStepFlow:

* A next step message entity is created with the minimum initial data
* The initial message applicable to that step, if it exists, will be sent out to the individual using the NextStepFlows Studio Flow. That flow expects:

  * ID of the nextStepMessage
  * Text to send as Message
  * Message type (Send; no reply or Send and wait for reply)
  * Mobile phone of the user
  * From number

* If the message accepts a reply, that reply gets sent to an endpoint on the website which is expecting a JSON packet of:

  * ID
  * Response

* The response is then processed:
  * Response gets stored as the replY_received for the nextStepMessage that matches on the returned ID
  * Processes the reply by comparing the Response to the Next Step Replies as a string match and:

     * Updates the nextStepMessage entity to set the next_step to the next follow up step
     * Sets the next_step_due_date to the current date + number of days
     * Sets the resend_count = resend_count + 2

   * Sends the "Send this message" component if send message = immediately.


Twilio integration
======================

The website should send the initial message to

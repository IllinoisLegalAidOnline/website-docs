========================================
NextStep Flows Technical Specificiation
========================================


Next Flow Content Type
=========================

+------------------------------+----------------------------------+--------------------+
| Field                        | Description                      |  Type              |
+==============================+==================================+====================+
| Title                        | Title for the flow               | Title              |
+------------------------------+----------------------------------+--------------------+
| Legal How-to                 | Single select for the associated | Entity reference   |
|                              | legal how-to content type        |                    |
+------------------------------+----------------------------------+--------------------+
| Next Step Component          | Container for a specific next    | Paragraphs;        |
|                              | step                             | unlimited          |
+------------------------------+----------------------------------+--------------------+

Next Step Component
======================

The next step component contains the triggering step, initial message and handling for replies.


+------------------------------+----------------------------------+--------------------+
| Field                        | Description                      |  Type              |
+==============================+==================================+====================+
| Step                         | Single select for the associated | Entity reference   |
|                              | steps in the how-to              |                    |
+------------------------------+----------------------------------+--------------------+
| Initial message              | Message to send when triggered   | Paired Markup      |
|                              |                                  | unlimited          |
+------------------------------+----------------------------------+--------------------+
| Message type                 | Single select - Message and wait | Select             |
|                              | for reply OR message             |                    |
+------------------------------+----------------------------------+--------------------+
| Replies                      | Container for processing replies | Paragraphs;        |
|                              |                                  | unlimited          |
+------------------------------+----------------------------------+--------------------+

Replies
=============

Replies live within the Next Step Component and are designed to store information for processing a reply and determining next steps.


+------------------------------+----------------------------------+--------------------+
| Field                        | Description                      |  Type              |
+==============================+==================================+====================+
| When the user replies        | Single select                    | Term reference     |
+------------------------------+----------------------------------+--------------------+
| Send this message            | Text of follow up                | Paired markup      |
+------------------------------+----------------------------------+--------------------+
| Send message                 | Single select (immediately or    | List               |
|                              | time from trigger or no reply)   |                    |
+------------------------------+----------------------------------+--------------------+
| Time from reply              | Number of days to send when      | Number             |
|                              | Send message is set time         |                    |
+------------------------------+----------------------------------+--------------------+
| Last step                    | Indicate if this is the last     | Boolean            |
|                              | or not                           |                    |
+------------------------------+----------------------------------+--------------------+
| Next follow up step          | Single select of availalbe       | Entity reference   |
|                              | steps                            |                    |
+------------------------------+----------------------------------+--------------------+
| Send follow-up step in       | Number of days to send follow    | Number             |
|                              | up step                          |                    |
+------------------------------+----------------------------------+--------------------+
| Maximum re-sends             | Maximum times we should send     | Number             |
|                              | a specific initial message       |                    |
+------------------------------+----------------------------------+--------------------+


Next Steps User Entity
=========================

The next steps user entity is used to track users subscribed to next steps.


+------------------------------+----------------------------------+--------------------+
| Property                     | Description                      |  Type              |
+==============================+==================================+====================+
| ID                           | Unique ID for the subscription   | Auto number        |
+------------------------------+----------------------------------+--------------------+
| UID                          | User ID of the subscriber; 0 if  | integer            |
|                              | unknown                          |                    |
+------------------------------+----------------------------------+--------------------+
| uuid                         | Legal Server uuid, if known      | varchar            |
+------------------------------+----------------------------------+--------------------+
| triage_id                    | OTIS triage user id, if known    | integer            |
+------------------------------+----------------------------------+--------------------+
| created                      | Date entity was created          | timestamp          |
+------------------------------+----------------------------------+--------------------+
| changed                      | Date entity was updated          | timestamp          |
+------------------------------+----------------------------------+--------------------+
| source                       | Source of subscription           | varchar            |
+------------------------------+----------------------------------+--------------------+
| mobile_phone                 | Mobile phone number subscribed   | varchar            |
+------------------------------+----------------------------------+--------------------+
| email                        | Email address subscribed         | varchar            |
+------------------------------+----------------------------------+--------------------+
| notification_type            | SMS, mail, or web                | varchar            |
+------------------------------+----------------------------------+--------------------+
| is_otis_case                 | 1 or 0                           | boolean            |
+------------------------------+----------------------------------+--------------------+
| zipcode                      | User's zip code                  | varchar            |
+------------------------------+----------------------------------+--------------------+
| preferred_language           | Language the user wants messages | varchar            |
+------------------------------+----------------------------------+--------------------+
| flow_id                      | NID of the flow subscribed to    | integer            |
+------------------------------+----------------------------------+--------------------+
| initial_step                 | NID of the flow's first step     | integer            |
+------------------------------+----------------------------------+--------------------+

NextStep Message Entity
=========================

This Message entity is used to store a history of messages sent.

+------------------------------+----------------------------------+--------------------+
| Property                     | Description                      |  Type              |
+==============================+==================================+====================+
| ID                           | Unique ID for the message        | Auto number        |
+------------------------------+----------------------------------+--------------------+
| nextStepUserID               | ID from the nextStep user entity | Integer/ entity    |
|                              |                                  | reference          |
+------------------------------+----------------------------------+--------------------+
| created                      | created date/time                | timestamp          |
+------------------------------+----------------------------------+--------------------+
| changed                      | changed date/time                | timestamp          |
+------------------------------+----------------------------------+--------------------+
| step_sent                    |  ID of the component sent        | integer            |
+------------------------------+----------------------------------+--------------------+
| reply_received               |  Reply received                  | string             |
+------------------------------+----------------------------------+--------------------+
| next_step                    | ID of the next step to send      | integer            |
+------------------------------+----------------------------------+--------------------+
| next_step_due_date           | date to send next step           | timestamp          |
+------------------------------+----------------------------------+--------------------+
| resent_count                 | integer                          | integer            |
+------------------------------+----------------------------------+--------------------+







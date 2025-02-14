=====================
DHI Content Types
=====================

Legal resources
==================
The legal resources content type is designed to be a flexible content type to store any legal or financial information that is not an Option or a Snippet.

The legal resource type:

* Automatically creates new revisions
* Does not have preview enabled
* Does not allow comments

+----------------------+----------------+------------------------------------------+
| Field                | Type           | Description                              |
+======================+================+==========================================+
| Title                | String (short) | Title of the resource                    |
|                      | Required       |                                          |
+----------------------+----------------+------------------------------------------+
| Description          | String (long)  | Description for use in social media and  |
|                      | Required       | on site listings / search                |
+----------------------+----------------+------------------------------------------+
| Content format       | Select one     | Type of content                          |
+----------------------+----------------+------------------------------------------+
| Prompt               | Taxonomy term  | Optional prompt library item             |
+----------------------+----------------+------------------------------------------+
| Content generation   | Plain text     | Prompt used to generate AI content       |
| prompt               |                |                                          |
+----------------------+----------------+------------------------------------------+
| Body                 | WYSIWYG        | Freeform text editor field; has unlimited|
|                      | Requires 1     | cardinality to support breaking segments |
|                      |                | apart or using different AI prompts      |
+----------------------+----------------+------------------------------------------+
| Problem types        | Term reference | Tags legal resource to 0 or more problem |
|                      |                | types.                                   |
+----------------------+----------------+------------------------------------------+
| Debt types           | Term reference | Tags legal resource to 0 or more debt    |
|                      |                | types                                    |
+----------------------+----------------+------------------------------------------+
| General information  | Term reference | Tags legal resource to 0 or more         |
| categories           |                | general information categories           |
+----------------------+----------------+------------------------------------------+
| Required ALL         | Term reference | Term reference to the profile problem    |
| Metadata             |                | metadata; see metadata below             |
+----------------------+----------------+------------------------------------------+
| Required ANY         | Term reference | Term reference to the profile problem    |
| Metadata             |                | metadata; see metadata below             |
+----------------------+----------------+------------------------------------------+
| Match settings       | Plain text;    | Readable summary of the required ALL and |
|                      | read only      | ANY metadata; see metadata below         |
+----------------------+----------------+------------------------------------------+
| Image                | Media (image)  | Adds an image that will be used auto-    |
|                      | Required       | matically in social media sharing        |
+----------------------+----------------+------------------------------------------+
| Jurisdiction         | Coverage area  | Allows resource to be tagged to 1 or more|
|                      | Required       | states, counties, cities, or zip codes   |
|                      |                | to indicate that the location            |
+----------------------+----------------+------------------------------------------+
| Negate jurisdiction  | Coverage area  | Allows resource to be essentially        |
|                      | Optional       | untagged to a location                   |
+----------------------+----------------+------------------------------------------+
| Last revised         | Date           | Allows content author to update date     |
|                      |                | when substantive changes made            |
+----------------------+----------------+------------------------------------------+
| Airtable ID          | Read only      | Tags a legal resource to a specific      |
|                      |                | Airtable entity                          |
+----------------------+----------------+------------------------------------------+


.. note:: Jurisdiction should be set to Illinois unless it applies to less than the state. For content that applies everywhere but Cook county or Chicago, the best approach is to set jurisdiction to Illinois and use negate jurisdiction to exclude Cook County or the city of Chicago.


Content formats
------------------
The currently supported content formats are:

* Article, for most text-based information
* Tool, for interactive content and similar
* Consequences, for articles related to "What if I lose?"
* Referral, for articles that serve as referrals to legal organizations outside of OTIS

Metadata conditions
----------------------

An article will match a user's specific debt journey when their problem profile OR debt entity:

* Matches on EVERY term in the Required ALL metadata, when at least one is selected; when left blank, it will never match.
* Matches on AT LEAST on of any Required ANY metadata, when at least one is selected; when left blank, it will never match
* Matches on any selected debt type
* Matches on any selected problem type

Examples
^^^^^^^^^^^^

**Article A has required metadata of is_debt_collector, is_wrong_venue; has required any metadata of is_600_of_fpg, is_300_of_fpg, debt type(s) of credit card, medical debt and problem type of "I'm being sued on a debt"**

User A's profile has:

* is_debt_collector = Y
* is_wrong_venue = Y
* is_600_of_fpg = N
* is 300_of_fpg = Y
* debt type = credit card debt
* problem type = "I'm being sued on a debt"

The article WOULD BE returned for this user; it matches on both required ALL and at least one of the required ANY and on the debt type and problem type.

User A's profile has:

* is_debt_collector = Y
* is_wrong_venue = N
* is_600_of_fpg = N
* is 300_of_fpg = Y
* debt type = credit card debt
* problem type = "I'm being sued on a debt"

The article WOULD NOT BE returned for this user because it failed the Required All metadata.

User A's profile has:

* is_debt_collector = Y
* is_wrong_venue = Y
* is_600_of_fpg = N
* is 300_of_fpg = N
* debt type = credit card debt
* problem type = "I'm being sued on a debt"

The article WOULD NOT BE returned for this user because it failed the Required ANY metadata.

**Article B has no required metadata and no required ANY metadata debt type(s) of credit card, medical debt and problem type of "I'm being sued on a debt"**


The article WOULD:

* Be returned when the user has no defined profile metadata and matches on debt type and problem type

* Never be returned when the user has any defined profile metadata

**Article C has all options selected for the required metadata and no required ANY metadata debt type(s) of credit card, medical debt and problem type of "I'm being sued on a debt"**


The article WOULD:

* Be returned when the user has no defined profile metadata and matches on debt type and problem type

* Never be returned when the user has any defined profile metadata because it would always fail on the ANY required metadata

**Article D has all options selected for the required metadata and all required ANY metadata debt type(s) of credit card, medical debt and problem type of "I'm being sued on a debt"**


The article WOULD:

* Be returned when the user has every defined profile metadata and matches on debt type and problem type

* Never be returned when the user is missing any defined profile metadata because it would always fail on the ALL required metadata

**Article E has no options selected for the required metadata and all required ANY metadata debt type(s) of credit card, medical debt and problem type of "I'm being sued on a debt"**


The article WOULD:

* Be returned when the user has every defined profile metadata and matches on debt type and problem type

* Never be returned when the user is missing any defined profile metadata because it would always fail on the ALL required metadata as none is selected.

Did you know snippets
========================

Did you know snippets are a custom block type. These blocks include:

* Name
* Message
* Problem type
* Debt type

These can be then placed on any page of the site by users with the content author role.

They can also be called via API and used in middleware.


Options
==========

Options are specifically formatted content types.

+----------------------+----------------+------------------------------------------+
| Field                | Type           | Description                              |
+======================+================+==========================================+
| Title                | String (short) | Title of the resource                    |
|                      | Required       |                                          |
+----------------------+----------------+------------------------------------------+
| Description          | String (long)  | Description for use in social media and  |
|                      | Required       | on site listings / search                |
+----------------------+----------------+------------------------------------------+
| Overview             | Paragraphs     | Paragraph entity of type "Option         |
|                      | Required       | overview" (see below)                    |
+----------------------+----------------+------------------------------------------+
| Steps                | Paragraphs     | Paragraph entity of Option step (below)  |
|                      | Required       |                                          |
+----------------------+----------------+------------------------------------------+
| Eligibility questions| String (short) | TBD; this may be a URL or an id          |
+----------------------+----------------+------------------------------------------+
| Eligibility          | String (long)  | Plain text field for evaluative criteria |
+----------------------+----------------+------------------------------------------+
| Jurisdiction         | Coverage area  | Allows resource to be tagged to 1 or more|
|                      | Required       | states, counties, cities, or zip codes   |
|                      |                | to indicate that the location            |
+----------------------+----------------+------------------------------------------+
| Negate jurisdiction  | Coverage area  | Allows resource to be essentially        |
|                      | Optional       | untagged to a location                   |
+----------------------+----------------+------------------------------------------+
| Last revised         | Date           | Allows content author to update date     |
|                      |                | when substantive changes made            |
+----------------------+----------------+------------------------------------------+
| Problem types        | Term reference | Tags legal resource to 0 or more problem |
|                      |                | types.                                   |
+----------------------+----------------+------------------------------------------+
| Debt types           | Term reference | Tags legal resource to 0 or more debt    |
|                      |                | types                                    |
+----------------------+----------------+------------------------------------------+

Overview
------------

This would be a paragraphs bundle with a cardinality of 1.

+----------------------+----------------+------------------------------------------+
| Field                | Type           | Description                              |
+======================+================+==========================================+
| Overview             | WYSIWYG        | Overview text                            |
|                      | Required       |                                          |
+----------------------+----------------+------------------------------------------+
| Pros Label           | Text           | Heading label for the pros section, if   |
|                      |                | exists                                   |
+----------------------+----------------+------------------------------------------+
| Pros                 | WYSIWYG        | Parapgraph for pros narrative            |
+----------------------+----------------+------------------------------------------+
| Cons Label           | Text           | Heading label for the cons section, if   |
|                      |                | exists                                   |
+----------------------+----------------+------------------------------------------+
| Cons                 | WYSIWYG        | Parapgraph for cons narrative            |
+----------------------+----------------+------------------------------------------+

Steps
---------
This would mirror the process step bundle on IllinoisLegalAid.org. The Steps field should have a cardinality of unlimited

+----------------------+----------------+------------------------------------------+
| Field                | Type           | Description                              |
+======================+================+==========================================+
| Step title           | Text (plain)   | Heading for the step                     |
|                      | Required       |                                          |
+----------------------+----------------+------------------------------------------+
| Body                 | WYSIWYG        | Body of the step                         |
+----------------------+----------------+------------------------------------------+

Basic pages
===============

FAQs
=======


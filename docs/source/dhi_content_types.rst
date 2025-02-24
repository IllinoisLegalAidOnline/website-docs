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
| Prompt               | Taxonomy term  | Optional prompt library item             |
+----------------------+----------------+------------------------------------------+
| Content generation   | Plain text     | Prompt used to generate AI content       |
| prompt               |                |                                          |
+----------------------+----------------+------------------------------------------+
| Eligibility questions| String (short) | TBD; this may be a URL or an id          |
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

.. note:: Need to remove eligibility field as it is replaced with the required all/any fields.

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
|                      |                | exists; defaults to "Pros"               |
+----------------------+----------------+------------------------------------------+
| Pros                 | WYSIWYG        | Parapgraph for pros narrative            |
+----------------------+----------------+------------------------------------------+
| Cons Label           | Text           | Heading label for the cons section, if   |
|                      |                | exists; defaults to "Cons"               |
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

Basic pages are used for the About section, user guide, and other similar static pages.

.. note:: Need to add a description field. May need to add a media/text story.

FAQs
=======

FAQs are simple pages that are are designed for a single question / answer as part of the website FAQs

+----------------------+----------------+------------------------------------------+
| Field                | Type           | Description                              |
+======================+================+==========================================+
| Title                | Text (plain)   | Question for the FAQ                     |
|                      | Required       |                                          |
+----------------------+----------------+------------------------------------------+
| Body                 | WYSIWYG        | Answer text / body                       |
+----------------------+----------------+------------------------------------------+
| FAQ weight           | Integer        | Used to order FAQs on a page; higher     |
|                      |                | values will appear first                 |
+----------------------+----------------+------------------------------------------+


Summary Templates
=====================

Summary templates are used to provide a recap of the information a user has provided into a narrative format that then is displayed on their summary and next steps page.

.. note:: At this stage, summary templates are limited only to debt and problem type.

----------------------+----------------+------------------------------------------+
| Field                | Type           | Description                              |
+======================+================+==========================================+
| Title                | Text (plain)   | Title / descriptor of template           |
|                      | Required       |                                          |
+----------------------+----------------+------------------------------------------+
| Body                 | WYSIWYG        | Answer text / body                       |
+----------------------+----------------+------------------------------------------+
| Debt type            | Term reference | Unlimited reference to debt types        |
+----------------------+----------------+------------------------------------------+
| Problem type         | Term reference | Unlimited reference to problem types     |
+----------------------+----------------+------------------------------------------+


Metadata conditions
=======================
Metadata conditions are used in legal resources and legal options.


An item will match a user's specific debt journey when their problem profile OR debt entity:

* Matches on EVERY term in the Required ALL metadata, when at least one is selected; when left blank, it will never match unless the Ignore empty all metadata box is checked
* Matches on AT LEAST on of any Required ANY metadata, when at least one is selected; when left blank, it will never match unless the Ignore empty any metadata box is checked
* Matches on any selected debt type
* Matches on any selected problem type

Examples
------------

Article A
^^^^^^^^^^^^^
Article A has required metadata of is_debt_collector, is_wrong_venue; has required any metadata of is_600_of_fpg, is_300_of_fpg, debt type(s) of credit card, medical debt and problem type of "I'm being sued on a debt"

User 1's profile has:

* is_debt_collector = Y
* is_wrong_venue = Y
* is_600_of_fpg = N
* is 300_of_fpg = Y
* debt type = credit card debt
* problem type = "I'm being sued on a debt"

The article WOULD BE returned for this user; it matches on both required ALL and at least one of the required ANY and on the debt type and problem type.

User 2's profile has:

* is_debt_collector = Y
* is_wrong_venue = N
* is_600_of_fpg = N
* is 300_of_fpg = Y
* debt type = credit card debt
* problem type = "I'm being sued on a debt"

The article WOULD NOT BE returned for this user because it failed the Required All metadata.

User 3's profile has:

* is_debt_collector = Y
* is_wrong_venue = Y
* is_600_of_fpg = N
* is 300_of_fpg = N
* debt type = credit card debt
* problem type = "I'm being sued on a debt"

The article WOULD NOT BE returned for this user because it failed the Required ANY metadata.

Article B
^^^^^^^^^^^
Article B has required ALL metadata of is_wrong_venue, a debt type of Credit card debt, and a problem type of I'm being sued on a debt. It has nothing marked for any metadata.

User 1's profile:

* is_debt_collector = Y
* is_wrong_venue = Y
* is_600_of_fpg = N
* is 300_of_fpg = Y
* debt type = credit card debt
* problem type = "I'm being sued on a debt

This article would be returned if the Ignore empty Any metadata was checked because only the "is_wrong_venue" and debt type and problem type would be required.

User 2's profile:

* debt type = credit card debt
* problem type = "I'm being sued on a debt
* has no other metadata

This article would never be returned because is_wrong_venue is not defined.

Article C
^^^^^^^^^^^^^
Article B has a debt type of Credit card debt, and a problem type of I'm being sued on a debt. It has nothing marked for the ANY metadata and nothing marked for the ALL metadata.

User 1's profile:

* is_debt_collector = Y
* is_wrong_venue = Y
* is_600_of_fpg = N
* is 300_of_fpg = Y
* debt type = credit card debt
* problem type = "I'm being sued on a debt

This article would be returned if the Ignore empty Any metadata and Ignore empty ALL metadata was checked because only debt type and problem type would be required.

It would not be returned if the ignore boxes were not checked.

User 2's profile:

* debt type = credit card debt
* problem type = "I'm being sued on a debt
* has no other metadata

This article would always be returned because it matches on debt type, problem type, and there is no metadata collected.



Block Types
===============

Did you know snippets
-------------------------

Did you know snippets are a custom block type. These blocks include:

* Name
* Message
* Problem type
* Debt type

These can be then placed on any page of the site by users with the content author role.

They can also be called via API and used in middleware.
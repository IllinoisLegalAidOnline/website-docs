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
| Content format       | Select one     | Type of content - tool, article. Types   |
|                      | Required       | may be expanded over time                |
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

.. note:: Jurisdiction should be set to Illinois unless it applies to less than the state. For content that applies everywhere but Cook county or Chicago, the best approach is to set jurisdiction to Illinois and use negate jurisdiction to exclude Cook County or the city of Chicago.

.. todo:: We will be incorporating AI tools to generate the body field(s) based on prompts and content derived from ILAO content and other trusted resources.


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

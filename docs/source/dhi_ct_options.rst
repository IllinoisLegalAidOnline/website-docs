=====================
DHI Options
=====================


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
============

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
=========
This would mirror the process step bundle on IllinoisLegalAid.org. The Steps field should have a cardinality of unlimited

+----------------------+----------------+------------------------------------------+
| Field                | Type           | Description                              |
+======================+================+==========================================+
| Step title           | Text (plain)   | Heading for the step                     |
|                      | Required       |                                          |
+----------------------+----------------+------------------------------------------+
| Body                 | WYSIWYG        | Body of the step                         |
+----------------------+----------------+------------------------------------------+


=======================
DHI Legal Resources
=======================


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
| Disambiguation       | String (short) | Used to keep similarly titled content    |
| Description          |                | organized and findable in the CMS        |
+----------------------+----------------+------------------------------------------+
| Description          | String (long)  | Description for use in social media and  |
|                      | Required       | on site listings / search                |
+----------------------+----------------+------------------------------------------+
| Content format       | Select one     | Type of content                          |
+----------------------+----------------+------------------------------------------+
| Prompt               | Taxonomy term  | Optional prompt library item             |
+----------------------+----------------+------------------------------------------+
| Length: word count   | Number         | Provides guidance to AI in generating    |
|                      |                | the content                              |
+----------------------+----------------+------------------------------------------+
| Content generation   | Plain text     | Prompt used to generate AI content       |
| prompt               |                |                                          |
+----------------------+----------------+------------------------------------------+
| Generated text       | Plain text     | AI generated content for drafting        |
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
| Required ALL         | Term reference | Term reference to the profile problem    |
| Metadata             |                | metadata; see metadata below             |
+----------------------+----------------+------------------------------------------+
| Required ANY         | Term reference | Term reference to the profile problem    |
| Metadata             |                | metadata; see metadata below             |
+----------------------+----------------+------------------------------------------+
| Match settings       | Plain text;    | Readable summary of the required ALL and |
|                      | read only      | ANY metadata; see metadata below         |
+----------------------+----------------+------------------------------------------+
| External source      | WYSIWYG        | Allows us to record where information    |
| material             |                | came from                                |
+----------------------+----------------+------------------------------------------+
| Last revised         | Date           | Allows content author to update date     |
|                      |                | when substantive changes made            |
+----------------------+----------------+------------------------------------------+
| Airtable ID          | Read only      | Tags a legal resource to a specific      |
|                      |                | Airtable entity                          |
+----------------------+----------------+------------------------------------------+
| Relevancy score      | Read only      | Assigns a relevancy score for ordering   |
|                      |                | legal resources on the debt summmary     |
+----------------------+----------------+------------------------------------------+

These fields appear only when the content format is set to tool:

+----------------------+----------------+------------------------------------------+
| Landbot url          | Short text     | For tools only, the landbot url to embed |
+----------------------+----------------+------------------------------------------+
| Entity field         | Select         | The entity and field the tool data is    |
|                      |                | attached to                              |
+----------------------+----------------+------------------------------------------+
| Text when tool is    | WYSIWYG        | Stores text to include when the tool is  |
| complete/has data    |                | complete and there is data stored        |
+----------------------+----------------+------------------------------------------+
| Text when tool is    | WYSIWYG        | Stores text to include when the tool is  |
| complete/no  data    |                | complete and there is no data stored     |
+----------------------+----------------+------------------------------------------+
| Text when tool is    | WYSIWYG        | Stores text to include when the tool is  |
| not complete         |                | not complete                             |
+----------------------+----------------+------------------------------------------+


Content formats
=================
The currently supported content formats are:

* Article, for most text-based information
* Tool, for interactive content and similar
* Consequences, for articles related to "What if I lose?"
* Referral, for articles that serve as referrals to legal organizations outside of OTIS


Tool fields
==============
Tools are built in landbot and return metadata that is attached to a specific field. Each tool has additional fields

* Landbot url - The url to embed
* Entity field - the entity field the results are attached to. **These must be created before the tool is created**
* Text when the tool has been completed and there is data. If the user is collection proof or has claims, for example, there will be data stored.
* Text when the tool has been completed and there is no data. If the user is not collection proof or has no claims, for example, the tool will be marked complete but there will be no metadata saved.
* Text when the tool has not been completed

Jurisdiction
================
Jurisdiction should be set to Illinois unless it applies to less than the state. For content that applies everywhere but Cook county or Chicago, the best approach is to set jurisdiction to Illinois and use negate jurisdiction to exclude Cook County or the city of Chicago. **At this point, jurisdiction is only used for referrals**.

Relevancy score
=================
Relevancy score defaults to 1000 for legal resources if there are no required ALL metadata selected and no required ANY metadata required. 

If either field has data, then the score is set to the total of:

* Number of ALL required metadata selected. Each required metadata is assigned 1 point.
* Number of ANY required metadata selected. Each required metadata is assigned 2 points.

.. note:: For example, 

   * article A has 2 required All metadata and 0 Any metadata, it’s score would be 2
   * article B has 0 required all metadata and 0 required any metadata, it’s score would be 1000
   * article C has 0 required All metadata and 2 required Any metadata. It’s score would be 4 (2 * 2)
   * article D has 2 required All metadata and 2 required any metadata; it’s score would be  6 (2 + 2*.2)
   
   When viewed on the debt summary page, the articles would be ordered as A, C, D, B. 




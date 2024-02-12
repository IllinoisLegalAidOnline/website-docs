==========================
Legal content reporting
==========================

.. warning:: This section is very out of date.

Available reports:

* `Content main report (all content) <https://www.illinoislegalaid.org/admin/content>`_
* `Find legal content report <https://www.illinoislegalaid.org/admin/reporting/content/legal-content>`_
* `Learn more in Guides report <https://www.illinoislegalaid.org/admin/reporting/content/guides/learn-more>`_
* `Take action in Guides report <illinoislegalaid.org/admin/reporting/content/guides/take-action>`_
* `Toolbox tool usage report <https://www.illinoislegalaid.org/admin/reporting/content/toolboxes/tool-usage>`_
* `Toolbox tool step usage report <https://www.illinoislegalaid.org/admin/reporting/content/toolboxes/tool-usage>`_
* `Content page views report (basic) <https://www.illinoislegalaid.org/admin/reporting/content-page-views>`_
* `Historical review/revised date data <https://www.illinoislegalaid.org/admin/reporting/content/legal-revisions>`_
* `Last revision report <https://www.illinoislegalaid.org/admin/content/last-revision-report>`_
* `Last SME review report <https://www.illinoislegalaid.org/admin/content/last-sme-review>`_
* `Localized content report <https://www.illinoislegalaid.org/admin/reporting/content/localized-content>`_


Main content report
=====================
This is the basic Drupal report for content. It includes all available content types.

Report data
---------------
The report includes:

* the ID (node ID)
* the title
* the content type
* the format (this applies only to legal content)
* the author
* the date published (this is the created date unless manually changed)
* the last updated date. This is the system date. For legal content specific dates, use the find legal content report.

Filters
-----------
This report can be filtered on:

* node ID. This will return a specific node.
* Title (contains)
* Content type (this is the system content type like legal content, event, basic page)
* Published status (yes or no)
* Translation language. Using this will filter out translations for the same node.


Bulk actions
---------------
This is the system set of actions that can be applied to content. Some of these are not relevant.

* Delete content  **Be careful** this will in fact delete selected content.
* Save content. This will re-save content and update the last updated/changed date.
* Publish content. This will publish unpublished content AND update the last updated/changed date. It will not move legal content revisions that is under moderation from an unpublished state like draft/revise to published.
* Unpublish content. This will unpublish published content and update the last updated/changed date.
* Update URL alias. **Use only if Gwen tells you to**  This will reset path aliases. This is helpful for some content types **other than legal content.**

.. todo:: Update the action list to only relevant items.


Legal content report
======================
Includes the following content types:

* Legal content
* ADRM content
* Portal content
* Toolboxes
* Toolbox tools
* Tool steps

Report data
-----------------

* Node ID (ID) of the content
* Title of the content
* Format of the content. Applies only to legal content.
* Primary legal category of the content.
* Created date. This is the date the system creates when the node is first created in any state. It does not necessarily represent published date.
* Original author
* Last changed. This is the date the system last recorded a change. This is triggered whenever:

  * A user saves the node
  * A system update saves the node. This may happen if there is a scheduled change, Google analytics data added, or any other system action that causes a call to the node save function.

* Last revised. This is the "last internal revision" field. This date is manually sent when a staff user makes a substantive change to the content. Does not include typos, grammatical fixes, or style changes. Does include anything that adds or removes information, especially law changes.
* Last expert review.
* Published status (Yes or No)
* Language of the node (content in more than one language will have multiple rows in the report)
* Page views from Google analytics. These are pulled in from the English content and associated with the node (so it will show the same page views on Spanish and Polish versions). These are pulled in as a scheduled task in batches and are based on the last 60 days +/- 14 days depending on when it was last imported. **This was added to aid in prioritization not as a 100% accurate measure**
* Word count. The number of words in the node (see :ref:`word-count-label`)

.. note::  The last revised and last expert review fields are not translatable in legal content but are translatable in toolbox, tool, and tool step content.   The last changed date is per language.

.. todo:: standardize date fields (translatable vs not translatable)


Filters
--------------
The find legal content report has many filters. Filters are based on an AND condition.

* ID is the node ID
* Title is the partial match of the title
* Category is the primary legal category for the content. This is the single select dropdown for category versus the legal issues multiple-select field.
* Published status (yes or no). Note that publish status is per node. An unpublished translation in Spanish with a published English version would show as published.
* Content format. This applies to legal content only and is set based on the paragraphs bundles included in the node.
* Created filters on the created date and can be set with a start date and/or end date
* Last revised filters on the last internal revision date and can be set with a start date and/or end date
* Last expert review filters on the last expert review date and can be set with a start date and/or end date
* Level (basic or advanced)
* Legal position
* Restrict (whether content is marked as restricted to legal aid or pro bono members)
* Jurisdiction (whether content is marked as national, statewide or relevant only to specific counties or cities) and to what counties, cities, or zip codes the content is tagged. Applies only to legal content type content.
* Annual updates tagged to the content  Applies only to legal content type content and ADRM content.
* Whether the translation is currently marked as outdated
* Whether there is an open request to create a translation. This field applies only to legal content.
* Translation language. This should be used to limit the list to English, Spanish or Polish.
* Content management tags. This should be used to limit the results to those that have a term from the content management tags taxonomy. Separate terms by commas.
* Legal issue. This is a single autocomplete of the legal issues taxonomy. Filtering on this will include any content tagged to that term or any child term, if a child term exists.

.. note:: because of the way jurisdictions were handled on the D7 site, the counties, cities and zipcodes show what jurisdictions the content is tagged to but the report **does not show** whether the relationship between the jurisdiction (some part of Illinois) includes or excludes the jurisdictions. The jurisdiction data is not used in any way on the website's front-end.

.. todo:: Determine whether toolbox and portal content should have translation fields.

Learn more in Guide report
============================

This report shows all of the articles that are included in a Guide and listed under Learn More. This report shows English language only. If a translation does not exist for a Learn More article, the English article will be listed in Spanish and Polish.

The report is exportable to CSV and includes:
* the ID of the guide
* the title of the guide
* the title of the learn more article
* the ID of the learn more article

All four fields are available as filters.

Take action in Guide report
============================

This report shows all of the articles that are included in a Guide and listed under Take action. This report shows English language only. If a translation does not exist for a Take action article, the English article will be listed in Spanish and Polish.

The report is exportable to CSV and includes:
* the ID of the guide
* the title of the guide
* the title of the take action article
* the ID of the take action article

All four fields are available as filters.

Toolbox Tool report
======================

The toolbox tool displays data captured as users interact with a toolbox tool. The fields included are:

* Toolbox ID - this is the unique ID associated with a toolbox user's interaction. If they are logged in and return to a tool, this ID is re-used, allowing us to track a user over time. Anonymous users do not have activity tracked over time.
* User ID - this is the user's id from our website. User ID 0 is an anonymous user.
* Toolbox title - title of the toolbox the tool is a part of
* Toolbox tool title - title of the toolbox tool the user is working on
* Started - timestamp of when the record was created
* Last activity - timestamp of the last recorded interaction
* Status - started, saved, or completed. Started means the user started the tool but has not yet saved any steps; completed means they marked the tool complete and saved means they've marked at least one step complete.


.. warning:: Data from before June 24, 2020 is not reliable. The last activity date was updated for the time of migration and changes to the toolbox platform changed the way the toolbox activity works.

Toolbox Tool Usage report
==========================

The toolbox tool displays data captured as users interact with the steps in a toolbox tool. The fields included are:

* Toolbox ID - this is the unique ID associated with a toolbox user's interaction. If they are logged in and return to a tool, this ID is re-used, allowing us to track a user over time. Anonymous users do not have activity tracked over time.
* Toolbox usage id - this is the unique ID for the specific interaction
* User ID - this is the user's id from our website. User ID 0 is an anonymous user.
* Toolbox tool title - title of the toolbox tool the user is working on
* Tool step title - title of the step
* Started - timestamp of when the record was created
* Changed - timestamp of the last recorded interaction
* Status - started, saved, or completed. Started means the user viewed the tool step;saved means they've marked the step complete and complete means they've completed all the applicable steps in a tool.


.. warning:: Data from before June 24, 2020 is not reliable. The last activity date was updated for the time of migration and changes to the toolbox platform changed the way the toolbox activity works.

Content page views report
===========================

This is a basic report to support A/B testing based on the page views stored from Google Analytics that are used to sort category pages. The report includes:

* a row number; when exported to excel, a formula of =mod(a2,2) will return a 1 or 0 based on whether the row number is even or odd, allowing it to be split.
* the content title
* the page views
* the unaliased path; this can be dropped into block configuration to cause a block to display on those pages.

Localized content report
=========================

This report shows what legal content contains markup for localized content. At this point, it can only show that it contains the span| markup used in localized content.


The list can be exported to CSV.

.. todo::
   Explore if we can expose the field filters to allow for searching on span|County|[values] for example to support better filtering.

Comments and Ratings report
===========================

This report lists  all of the comments and associated ratings for legal content. The report includes:

* Node ID
* Content title
* Total rating, with average and count, for the content
* Comment
* Comment author
* Individual rating associated with the comment

The report has filters for:

* Content title
* Node ID
* Whether to exclude staff comments or not

.. note:: The "hide staff users" requires that the user have the staff role. If former staff have been left active but had the staff role removed, they will not be filtered out. The better practice for former staff is to block their account but leave their permission in place.

.. warning:: On revision reports, revisions are not separatable by language.

Historical Revision report
===============================

This report should be used only to track date fields over time. It's primary purpose is to pull data for reports where we need to report on internal revisions and expert reviews from a given time period and that data is not reflected in the current revision because the content was later revised/reviewed.

.. note::  For data before May 24, 2020:

   * Content revisions were handled differently in that each unpublished change was within a single revision.
   * Language management was handled differently; it is impossible to sort by language on older revisions.
   * All legal content was set with a last internal revision date of 5/24/2020 when it was migrated over.

.. note:: For data after May 24, 2020:

   * ADRM (lawyer manual) content did not have the internal revision/expert review fields until recently.
   * Older toolbox tools do not have an internal revision or expert review dates because they did not exist on the old website.
   * Language filtering does not work because the date fields are not translatable on legal content. That means that an edit to the Spanish or Polish version will still have an English field revision causing every revision to be displayed. That is why this report should be limited to date field tracking.


Last Revision report
======================

The last revision report shows all revisions where the last revision date field has been changed.

The report includes:

* Title
* Last revision date associated with the specific revision
* Revision author
* Node ID as ID
* Revision log message (this may be used to help filter by language)
* Revision ID
* The type of content. Only Legal Content, Portal Main Page, Toolbox, Toolbox Tool Step, and Toolbox Tool are included.


.. note:: Depending on how quickly a user saves the revision, it is possible to have multiple revisions close together. For reporting, the best option is to export the date range you need and de-duplicate on node ID (ID) and the last revision date.


Last SME Review report
=======================

The last SME report shows all revisions where the last reviewed date field has been changed.

The report includes:

* Title
* Last reviewed date associated with the specific revision
* Revision author
* Node ID as ID
* Revision log message (this may be used to help filter by language)
* Revision ID
* The type of content. Only Legal Content, Portal Main Page, Toolbox, Toolbox Tool Step, and Toolbox Tool are included.


.. note:: Depending on how quickly a user saves the revision, it is possible to have multiple revisions close together. For reporting, the best option is to export the date range you need and de-duplicate on node ID (ID) and the last revision date.

Moderated content report
===========================
This is a system report accessible from the main content report. It needs review.


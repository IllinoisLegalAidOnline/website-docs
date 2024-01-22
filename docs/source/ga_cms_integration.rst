======================================
Legal content CMS data for integration
======================================

To leverage our Google Analytics 4 data, we have a Tableau table that contains legal content metadata.


The required dataset includes:

* An export of the Find Legal Content report
* An export of the Navigational IA export (for second level categories)
* An export of the Legal Issues IA export (for top level categories)
* An export of the content formats taxonomy


.. note:: The exported taxonomy tables are required to combine and label taxonomy terms in English regardless of the content language.

When run through the Tableau prep builder, this results in a CSV file with the following fields:

* ID (node ID)
* Category
* Subcategory
* Title
* Content type (Legal content, ADRM, Portal Main Page, etc)
* Created (date)
* Last Changed (last changed by the system)
* Last Revised (last revised by staff)
* Last expert review (last SME review)
* Language
* Word count (where available)
* Link to content (full url)
* Content level (basic or advanced)
* Content format (applies only to legal content)
* Page path (url minus the domain)



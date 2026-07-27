==========================
Glossary / Glossify
==========================

.. note:: In general practice, we are not using Glossify in new legal content or when revising existing content due to translation and usability issues on IllinoisLegalAid.org. It is used on DebtHelpIllinois.org


ILAO uses the Glossify module to add glossary terms to content.

This module adds links and tooltips to content and:

* Ignores H1, H2, H3, H4, and H5 elements
* Applies to the first match in a WYSIWYG field. This may result in the same term being linked to in a page where the page contains multiple WYSIWYG fields.
* Uses the Glossary taxonomy to identify glossary terms


To exclude text from being linked to
=======================================

Option 1: Set the text format for an entire section to "Full text without Glossify." This will prevent glossify from being applied to the entire block of text.

Option 2: Exclude a specific segment

* Switch to the source view in the WYSIWYG
* Wrap the text in the tags below:

.. code:: html
   
   <span class="glossify-exclude">TERM</span>

.. note:: 
   To add or edit glossary terms, edit the `Glossary taxonomy <https://www.illinoislegalaid.org/admin/structure/taxonomy/manage/glossary/overview>`_.





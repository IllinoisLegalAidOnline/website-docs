==========================
Glossary / Glossify
==========================

ILAO uses the Glossify module to add glossary terms to content.

This module adds links and tooltips to content and:

* Ignores H1, H2, H3, H4, and H5 elements
* Applies to the first match in a WYSIWYG field. This may result in the same term being linked to in a page where the page contains multiple WYSIWYG fields.
* Uses the Glossary taxonomy to identify glossary terms


To exclude text from being linked to:

* Switch to the source view in the WYSIWYG
* Wrap the text in the tags below:

.. code:: html
   
   <span class="glossify-exclude">TERM</span>

To add or edit glossary terms, edit the `Glossary taxonomy <https://www.illinoislegalaid.org/admin/structure/taxonomy/manage/glossary/overview>`_.

.. note:: The glossary taxonomy has not been actively used in a long time. The Spanish terms can likely be deleted as those are managed via Motionpoint translation. The glossary linked to on the menu is a basic page that was created to have a link to a glossary and the two may be out of sync. We need to replace this page with a Glossary view in the future.



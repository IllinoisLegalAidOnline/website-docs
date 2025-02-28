===============================
Tagging for Motionpoint
===============================

In content
================

In content, we sometimes have strings that we do not want to have Motionpoint change. The most common use case is in Easy Forms where we want the English title to appear next to the translated Spanish title.


To tag content
=================
To tell Motionpoint to ignore text, go into the source view and wrap the text in a span class of Spanish. 

.. code:: html

   <span class="Spanish">The text you want ignored</span>
   
Content in the Span class:

* Will not show on the front end of IllinoisLegalAid.org
* Will appear in the WYSIYWYG field
* Will appear as is on the Spanish website
* Will be replaced with the appropriate Motionpoint Directive Tags (DT). See below for the resulting HTML that will be shown in the "View source" in the browser on the front-end.

.. code:: html

   <!-- mp_trans_disable_start -->
   <!-- mp_trans_add
     <span>The text you want ignored</span> -->
    <!-- mp_trans_disable_end --> “

.. todo:: We need to fix the button to apply the class automatically. It works but it leaves the original text. For example, if I want to wrap "This text" in the class, in source, when I press the code button, it results in This text <span class="Spanish">This text</span>; it would be helpful too if the Ckeditor showed a distinction.


In blocks, views and other components
========================================

There are a few instances where we do not want something to appear on the Spanish site or want something that isn't content to appear on the Spanish site.

Examples:

* Removing the Ask ILAO search from Spanish
* Displaying the Spanish Vertex search on Spanish

For these cases, please see Gwen or Mike; the developers will need to implement the blocks to accommodate.

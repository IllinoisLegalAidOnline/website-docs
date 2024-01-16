=================
Buttons
=================

Button styles
==============


Button classes
===============


.. note::  Hyperlinks in legal content even when styled with the button class are showing the wrong link color; they should be white for primary and secondary links. 

Primary
---------

The primary CTA button is the bright blue button with white text. It can be added in the WYSIWYG using the class name "cta-primary"

.. code-block:: HTML

  <a href="#" class="cta-primary">Primary CTA</a>

 
Use for:

 * Buttons that serve as the primary call to action for a page.
 * Submit button for forms

Do not use:

 * On about pages, except when it is the primary call to action. For example, on the why donate page, the donate button is the primary call to action and Learn more about connector's circle or other ways to give should be secondary buttons. **In most cases, the secondary or tertiary buttons should be used.**
 * Within legal content 

Secondary
--------------
The secondary CTA button is the dark blue button with white text. It can be added in the WYSIWYG using the class name "cta-secondary"

.. code-block:: HTML

  <a href="#" class="cta-secondary">Secondary CTA</a>
  <a href="#" class="cta-secondary" style="color:white">Secondary CTA in legal content</a>

Use for:

 *  On about pages, for important buttons where the button is not the primary CTA on the page
 * On legal content (other than toolbox, tool, tool step content), for a **primary next action** in an article that the user must take (for example, filing an answer or appearance in an article on responding to a lawsuit). 
 
   * A primary next action is usually filling out or downloading a form or other document. 
   * Legal content should never have more than one secondary button within the text. 
   * If there are more than one critical action to highlight (for example, linking to an answer and an appearance separately, use two tertiary buttons).

Do not use:

 * For form submit buttons
 * For cancel buttons
 * In toolbox, tool, and tool step content 
 * For links generally except 
 
   * in About pages in side-by-side blocks that go to an underlying child page
   * in legal content except for the above use case

 

Tertiary
-------------

The tertiary CTA button is white with a border and dark blue text. It can be added in the WYSIWYG using the class name "cta-tertiary"

.. code-block:: HTML

  <a href="#" class="cta-tertiary">Tertiary CTA</a>

Use for:

 * Cancel actions
 * When you absolutely need to use a button to direct a user to another node:
 
   * And the secondary action rule for legal content does not apply (for example linking from a Guide to a How-to) 
   * When you need to call out two actions of similar weight (for example, File divorce with kids and file divorce without kids) that would meet the secondary button rule if they were a single button




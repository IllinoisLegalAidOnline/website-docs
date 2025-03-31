===================================
User journey: Single debt results
===================================

When a user completes the diagnosis flow and are focused on a single debt, they are given a results page that contains several components.

Summary
============
The summary is based on a matching template (see TBD). The selected summary:


Consequences Article
============================

A consequences article is available when:

  * It is a legal resource
  * That is published
  * That has a content format of "Consequences"
  * Matches on debt type
  * Matches on problem type
  * Matches on any metadata
  
The title, description, and link callout text are displayed on the results page.

Referrals
==============
  
Any available referrals are displayed. A referral is defined as:

  * Legal resources
  * That are published
  * Of type "Referral"
  * that match the user's debt type, problem type, and any required metadata
  
.. note:: How do we want to handle location (do we filter on jurisdiction)? How is GLH tracked in version 1; what if there is more than 1 matching?

The title, description, and link callout text are displayed on the results page. The link callout is styled as a button.


Options
============

Options are selected based on the following:

  * They are published
  * The are of type "Options"
  * They match on debt type
  * They match on problem type
  * They match on defined metadata
  
An icon, title, description are displayed on the results page. Clicking on the title or card opens the option as an overlay.

.. note:: How do we want options to be ordered? Where are icons coming form?

Legal resources
================

Additional content resources are provided when available.

Legal resources are available when:

  * It is a legal resource
  * That is published
  * Has a content format of "Article" or "Tool"
  * Matches on debt type
  * Matches on problem type
  * Matches on any metadata
  * Is not tagged to any general information terms
  
An icon, the title, description, and problem type are displayed in each card. A heart to favorite the resource is also visible. Resources are ordered:

.. note:: Resources are ordered using an algorithm that ranks most narrowly tailored to least tailored. Resrouces pinned as sticky at top of lists will appear first.

.. note:: If the user is not logged in, pressing the heart will launch the sign up modal.




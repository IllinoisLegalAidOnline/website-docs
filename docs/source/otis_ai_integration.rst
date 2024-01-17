====================
OTIS AI Integration
====================

We have access to 2 legal issue classifiers that return one or more likely legal issues.

Both produce similar results although they don't always perform evenly.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   otis_tech_houston_ai
   otis_tech_spot_classifier
   otis_natural_language_processing

Prototype
===========

The `first prototype <https://dnlmkx.axshare.com/home.html>`_ demonstrates how the classifiers might work in conjunction with our taxonomy to guide users into webform triage rules or into Guided navigation.

Walking through the prototype:  Managing the legal problem
------------------------------------------------------------

* Enter **cut in my food stamps** in the text area and click Continue to see what would happen if the user entered an exact match to ILAO's taxonomy. In this case, the user is just asked to confirm their legal issue.
* Enter **food stamps** to see one option when the classifiers do not return anything meeting our threshold. In this case, it shows all the lowest level taxonomy terms that contain the search term or whose parent contains the search term.
* Enter **snap** to see the other option when the classifiers do not return anything meeting our threshold. In this case it shows the highest level taxonomy terms that contain the search term.
* Enter **I lost my job and now am being evicted from my apartment** to see results where one or both classifiers return items. This example shows multiple relevant issues.


Guided navigation vs. Webform triage rules
--------------------------------------------
For some legal issues, we will have Guided navigation and for other issues, we will continue ot use webform triage rules.

* Enter **bills** in the legal problem text area
* Click on bankruptcy
* Click on I want to file bankruptcy
* Click No on the Do you have an open bankruptcy case
* Click on To stop a foreclosure to see what happens when a user is taken out of Guided navigation to triage rules
* Click on To stop a foreclosure of my home to see what happens when a user is taken completely through Guided navigation

One match vs Multiple
------------------------

With Guided Navigation we can handle multiple matching organizations where we can't do that with the webform triage rules.

Guided navigation: `multiple matches <https://dnlmkx.axshare.com/matches_-_multiple.html>`_


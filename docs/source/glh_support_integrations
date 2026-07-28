==========================
Supported Integrations
==========================

URL Pre-fill method
===================
This method allows for passing in query parameters in the URL to pre-fill the main Get Legal Help form. It is designed to allow for easier integration from chatbots and external services into OTIS without the user having to re-enter information.


This method supports up to 5 parameters:

* issue, which is the legal issues taxonomy term ID. ILAO will provide a list of taxonomy term IDs for interested partners of the lowest-level terms so that users bypass additional screening.
* zipcode, the user's zipcode
* household, the size of the household as a number
* source (which then requires the referral_source_type parameter
* helptype[]

  * up to 3 instances of helptype[] are allowed
  * the accepted values for these are lawyer, content, forms
  
  
Source parameters
===================

Source parameters should be matched as a pair:

* source should be either an organization id or intake_settings id
* referral_source_type should be either organization or intake_settings

When a source is included with a referral_source_type of organization, the specific organization will receive priority over any other organization. This is usually the **preferred** approach to use unless an organization needs to prioritize a specific intake setting.

When a source is included with a referral_source_type of intake_settings, the specific intake settings or organization will receive priority over any other intake settings. This is expected to be used by organization partners on their own websites or via social media to prioritize traffic from those partners into OTIS. For example, if the url is /get-legal-help?source=1226&referral_source_type=intake_settings then Legal Aid Chicago's housing rules would take priority over other organizations. 

.. note::  
   Because the source parameter is tied to the intake settings, it is best practice to include a relevant taxonomy term as the parameter will be ignored if the user selects a topic that is unrelated to the intake settings
   
   
Examples
================

When used as a link on a website or social media
--------------------------------------------------

In these examples, we are using just the source parameters to prioritize an OTIS partner.

Direct referral to Legal Aid Chicago for any legal issue:

`https://www.illinoislegalaid.org/get-legal-help?source=25231&referral_source_type=organization <https://www.illinoislegalaid.org/get-legal-help?source=25231&referral_source_type=organization>`_

Direct referral to JEP for any legal issue:

`https://www.illinoislegalaid.org/get-legal-help?source=25181&referral_source_type=organization <https://www.illinoislegalaid.org/get-legal-help?source=25181&referral_source_type=organization>`_

Direct referral to Legal Aid Chicago's housing practice group:

`https://www.illinoislegalaid.org/get-legal-help?source=1226&referral_source_type=intake_settings&helptype[]=lawyer <https://www.illinoislegalaid.org/get-legal-help?source=1226&referral_source_type=intake_settings&helptype[]=lawyer>`_

When used in a chatbot
--------------------------
In these examples, we are using the parameters to prefill the Get Legal Help form without prioritizing one organization over another.

Looking for a lawyer:
`https://www.illinoislegalaid.org/get-legal-help?issue=514616&zipcode=60603&household=3&helptype[]=lawyer <https://www.illinoislegalaid.org/get-legal-help?issue=514616&zipcode=60603&household=3&helptype[]=lawyer>`_

Looking for a lawyer & content:
`https://www.illinoislegalaid.org/get-legal-help?issue=514616&zipcode=60603&household=3&helptype[]=lawyer&helptype[]=content <https://www.illinoislegalaid.org/get-legal-help?issue=514616&zipcode=60603&household=3&helptype[]=lawyer&helptype[]=content>`_


Combining the two
--------------------

We can combine the two to pre-fill the form and prioritize an organization. This may be helpful for social media or website campaigns where an OTIS partner may want to help the user get to the right triage rules, for example, prefilling the legal issue as foreclosure to ensure that users don't search for bankruptcy when they are considering bankruptcy to prevent a foreclosure.

Looking for a lawyer for foreclosure in 60603, household size of 3 and prioritizing Legal Aid Chicago:

`https://www.illinoislegalaid.org/get-legal-help?issue=515281&zipcode=60603&household=3&helptype[]=lawyer&source=25231&referral_source_type=organization <https://www.illinoislegalaid.org/get-legal-help?issue=515281&zipcode=60603&household=3&helptype[]=lawyer&source=25231&referral_source_type=organization>`_


.. note:: Where the user still has to drill down from ILAO's taxonomy, there is a chance that the organization will be de-prioritized if the user drills down to a subtopic not covered by that organization's triage rules.


.. image::  ../assets/otis-prefill-mobile.png

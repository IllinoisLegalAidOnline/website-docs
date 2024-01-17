.. _otis-qualifiers-label:

============
Qualifiers
============

OTIS partners have the ability to ask organization or eligibility specific questions to an applicant prior to the applicant completing the intake. This allows partners to further screen an applicant and if the applicant does not fit the organization's specific criteria, the applicant can still be referred to another organization.

Where does this appear?
========================
When an OTIS applicant is matched to an organization who has additional qualifiers, the applicant will see the additional questions only if they select that organization from the list of matched organizations.

If the applicant does not qualify after the qualifiers they are returned to the match screen so they can select an different OTIS partner. If there are no more matches, the applicant is redirected to referrals.

Creating qualifers
===================

In LegalServer
---------------
Create a new guided navigation interactive dialogue. The dialogue should be named Qualifier_[short description of the qualifier] 
see :ref:`otis-guided-navigation-label` 
All steps of creating a guided navigation path must be complete (dialogue, segments, and process)

On IllinoisLegalAid.org
-------------------------
* Once the guided navigation process has been created and you have the process id, follow these steps:

  * Create a new taxonomy term under "OTIS Qualifiers"; 
  * Name the new term and fill in the Guided Navigation Process ID;
  * Go to the OTIS partner's intake setting where the qualifier will apply; and
  * Start typing the name (taxonomy term) in the Additional qualifiers section of the intake setting

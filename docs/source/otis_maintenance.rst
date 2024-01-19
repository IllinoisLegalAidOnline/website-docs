====================================
Maintaining and expanding OTIS SMS
====================================

Expanding for new legal issues
=====================================


.. toctree::
   :numbered:

   otis_maintenance_gn
   otis_maintain_case_acceptance_webform
   otis_maintenance_case_acceptance_view
   otis_maintenance_twilio
   otis_maintenance_tokens
   otis_maintenance_failures



Demographic taxonomy terms
=============================

Taxonomy terms for gender, race, ethnicity, etc, that are used in the SMS application, are stored in functions rather than pulled from the website.

Any change needs to be made in both the relevant otis-load and otis-validate functions. Each demographic term has its own pair of functions (for example, otis-load-genders and otis-validate-genders).

.. code-block:: javascript


   if (event.langcode == null || event.langcode == 'en') {
     marital.push('Single','Married','Divorced','Separated','Widowed');
     marital.push('Other', 'Prefer not to respond');
   }
   else {
    marital.push('Soltero','Casado','Divorciado','Separado','Viudo');
    marital.push('Otros', 'Prefiero no contestar');
  }


.. todo:: Replace this with API calls to the website.




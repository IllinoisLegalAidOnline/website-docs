==========================
OTIS API Related Entities
==========================

There are numerous related entities attached to triage user and intake settings entities.

These can be added via includes or accessed directly through their own API calls in the format of jsonapi/[type]/[bundle].

For example:

* /jsonapi/taxonomy_term/region/[uuid]
* /jsonapi/income_standard/income_standard/[uuid]

Triage users
==============
Triage users have the following relationships:

* user_id : the user entity of the author of the intake settings
* intake_organization: the oas_intake_setings uuid of the applicable intake settings
* oas_limited_populations: an array of type taxonomy_term--intake_populations that represents the populations selected by the user
* oas_triage_problem: the taxonomy_term from legal issues that represents the user's issue
* oas_triage_problem_history: the taxonomyt_term from legal issues that represents the user's issue, with full taxonomy path


Intake settings
================
Intake settings have the following relationships:

* user_id : the user entity of the author of the intake settings
* entity_id of type node--location_services: the service associated with the intake settings
* field_cities: an array of type taxonomy_term--region of ids from the region taxonomy that represent cities selected for use in the intake settings
* field_counties: an array of type taxonomy_term--region of ids from the region taxonomy that represent counties selected for use in the intake settings
* field_zipcodes: an array of type taxonomy_term--region of ids from the region taxonomy that represent counties selected for use in the intake settings
* field_legal_issues: an array of type taxonomy_term--legal_issues from the legal issues taxonomy that represent the legal issues associated with the intake settings
* field_oas_callback_hours_fri: an array of type taxonomy_term--oas_callback_hours that represent the callback hour slots for the intake settings on Fridays
* field_oas_callback_hours_mon: an array of type taxonomy_term--oas_callback_hours that represent the callback hour slots for the intake settings on Mondays
* field_oas_callback_hours_sat: an array of type taxonomy_term--oas_callback_hours that represent the callback hour slots for the intake settings on Saturdays
* field_oas_callback_hours_sun: an array of type taxonomy_term--oas_callback_hours that represent the callback hour slots for the intake settings on Sundays
* field_oas_callback_hours_thurs: an array of type taxonomy_term--oas_callback_hours that represent the callback hour slots for the intake settings on Fridays
* field_oas_callback_hours_tue: an array of type taxonomy_term--oas_callback_hours that represent the callback hour slots for the intake settings on Fridays
* field_oas_callback_hours_wed: an array of type taxonomy_term--oas_callback_hours that represent the callback hour slots for the intake settings on Fridays
* oas_asset_catagories
* oas_expense_categories
* oas_income_categories: an array of type ilao_oas_financial_category--income_type that represent the financial category entities of type income to collect.
* oas_income_exempt: an array of type taxonomy_term--intake_populations that represents user populations that should be exempt from income limits
* oas_income_standard: an array of type income_standard--income_standard that represents the entity id of the income standard to apply if needed



.. note:: Only one of the field_cities, field_counties, and field_zipcodes will have actual data.

Example cUrl call for taxonomy term
=====================================

.. code-block:: html

   curl -X GET -H "Content-Type:application/vnd.api+json" http://ilaodrupal8.prod.dd:8083/jsonapi/taxonomy_term/region



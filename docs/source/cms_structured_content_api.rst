===========================
Structured content API
===========================

The structured content API relies on Drupal's JSONAPI.  For information on interacting with that generally, see the `Drupal Documentation <https://www.drupal.org/docs/core-modules-and-themes/core-modules/jsonapi-module/api-overview>`_.

JSONAPI results generally are formatted in JSON with the data stored in the response.data object:

* type (entity type)
* id (string of the uuid)
* attributes (an object of field data)
* relationships (an object of types, id, and links to referenced entities)
* included (an optional object of full referenced entities. This requires an includes parameter be provided)



.. toctree::
   :maxdepth: 1
   :caption: Contents:

   cms_api_taxonomy_terms
   cms_api_legal_problems_list
   cms_api_legal_problem
   cms_api_solutions_list
   cms_api_solution
   cms_api_questions_list
   cms_api_question
   cms_api_how_to_list
   cms_api_solution_how_to
   cms_api_step
   cms_api_solution_form
   cms_api_solution_helpful_organization




Authentication
===================

An authorization token will be required to access the API.


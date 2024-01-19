============================
Content API:  Legal Question
============================

Returns a specific question and answer. The UUID of the question must be provided.

Function call
================

Method: GET

URLs:

* https://www.illinoislegalaid.org/jsonapi/node/legal_question/[uuid] (English)
* https://www.illinoislegalaid.org/es/jsonapi/node/legal_question/[uuid] (Spanish)
* https://www.illinoislegalaid.org/pl/jsonapi/node/legal_question/[uuid] (Polish)

Sample response
=================

See the :ref:`legal-questions-list-api` for an example.

Parameters
=============

* question_identifier:  uuid of the question to return.

Any parameter supported by the JSONAPI is supported. See the :ref:`ilao-api-filters` for filter examples.



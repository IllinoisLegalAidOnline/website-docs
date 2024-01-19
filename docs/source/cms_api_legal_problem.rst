=================================
Content API: Legal Problem
=================================

Returns a specific legal problem package. This includes the full content:  problem, solutions, etc.

Function call
===============

Method: GET

URLS:

* https://www.illinoislegalaid.org/jsonapi/node/legal_problem/[uuid] (English)
* https://www.illinoislegalaid.org/es/jsonapi/node/legal_problem/[uuid] (Spanish)
* https://www.illinoislegalaid.org/pl/jsonapi/node/legal_problem/[uuid](Polish)

.. note:: For example https://www.illinoislegalaid.org/jsonapi/node/legal_problem/9cff9122-2e2e-404a-b909-bf58955c40a6 returns the Legal Problem of "I am unemployed".


Sample Output
=================

See the :ref:`legal-problems-list-api` for an example.

Parameters
=============

* identifier:  the uuid of the problem (required)

Additional parameters supported by the JSONAPI are allowed. See the :ref:`ilao-api-filters` for filter examples.

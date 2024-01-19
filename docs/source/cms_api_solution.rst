============================
Content API: Legal Solution
============================

Returns the entire schema for a specific solution. While solutions exist within problems, it is sometimes helpful to pull in just the solution segment.

Function call
================

Method: GET


URLs:

* https://www.illinoislegalaid.org/jsonapi/node/legal_solution/[uuid] (English)
* https://www.illinoislegalaid.org/es/jsonapi/node/legal_solution/[uuid] (Spanish)
* https://www.illinoislegalaid.org/pl/jsonapi/node/legal_solution[uuid] (Polish)

.. note:: For example:  https://www.illinoislegalaid.org/jsonapi/node/legal_solution/608b2d24-b283-46ec-a8e0-4fb2ec920b2d will return the Legal Solution Apply for unemployment insurance (UI) benefits.

Sample Response
=================

See the :ref:`legal-solution-list-api` for a full example.

Parameters
============

* identifier:  the uuid of the specific solution can be included to return a specific solution.


Additional parameters supported by the JSONAPI are allowed. See the :ref:`ilao-api-filters` for filter examples.

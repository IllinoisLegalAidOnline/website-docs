========================
Content taxonomy terms
========================

Taxonomy term API calls return the list of terms for a specific taxonomy for the language specified OR returns the list of terms and term IDs

* life areas
* solution types
* form prep programs

For each taxonomy, the taxonomy
Function call
==================

Method: GET


 
Sample Output
=================

.. code-block:: json

   [{
   "name":"White"},
   {"name":"Black"},
   {"name":"Red"},
   {"name":"Green"},
   {"name":"Blue"},
   {"name":"Orange"}]
   
Parameters
==============

* language: the 2 digit ISO code of the language to return   
* includeIds: if provided, the term UUIDs will also be returned
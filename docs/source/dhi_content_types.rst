=====================
DHI Content Types
=====================

Contents
--------

.. toctree::
   :maxdepth: 1

   dhi_ct_legal_resources
   dhi_ct_options
   dhi_ct_summaries
   dhi_ct_other


Metadata conditions
=======================
Metadata conditions are used in legal resources and legal options.


An item will match a user's specific debt journey when their problem profile OR debt entity:

* Matches on EVERY term in the Required ALL metadata, when at least one is selected; when left blank, it will never match unless the Ignore empty all metadata box is checked
* Matches on AT LEAST on of any Required ANY metadata, when at least one is selected; when left blank, it will never match unless the Ignore empty any metadata box is checked
* Matches on any selected debt type
* Matches on any selected problem type

Examples
------------

Article A
^^^^^^^^^^^^^
Article A has required metadata of is_debt_collector, is_wrong_venue; has required any metadata of is_600_of_fpg, is_300_of_fpg, debt type(s) of credit card, medical debt and problem type of "I'm being sued on a debt"

User 1's profile has:

* is_debt_collector = Y
* is_wrong_venue = Y
* is_600_of_fpg = N
* is 300_of_fpg = Y
* debt type = credit card debt
* problem type = "I'm being sued on a debt"

The article WOULD BE returned for this user; it matches on both required ALL and at least one of the required ANY and on the debt type and problem type.

User 2's profile has:

* is_debt_collector = Y
* is_wrong_venue = N
* is_600_of_fpg = N
* is 300_of_fpg = Y
* debt type = credit card debt
* problem type = "I'm being sued on a debt"

The article WOULD NOT BE returned for this user because it failed the Required All metadata.

User 3's profile has:

* is_debt_collector = Y
* is_wrong_venue = Y
* is_600_of_fpg = N
* is 300_of_fpg = N
* debt type = credit card debt
* problem type = "I'm being sued on a debt"

The article WOULD NOT BE returned for this user because it failed the Required ANY metadata.

Article B
^^^^^^^^^^^
Article B has required ALL metadata of is_wrong_venue, a debt type of Credit card debt, and a problem type of I'm being sued on a debt. It has nothing marked for any metadata.

User 1's profile:

* is_debt_collector = Y
* is_wrong_venue = Y
* is_600_of_fpg = N
* is 300_of_fpg = Y
* debt type = credit card debt
* problem type = "I'm being sued on a debt

This article would be returned if the Ignore empty Any metadata was checked because only the "is_wrong_venue" and debt type and problem type would be required.

User 2's profile:

* debt type = credit card debt
* problem type = "I'm being sued on a debt
* has no other metadata

This article would never be returned because is_wrong_venue is not defined.

Article C
^^^^^^^^^^^^^
Article B has a debt type of Credit card debt, and a problem type of I'm being sued on a debt. It has nothing marked for the ANY metadata and nothing marked for the ALL metadata.

User 1's profile:

* is_debt_collector = Y
* is_wrong_venue = Y
* is_600_of_fpg = N
* is 300_of_fpg = Y
* debt type = credit card debt
* problem type = "I'm being sued on a debt

This article would be returned if the Ignore empty Any metadata and Ignore empty ALL metadata was checked because only debt type and problem type would be required.

It would not be returned if the ignore boxes were not checked.

User 2's profile:

* debt type = credit card debt
* problem type = "I'm being sued on a debt
* has no other metadata

This article would always be returned because it matches on debt type, problem type, and there is no metadata collected.



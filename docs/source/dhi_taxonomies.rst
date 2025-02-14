====================
DHI Taxonomies
====================

Debt Help Illinois has the following taxonomies that are used to tag and categorize resources.

Problem type
==============

The problem type taxonomy includes the types of debt problems the site is expecting to solve. The taxonomy is used:

* to provide the front-end filtering question for the type of problem the individual is seeking help for (or thinks they are seeking help for)
* to associate content with specific debt problems

Problem type has:

* Name. This is the label shown to individuals
* Description. This is a short user-friendly description to help users identify the type of problem they are experiencing or stage of the debt.
* Debt type. This is a reference to the debt type taxonomy to tie specific debt types to specific problem types. For example, "Trouble paying bills" may cover more debt types than "A judgment has been entered against me"


Debt type
=============

The debt type taxonomy includes the types of debts the site is expecting to help users with. The taxonomy is used:

* to associate specific debt types with specific debt problems that the system is currently helping people with
* to associate content with specific debt problems

Debt type has:

* Name. This is the label shown to individuals
* Description. This is a short user-friendly description to help users identify debt types.
* Main category. This is used to group debts into classes. 
* Typical priority. This is used to classify debts into High, medium, or low priority for repayment
* Priority note. This is a text field to allow the prioritization tool to explain why a debt is classified as it is.
* Security status. This is used to indicate whether typically the debt is secured, unsecured, or depends on context.

.. todo:: Determine what type of icon to include with debt type (image or font awesome class)

General information categories
=================================

The general information categories taxonomy is designed to allow us to tag specific resources into categories that will create a browsable set of general resources. It is used to

* to associate resources to consumer debt-related topics.

General information categories have:

* Name. This is the label shown to individuals
* Description. This is a short user-friendly description to help users identify what types of information may be included in the category.

Region
========

The region taxonomy is a replication of the region taxonomy on IllinoisLegalAid.org and contains a hierarchical taxonomy of state, county, city, zip code. For example, 60603 will relate up to Chicago, Cook, Illinois and 60505 will relate up to Aurora, Kane, Illinois.

This taxonomy is used primarily to:

* Gather additional geographic data when we have a visitor's zip code
* Tag legal resources or options to specific jurisdictions
* Indicate that legal resources or options do not apply to specific jurisdictions

Creditor taxonomy
===================

The creditor taxonomy is used to maintain an internal listing of known common creditors. The taxonomy contains:

* Name
* Type (collection agency, debt buyer, law firm, original creditor)
* Aliases (common misspellings or other variants that may be used to support fuzzy searching)


Courts
====================

The court information taxonomy is used to store information about the Illinois court system. The taxonomy contains:

* Name of the court house (Adams County Courthouse, Appellate Court - 1st District), for example
* Street address of the court
* Phone number of the court
* Website url
* URL of the directory page from the IL court website, which provides better metadata on the Court
* Typical opening time (in hh:mm a.m)
* Typical closing time (in hh:mm p.m)
* Jurisdiction (based on our jurisdiction paragraphs bundle); this then connects to the region taxonomy so that we can tie specific user profiles to their local court automatically
* District - number of the district the court is in
* Circuit - the ordinal number of the circuit the court is in, if applicable.

Problem Profile Metadata
============================

Problem profile metadata are terms that are attached to debts and profile data to evaluate the appropriatness of an article or option. These are variables that are returned from Landbot.

Each taxonomy term has:

* A name
* An optional description
* A variable name that corresponds to the Landbot variable name
* The variable type (Boolean, String or Number); defaults to Boolean
* Evaluation function is a text field to input a specific function to evaluate the variable as true or false.

.. note:: We have not created any functionality that supports the evaluation function piece yet.


Prompt Library
=================

The prompt library is designed to store AI prompts that can be used to generate content. 

Each term has:

* A name
* A description that contains the actual prompt. Tokens are supported.

Example prompts may be:

* "Write an article of less than 300 words that explains [node:title]" where the [node:title] token is replaced with the content title"
* "Write an article of less than 300 words that explains [node:title] when it involves debt of [node:field_debt_types]" where the [node:title] token is replaced with the content title and the [node:field_debt_types] is replaced with the selected debt typetaxonomy terms attached to the article.

Region
==========

This is an import of the IllinoisLegalAid.org region taxonomy that includes state, county, city, and zip code data.

Glossary
===========

The glossary taxonomy contains glossary terms.

Each term has:

* A name
* A description, which serves as the definition




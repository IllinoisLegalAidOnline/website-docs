================================
Organization referral algorithm
================================

Business card referrals are generated based on:

* Whether the specific referral is a best bet for a legal issue or topic
* The referral score for the service

Organizations are then organized by type (legal aid, bar referrals, legal self-help centers, and non-legal organizations).


Referral Best Bets
=====================

ILAO admins can set a location service to be a best bet for a particular legal issue or intake population, or both.

.. note:: See the :ref:`referral_mgmt` for more information on how and when a Best Bet should be used.

Referral Score
==================

The system will automatically generate a score for location services content based on data in our Get Legal Help referral settings form and individual profile data, including whether the service is a hotline, advice desk, allows walk-ins, phone or email intake and the volume of the service.

Volume is updated on an annual basis with data provided by organizations.

.. note:: See the :ref:`referral_mgmt` for more details on how this score is set.

Results Algorithm
===================

The referrals page results are organized as follows:

* Best Bets - the first results will be any location service that:

  * Matches on location and legal issue
  * Matches on population, or is not limited to any population
  * Is open
  * Provides direct representation
  * Is a Best Bet on the legal issue OR Is a best bet on a population the user is a member of
  * Is then ordered by referral score descending if there are multiple matching Best Bets
  * Is not part of OTIS

* Top Results - up to 5 results of any location service that:

  * Matches on location and legal issue
  * Matches on population, or is not limited to any population
  * Is open
  * Provides direct representation
  * Is not a Best Bet on the legal issue AND is not a best bet on a population the user is a member of
  * Is not part of OTIS
  * Is then ordered by referral score descending with a limit of 5 results

* Bar referrals
* The LSHC serving the user's county.
* Helpful organizations that match the user's location and legal issue. These are automatically imported community and social service organizations. As of 2024, this is limited to housing counselors and domestic violence agencies.

.. note:: An organization may be an OTIS partner and have services outside of OTIS. For example, Legal Aid Chicago may use OTIS for housing cases but have a separate non-OTIS service for senior family law cases. Legal Aid Chicago will not come back as a business card referral for housing but will come back if the visitor is a senior with a family law problem.





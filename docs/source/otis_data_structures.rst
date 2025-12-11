================================
Get Legal Help Data Structures
================================

Organization
================

+--------------------+----------------------+-------------------------------------------+
| Field              | Type                 | Description                               |
+====================+======================+===========================================+
| ID                 | Auto-generated number|                                           |
+--------------------+----------------------+-------------------------------------------+
| Name               | Short text           | Name of the organization                  |
|                    | Required             |                                           |
+--------------------+----------------------+-------------------------------------------+
| Alternate name     | Short text           | Alias of an organization, if applicable   |
+--------------------+----------------------+-------------------------------------------+
| Description        | HTML                 | Organizational description                |
+--------------------+----------------------+-------------------------------------------+
| Physical address   | Address              | Street address, city, state, zip code     |
|                    | Required             |                                           |
+--------------------+----------------------+-------------------------------------------+
| Display address    | Yes/No               | Indicates whether address can be shown    |
| to public users    | Required             | when providing a referral                 |
+--------------------+----------------------+-------------------------------------------+
| Mailing address    | Address              | Street address, city, state, zip code     |
|                    | Required             |                                           |
+--------------------+----------------------+-------------------------------------------+
| Phone number       | Telephone            | Telephone number as (xxx) xxx-xxxx        |
|                    | Required             |                                           |
+--------------------+----------------------+-------------------------------------------+
| Contact email      | Email                | Email address for primary/general         |
| address            | Required             | contact                                   |
+--------------------+----------------------+-------------------------------------------+
| Website addresss   | URL; Required        | Full website url                          |
+--------------------+----------------------+-------------------------------------------+
| Facebook           | URL                  | Link to org's Facebook page               |
+--------------------+----------------------+-------------------------------------------+
| Twitter/X          | URL                  | Link to org's Twitter/X page              |
+--------------------+----------------------+-------------------------------------------+
| Instagram          | URL                  | Link to org's instagram feed              |
+--------------------+----------------------+-------------------------------------------+
| Associated email   | Short text; multiple | Domains associated with organization;     |
| domains            |                      | users registering with the domain are     |
|                    |                      | given legal aid permissions automatically |
+--------------------+----------------------+-------------------------------------------+
| Public referral    | Yes/No               | Indicates whether organization provides   |
|                    | Required             | services to the public.                   |
+--------------------+----------------------+-------------------------------------------+
| Maximum callbacks  | Number               | For OTIS orgs, when set, limits callbacks |
| per we call you    |                      | per slot universally                      |
| slot               |                      |                                           |
+--------------------+----------------------+-------------------------------------------+

Locations
=============
Every organization must have at least one location.

+--------------------+----------------------+-------------------------------------------+
| Field              | Type                 | Description                               |
+====================+======================+===========================================+
| ID                 | Auto-generated number|                                           |
+--------------------+----------------------+-------------------------------------------+
| Parent organization| Number; required     | ID of the organization                    |
+--------------------+----------------------+-------------------------------------------+
| Title              | Short text           | Title/name of the location (main office,  |
|                    | Required             | Alton office, etc)                        |
+--------------------+----------------------+-------------------------------------------+
| Address            | Address              | May be copied from organization; street   |
|                    | Required             | address, city, state, zip code            |
+--------------------+----------------------+-------------------------------------------+
| Phone number       | Telephone            | May be copied from organizatio            |
|                    | Required             |                                           |
+--------------------+----------------------+-------------------------------------------+
| TTY phone number   | Telephone            | TTY phone number, if applicable           |
+--------------------+----------------------+-------------------------------------------+
| Toll-free number   | Telephone            | Toll free number, if applicable           |
+--------------------+----------------------+-------------------------------------------+
| Weekly hours       | Complex              | First occurence start and end dates       |
|                    | Required if not open | Repeat rule baed on RRule format          |
|                    | at least weekly      |                                           |
+--------------------+----------------------+-------------------------------------------+
| Hours              | Complex              | Up to 4 time slots per day, each with     |
|                    | Required if open at  | its own start and end times               |
|                    | least once a week    |                                           |
+--------------------+----------------------+-------------------------------------------+
| Holidays           | Holiday taxonomy term| Holidays when a location is closed        |
|                    | Unlimited cardinality|                                           |
+--------------------+----------------------+-------------------------------------------+
| Serves all of IL   | Yes/No; required     | Yes for statewide organizations; no for   |
|                    |                      | all others                                |
+--------------------+----------------------+-------------------------------------------+
| Counties           | Term reference to    | Counties served by a location             |
|                    | county level of      |                                           |
|                    | region taxonomy;     |                                           |
|                    | unlimited cardinality|                                           |
+--------------------+----------------------+-------------------------------------------+
| Cities             | Term reference to    | Cities served by a location               |
|                    | city level of        |                                           |
|                    | region taxonomy;     |                                           |
|                    | unlimited cardinality|                                           |
+--------------------+----------------------+-------------------------------------------+
| Zip codes          | Term reference to    | Zip codes served by a location            |
|                    | county level of      |                                           |
|                    | region taxonomy;     |                                           |
|                    | unlimited cardinality|                                           |
+--------------------+----------------------+-------------------------------------------+
| Income eligibility | Single select        | Free, Free to eligible persons, sliding   |
|                    | Required             | scale based on income, flat fee           |
+--------------------+----------------------+-------------------------------------------+
| Income standard    | Single select        | Required when free to eligible persons.   |
|                    |                      | Options are Federal poverty level and area|
|                    |                      | median income                             |
+--------------------+----------------------+-------------------------------------------+
| Max. percentage of | Number               | Required when free to eligible persons.   |
| income standard    |                      |                                           |
+--------------------+----------------------+-------------------------------------------+
| Sliding scale      | Long plain text      | Required when income eligibility is       |
| description        |                      | sliding scale                             |
+--------------------+----------------------+-------------------------------------------+
| Flat fee           | Long plain text      | Required when income eligibility is flat  |
| description        |                      | description                               |
+--------------------+----------------------+-------------------------------------------+



.. note:: ILAO maintains a taxonomy of holidays, each with an associated date rule. We will also use this taxonomy to create "holidays" when an organization will be closed outside of typical holidays.

.. note:: The location geographic area could have been implemented better. We eventually moved to a Jurisdiction/Negate Jurisdiction option in other places but have not refined here. With that it is easy to mark an organization as Illinois except for Chicago or Illinois except for Cook County. The current system requires a choice between one of Statewide, 1 or more counties, 1 or more cities or 1 or more zip codes. These are stored i our Region taxonomy.


Services
================
Every location must have at least one service.

+--------------------+----------------------+-------------------------------------------+
| Field              | Type                 | Description                               |
+====================+======================+===========================================+
| ID                 | Auto-generated number|                                           |
+--------------------+----------------------+-------------------------------------------+
| Parent organization| Number; required     | ID of the organization                    |
+--------------------+----------------------+-------------------------------------------+
| Location           | Number; required     | ID of the location                        |
+--------------------+----------------------+-------------------------------------------+
| Is service open?   | Yes/No; required     | No referrals are made if set to No        |
+--------------------+----------------------+-------------------------------------------+
| Service type       | Single select        | One of: direct representation, legal info |
|                    | Required             | and education; self-help center; lawyer   |
|                    |                      | referral service;policy, impact litigation|
|                    |                      | support, or other                         |
+--------------------+----------------------+-------------------------------------------+
| Phone number       | Telephone; required  | Can be copied from location; phone number |
|                    |                      | for service.                              |
+--------------------+----------------------+-------------------------------------------+
| Income eligibility | Required             | Can be copied from location; otherwise,   |
|                    |                      | same questions as in location.            |
+--------------------+----------------------+-------------------------------------------+
| Is service limited | Yes/No; Required     | Indicates if the service is limited to    |
| by population      |                      | specific groups (seniors, disabled, etc)  |
+--------------------+----------------------+-------------------------------------------+
| Populations        | Term reference to    | One or more populations a person must be  |
|                    | intake populations   | to qualify for service. Req. if limited   |
+--------------------+----------------------+-------------------------------------------+
| Service area       | Required             | Can be copied from location; otherwise    |
|                    |                      | is statewide, counties, cities, zip codes |
|                    |                      | fields required                           |
+--------------------+----------------------+-------------------------------------------+
| Best bet for groups| Term reference to    | Allows ILAO staff to promote a referral   |
|                    | populations          | outside of OTIS for specific populations  |
+--------------------+----------------------+-------------------------------------------+
| Best bet for legal | Term reference to    | Allows ILAO staff to promote a referral   |
| issue              | legal issues taxonomy| outside of OTIS for specific legal issues |
+--------------------+----------------------+-------------------------------------------+








                       
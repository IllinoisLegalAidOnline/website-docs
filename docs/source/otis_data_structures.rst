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
| Hours              | Office hours         | Up to 4 time slots per day, each with     |
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

Direct representation fields
--------------------------------
These fields are unique to services that provide direct representation.

+--------------------+----------------------+-------------------------------------------+
| Field              | Type                 | Description                               |
+====================+======================+===========================================+
| ID                 | Auto-generated number|                                           |
+--------------------+----------------------+-------------------------------------------+
| Service is hotline | Yes/No; required     | Used to indicate if a service is a hotline|
+--------------------+----------------------+-------------------------------------------+
| Advice desk or     | Yes/No; required     | Used to indicate if advice desk or clinic |
| walk-in clinic     |                      |                                           |
+--------------------+----------------------+-------------------------------------------+
| Level of service   | Multi-select         | Extended representation, brief services,  |
|                    | required             | advice, mediation/ADR, pro bono placement |
+--------------------+----------------------+-------------------------------------------+
| Service delivery   | Multi-select         | In-person, phone, online/remote (incuding |
|                    | Required             | real-time and asynchronous communication  |
+--------------------+----------------------+-------------------------------------------+
| Practice areas     | Multi-select         | Legal issues taken from ILAOs' legal      |
|                    | Required             | issues taxonomy                           |
+--------------------+----------------------+-------------------------------------------+
| Average volume     | Number               | Estimate number of clients/cases per month|
|                    |                      | Used for cold referrals to prioritize     |
+--------------------+----------------------+-------------------------------------------+
| Application process| Multi-select         | Telephone, walk-in, online, email, online |
|                    | Required             | through OTIS                              |
+--------------------+----------------------+-------------------------------------------+
| Telephone process  | Plain long text      | Description of how one applies via phone; |
|                    |                      | used to set expectations                  |
+--------------------+----------------------+-------------------------------------------+
| Walk-in process    | Plain long text      | Description to how one applies via walk-in|
|                    |                      | where process includes walk-in            |
+--------------------+----------------------+-------------------------------------------+
| Online process     | Plain long text      | Description of the online process where   |
|                    |                      | process includes online                   |
+--------------------+----------------------+-------------------------------------------+
| Application form   | URL                  | Link to online application form if        |
|                    |                      | process includes online                   |
+--------------------+----------------------+-------------------------------------------+
| Email process      | Plain long text      | Description of the email applicaton       |
|                    |                      | process when process includes email       |
+--------------------+----------------------+-------------------------------------------+
| Email              | Email                | Email address for email applications      |
+--------------------+----------------------+-------------------------------------------+
| Program name for   | Short text           | For OTIS partners, their legalserver name |
| Legal Server       |                      | for mapping etransfers if on LegalServer  |
+--------------------+----------------------+-------------------------------------------+
| Callback slots     | Number               | Number of callback slots a person can     |
| per applicant      |                      | choose to schedule a callback             |
+--------------------+----------------------+-------------------------------------------+
| Maximum callback   | Number               | Maximum callbacks that can be scheduled   |
| per slot           |                      | in a time slot per service. Can be        |
|                    |                      | overridden at the organization level      |
+--------------------+----------------------+-------------------------------------------+


 
Intake Settings
=================

Intake settings are tied to a specific service. A service can have an unlimited number of intake settings but each should be unique.


+--------------------+----------------------+-------------------------------------------+
| Field              | Type                 | Description                               |
+====================+======================+===========================================+
| ID                 | Auto-generated       |                                           |
|                    | number               |                                           |
+--------------------+----------------------+-------------------------------------------+
| Name               | Short text           | Name for the intake settings              |
+--------------------+----------------------+-------------------------------------------+
| Service            | Number               | ID of the associated service              |
+--------------------+----------------------+-------------------------------------------+
| Legal issues       | Multi-select         | Legal issues taken from ILAOs' legal      |
|                    | Required             | issues taxonomy; may be copied from       |
|                    |                      | service                                   |         
+--------------------+----------------------+-------------------------------------------+
| Service area       | Required             | Can be copied from service; otherwise     |
|                    |                      | is statewide, counties, cities, zip codes |
|                    |                      | fields required                           |     
+--------------------+----------------------+-------------------------------------------+
| Intake open        | Yes/No; required     | Indicates whether intake is open or closed|
+--------------------+----------------------+-------------------------------------------+
| Number of intakes  | Number; required     | Number of intakes to allow per time period|
| allowed            |                      | Zero is treated as unlimited              |
+--------------------+----------------------+-------------------------------------------+
| Intake reset period| Daily, weekly, or    | Required when number of intake is not zero|
|                    | monthly.             | Count of etransfers reset based on this   |
+--------------------+----------------------+-------------------------------------------+
| Allow applications | Yes/No; required     | Allows/disallows applications from        |
| from jail/prison   |                      | jail or prison.                           |
+--------------------+----------------------+-------------------------------------------+
| Minimum age to     | Number; required     | Individuals at or above this age are      |
| qualify as a senior| Defaults to 60       | considered seniors for intake purposes    |
+--------------------+----------------------+-------------------------------------------+
| Minimum age to     | Number; required     | Minimum age to apply via OTIS. Minimum    |
| apply              | Default is 18        | is 13 to comply with online regulations   |
+--------------------+----------------------+-------------------------------------------+
| Qualifiers         | Term reference       | Option rules to apply to the intake to    |
|                    | to qualifiers        | determine eligibility                     |
+--------------------+----------------------+-------------------------------------------+
| Collect income?    | Yes/No; required     | Determines whether we collect income      |
+--------------------+----------------------+-------------------------------------------+
| Income types       | Term reference to    | List of income types to collect           |
|                    | income types;        | when income is collected                  |
|                    | multi-select         |                                           |
+--------------------+----------------------+-------------------------------------------+
| Apply income limit | Yes/No; required     | Determines whether the system tests for   |
|                    |                      | income eligibility                        |
+--------------------+----------------------+-------------------------------------------+
| Income standard    | Single select        | Required when apply income limit is yes.  |
|                    |                      | Options are Federal poverty level and area|
|                    |                      | median income                             |
+--------------------+----------------------+-------------------------------------------+
| Max. percentage of | Number               | Required when apply income limit is yes   |
| income standard    |                      |                                           |
+--------------------+----------------------+-------------------------------------------+
| Waive income for   | Multi-select term    | Ignores income calculation for these      |
| populations        | reference to         | groups                                    |
|                    | population taxonomy  |                                           |
+--------------------+----------------------+-------------------------------------------+
| Collect income for | Yes/No required      | If No, income will not be collected for   |
| waived populations |                      | people in those populations               |
+--------------------+----------------------+-------------------------------------------+
| Hours & Callback   | Hours Entity         | Indicates which hours & callback rules to |
| settings           |                      | use                                       |
+--------------------+----------------------+-------------------------------------------+
| Bypass intake and  | HTML text            | Message to display when programs want     |
| contact program    |                      | the person to call instead of apply online|
+--------------------+----------------------+-------------------------------------------+
| Program disclaimer | HTML text            | Text to display after application complete|
|                    |                      | as required by the organization           |
+--------------------+----------------------+-------------------------------------------+
| Household          | HTML text            | Text to display to help applicants define |
| definition         |                      | adults and children in household          |
+--------------------+----------------------+-------------------------------------------+
| Exit message for   | HTML text            | Text to display if applicant indicates    |
| current clients    |                      | they are already clients for this problem |
+--------------------+----------------------+-------------------------------------------+
| Exit message for   | HTML text            | Text to display if applicant indicates    |
| applicants who     |                      | they've already applied to the program.   |
| applied already    |                      |                                           |
+--------------------+----------------------+-------------------------------------------+
| "Please call us"   | HTML text            | Text to display for completed applications|
| message            |                      | where the applicant must call program     |
+--------------------+----------------------+-------------------------------------------+
| "We call you"      | HTML text            | Text to display for completed applications|
| message            |                      | who have scheduled a callback/appointment |
+--------------------+----------------------+-------------------------------------------+
| Collect country    | Yes/No; required     | Should we collect country of origin       |
+--------------------+----------------------+-------------------------------------------+
| Collect ethnicity  | Yes/No; required     | Should we collect ethnicity               |
+--------------------+----------------------+-------------------------------------------+
| Collect adverse    | Yes/No; required     | Should we collect adverse party           |
| information        |                      | information                               |   
+--------------------+----------------------+-------------------------------------------+
      
      
.. note:: The system collects race, gender, language spoken at home, marital status automatically. 

Hours & Callback Settings Entity
------------------------------------
Hours and callback settings are tied to an organization and can then be attached to any intake settings on any service for that organization.

+--------------------+----------------------+-------------------------------------------+
| Field              | Type                 | Description                               |
+====================+======================+===========================================+
| ID                 | Auto-generated       |                                           |
|                    | number               |                                           |
+--------------------+----------------------+-------------------------------------------+
| Title              | Short text           | Title of the entity; useful for finding   |
+--------------------+----------------------+-------------------------------------------+
| Parent organization| Number               | ID of the parent organization             |
+--------------------+----------------------+-------------------------------------------+
| Callback number    | Telephone; required  | Phone number for person to call program   |
+--------------------+----------------------+-------------------------------------------+
| Callback type      | Single select;       | Options are we call cient, client calls,  |
|                    | required             | or we call client - no appointment        |
+--------------------+----------------------+-------------------------------------------+
| Maximum callbacks  | Number; optional     | Maximum callbacks per slot                |         
+--------------------+----------------------+-------------------------------------------+
| Call back hours by | Multi-select slots   | Time slots for callbacks; each day has its|
| day                |                      | own select field                          |
+--------------------+----------------------+-------------------------------------------+
| Hours of operation | Office hours         | Up to 4 time slots per day, each with     |
|                    | Required if open at  | its own start and end times               |
|                    | least once a week    |                                           |
+--------------------+----------------------+-------------------------------------------+
| Add to calendar    | Yes/No; required     | Indicates whether we should add callback  |
|                    |                      | to program calendar                       |
+--------------------+----------------------+-------------------------------------------+
| Legalserver URL    | URL                  | Base url for calendar on LegalServer      |
+--------------------+----------------------+-------------------------------------------+
| Calendaring URL    | URL                  | Full url of calendaer to add appointment  |
|                    |                      | to                                        |
+--------------------+----------------------+-------------------------------------------+
| Calendaring        | Short text           | Token or API credential to write to       |
| credentials        |                      | calendar                                  |
+--------------------+----------------------+-------------------------------------------+

.. note:: Callback hours are grouped in 1 hour slots from 6am to 10:30am, with starting times on the hour and half-hour. Additionally, blocks of morning, afternoon, and evening are also available.

Qualifiers
------------

Qualifiers live in Guided Navigation in LegalServer. They are referenced via the Qualifiers taxonomy. See :ref:`otis-qualifiers-label` for more information.

+--------------------+----------------------+-------------------------------------------+
| Field              | Type                 | Description                               |
+====================+======================+===========================================+
| ID                 | Auto-generated       |  Term D                                   |
|                    | number               |                                           |
+--------------------+----------------------+-------------------------------------------+
| Name               | Short text           | Name of the qualifier                     |
+--------------------+----------------------+-------------------------------------------+
| Guided Navigation  | UUID                 | UUID for the process from LegalServer     |
| process ID         |                      |                                           |
+--------------------+----------------------+-------------------------------------------+




                       
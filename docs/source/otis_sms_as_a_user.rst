====================================
Getting legal help over SMS
====================================

Users can text ILAO's short code to apply for legal help in Illinois.

As of November 2023, users can apply for legal help in:

* Eviction (both landlord and tenant)
* Other rental housing issues
* TANF
* SNAP
* Unemployment benefits
* Clearing a criminal record
* Criminal defense (limited area)
* Orders of protection
* Civil no contact orders
* Stalking protective orders

New issues that will be added soon include:

* Bankruptcy
* Foreclosure
* Other non-bankruptcy consumer debt issues
* Asylum 
* U-Visa
* Divorce
* Property tax


If a user texts a keyword that we can match to an existing Guided Navigation flow, we will direct the user directly into the online triage and intake system with the Guided Navigation flow already determined. If the texted keyword does not match a term, we will ask the user to pick from a menu. 

The initial prompt asks the user to opt-in. Once the user opt-ins, they are asked for which language they would like to proceed in (English, Spanish, or Polish) and then directs them through the correct SMS flow.

* Step 1: Ask the user for their language (system supports English, Spanish, and Polish)
* Step 2: Determine if the keyword is a match to existing terms
* Step 3:

  * If there is a match, send that keyword to the relevant language subflow
  * If there is no match, send -1 to the relevant language subflow

* Step 4: If we do not get the user's legal issue from their keyword, they will enter their first subflow. This subflow is named "OTIS get legal issue"

* Step 5: We collect the user's first name and location in the "OTIS get location" subflow. During the subflow, the user provides their zip code and the system validates that it is in Illinois.

  * If the system determines that it is not an Illinois zip code, they will be informed, and they can text zip to enter a new zip code
  * If it is not an Illinois zip code and the user does not retry, the application refers the user to LawHelp.org and exits

* Step 6: We collect the number of adults and children in the household in the "OTIS household" subflow

  * The system then determines a maximum income threshold for the household size and asks the user to verify if they are above or below that level. If the user's income exceeds this threshold, the application exits.

.. note:: Some programs have no income limits either generally or for special populations. These are not yet supported in the SMS application.

* Step 7: Once the system determines that the user is eligible (geography and income), The "OTIS Guided Navigation" subflow is launched to triage the user through their legal problem.
* Step 8: When the guided navigation ends, the system connects to IllinoisLegalAid.org and  checks to see if one or more organizations match the user's legal issue

  * If no organization matches, the system exits with legal content
  * If more than 1 organization matches, the user is given a choice of where to apply
  * If 1 organization matches, the user is offered the option to apply.

.. note:: This needs updated for qualifiers & maybe adverse party

* Step 9: Once the user selects an organization to apply to, we begin the intake (OTIS Intake subflow). 

  * We collect the user's last name, any nicknames, and any aliases they have used
  * We collect the user's date of birth. We ask the user to confirm their date of birth and if it is incorrect, they can re-enter
  * We collect demographic data (race, ethnicity, gender, marital status, language)
  * We collect income information

    * If the user has wages or salary, we ask them how often they get paid and for an amount.
    * We ask them if they have self-employment
    * We ask if they receive any government cash benefits
    * We ask if they receive any regular private payments such as disability, alimony, child support or investment income
    * We ask if they have any other income sources

  * Determine income eligibility. If the user is not eligible because of their income, they are diverted to legal content
* Step 10: For income-eligible applicants, we gather the applicant's contact information (OTIS location subflow).

    * We ask them to confirm that the phone number used to text from is the best number to reach them at.

      * If this is not the best number, they are asked for the best number

    * We collect their email and address. We ask them to confirm their contact information. If there are any mistakes, they are prompted to redo them.

* Step 11: If the referral organization schedules callbacks: (begin OTIS appointment scheduler subflow)

  * The user is offered the first available appointment time
  * If this time does not work for the user, they are offered a set of available dates
  * When the user selects a date, they are offered a list of times to pick from

* Step 12: The system e-transfers a completed case file to LegalServer
* Step 13: A confirmation message displays
* Step 14: If the program has a disclaimer, that is shared with the user
* Step 15: A final "your application is complete" message displays with links to relevant legal information.

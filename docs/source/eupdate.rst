=======================
Automated eUpdate
=======================

The automated eUpdate compiles information from the website into a Mailchimp template that is then sent to targeted groups.

.. toctree::
   :maxdepth: 2
   :caption: See also:

   announcements

Who Gets the eUpdate
=======================

Any registered user of IllinoisLegalAid.org can get the eUpdate. When creating an account:

* Legal aid members default newsletter settings to select the eUpdate every Tuesday morning
* All others membership types default newsletter settings to select the eUpdate every month.

.. note:: Users may unselect the defaults before saving their account.

What is in the eUpdate
===========================
The weekly version includes content from the current date minus 7 days
The monthly version includes content from the current date minus 30 days


The content includes:

* Legal content, portal main pages, tools, toolboxes, and ADRM content that has a last revised date within the selected timeframe
* Legal content that has a created date = last revised date will show as "New" in the eUpdate
* The next 3 upcoming calendar events
* The 3 most recently updated published job postings

Sending
===========
The eUpdate is scheduled to send at:

* 9am Tuesdays for weekly subscribers.
* 9am on the 1st of the month for monthly subscribers.

Because the scheduled task system runs once per hour, it may be delayed and run anytime between 9am and 10am.

Tracking
==========
Links within the eUpdate are tracked using:

* campaign = date the eUpdate is sent
* source = eUpdate
* medium = email

These can be tracked in Google Analytics. Mailchimp also tracks data.


Testing
===========
There is a check group in the master segment that is made up of Gwen and various members of the QED42 team. This is the default send-to on all non-production instances to prevent accidentally sending from these machines to all users.

.. note:: Mailchimp campaigns sent to the check group may be safely deleted from Mailchimp.


Mailchimp/Website Integration
===============================

Subscribing to eUpdate via user account
-------------------------------------------
The mailchimp block that appears on the user registration/profile page is tied to the Master list within Mailchimp. When a user creates an account on the website:

* They are added to the master list
* They are added to the segment that matches their role
* If they sign up for specific communications, they are added to groups within website communications:

  * if they sign up for the monthly newsletter, they are added to the Newsletter segment
  * if they sign up for the weekly eUpdate, they are added to the weekly eUpdate segment
  * if they sign up for the monthly eupdate, they are added to the monthly eUpdate segment
  * if they sign up for the blog alerts, they are added to the blog segment

.. note:: There are also signup forms for anonymous users for the newsletter and the blog alerts.

Unsubscribing from eUpdates via user account
-----------------------------------------------
If a user edits their profile and changes the selections for eUpdates, ILAO blog, newsletter, those are reflected in their Mailchimp profile

If a user is marked inactive or deleted:

* their subscriptions are removed from the website
* their subscriptions are removed from Mailchimp
* they are set as "unsubscribed" in Mailchimp



Unsubscribing via Mailchimp
----------------------------
There is no automatic updates to the user's profile on the website if they unsubscribe from the master list in Mailchimp. This may result in resubscribing a user if their account is later resaved in Drupal

On a monthly basis, the product support manager should export a list of mailchimp users who have unsubscribed and who have website subscriptions and then edit their profile on the website.

If a user's account is edited by a staff user and the "Unsubscribe" box is checked:

* their subscriptions are removed from the website
* their subscriptions are removed from Mailchimp
* they are set as "unsubscribed" in Mailchimp










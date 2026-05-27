====================
Notifications
====================


Overview
===========

DHI includes a notification system that automatically sends messages to users when important things happen on the site. Notifications appear in a dedicated inbox on the user's dashboard and can also be delivered by email or text message, depending on the user's preferences.

All notifications built to date are listed below, along with what triggers them and how they are delivered.

----

Notifications
===============

Welcome Message
------------------

**What it does:** When a new user creates an account on DHI, they immediately receive a welcome notification in their inbox. The message greets them by name and prompts them to visit their account settings to set up their notification preferences and complete their profile.

**Message text:**

   Welcome to Debt Help Illinois [name]. Please visit your account page to enable text or email notifications and complete your profile.

**Trigger:** Automatically sent the moment a new account is created.

**Delivery:** On-site notification inbox only (appears the first time the user logs in).

----

Active Option Reminder
------------------------

**What it does:** If a user has started working through an option on DHI but has not logged back in for seven days, they receive a reminder nudging them to return to their dashboard and continue where they left off. This helps users stay on track and not lose progress on their debt help journey.

**Message text:**

   Pick up where you left off. Visit your dashboard to take the next step with [option title].

**Trigger:** A user has an active option in progress and has not logged into DHI for 7 or more days.

**Repeat cadence:** The reminder can repeat weekly, up to four times, until the user logs back in.

**Delivery:**

- **On-site** — appears in the user's notification inbox.
- **Email** — sent at 11:10 a.m. Central time, from the default DHI site email, with the subject "New notification from DebtHelpIllinois.org."
- **Text message** — sent at 11:05 a.m. Central time, from the standard DHI SMS number, with a short version of the message body.

Email and text delivery only occur if the user has opted into those channels in their account settings.

----

Notification Inbox
====================

All notifications are accessible at ``/user/[uid]/dashboard/notifications``. The page is private — users can only see their own notifications.

Each notification is displayed in a table showing the message text and the date and time it was sent (formatted as mm/dd/yyyy hh:mm am/pm).

**If there are no notifications,** the page shows:

   All caught up! We'll let you know here if you get a reminder, a request to share feedback, or an update with helpful resources.

Managing Notifications
-------------------------

Users can keep their inbox tidy with two actions on each notification:

- **Archive** — moves the notification out of the main inbox view. Archived notifications can be retrieved at any time by checking "Show archived messages."
- **Delete** — permanently removes the notification from view.

When a notification is archived, a confirmation message appears: *"This message has been archived. You can view archived messages by checking the 'Include archived messages' checkbox."*

When a notification is deleted, the message *"This message has been deleted."* is shown.

Unread Indicator
--------------------

When a user has one or more unread notifications (not archived, not deleted), a **red dot** appears on the envelope icon in the site header. Hovering over the icon shows the tooltip: *"You have new notifications."*

The envelope icon appears in the desktop header next to the language toggle, and in the mobile header next to the Dashboard label. It links directly to the user's notifications page.

----

Notification Preferences
=============================

Users control how they receive notifications from their profile settings page, under **Notification preferences**. The available options are:

- **Email** — notifications are sent to the user's email address on file. Selecting this option makes the email field required.
- **Text message** — notifications are sent as SMS to the user's mobile number. Selecting this option makes the mobile number field required. Standard message and data rates may apply; users can reply STOP to opt out.

If neither option is selected, notifications will only appear in the on-site inbox when the user logs in.




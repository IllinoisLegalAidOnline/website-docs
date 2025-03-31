================================
User journey: Returning users
================================

Returning users have a dashboard that tracks their progress. The information on the dashboard depends on where they are in addressing their debts.

.. note:: Clicking on any debt will update the current session's variables for the current debt entity ID and associated debt problem ID and problem profile ID.

Visitors can:

* Be working on one or more options for a specific debt
* Have prioritized debts in their queue
* Have one or more specific debts in their profiles that they have not yet started on an option for
* Have completed or archived debts
* Have never prioritized their debts

Visitors with active options
================================

An active option is one in which:

* It is tied to a specific debt
* The user has marked it as a "Yes"

.. note:: The user may or may not have actively started working on the option.

From each active option, the visitor will see:

* name of the debt
* title of the option
* the option's description
* a progress bar, based on the number of steps in the option and their individual progress
* a label repesenting the debt type
* a continue button that takes the user to the option page

Working on the active option
-----------------------------

When the user views an active option, they see a tailored view that:

* Hides the pros and cons
* Shows each step in full
* Has an indicator to show whether the step has been completed
* The ability to update the step's status
* An option to Mark the option as complete

.. todo: Add ticket for mark as done




Visitors with incomplete debts
==============================================

The "My debts" section shows:

* A single card for any priorited debts
* A card for each other debt that is not archived

The priorization card shows:

The single debt cards show:

* Debt name
* First 200 characters of the associated summary template for the specific debt
* Problem type taxonomy term label
* Your selected solution
* Drop down list of options
* View option link that takes the user to the specific option
* View debt summary that takes the user to the summary & next steps page.

.. todo: How do we handle the option selected when status is not yet set? Can I remove a debt?

Visitors with completed debts
==================================

The "Archived debts" section shows any debts that have a status of "Archived."

Each archived debt displays:

* Debt name
* First 200 characters of the associated summary template for the specific debt
* A congratulations message with the date the debt was archived
* A button to view the debt summary page

Visitors with saved resources
===============================

Saved resources for the dashboard page are those legal resources that the user has affirmatively checked.

.. todo: Add a no results option.
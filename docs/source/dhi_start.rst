==========================
User journey: Debt start
==========================

The "Get started" step in the debt tool is a form that includes:

* A disclaimer checkbox
* A terms of service checkbox
* A location checkbox

The form is editable on the backend by content authors in Configuration -> Debt Tool Configuration.

If a person does not check all 3 boxes, they can not proceed.

When the form is submitted, a problem profile is created that captures:

* Timestamp of terms of use accepted
* Timestamp of privacy policy accepted
* Sets the problem type to Debt problem
* Stores the UID of the user, if they are logged in



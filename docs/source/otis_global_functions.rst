======================
Global SMS functions
======================

These functions are used across applications.

OTIS Validate Total Income
===============================

**Function name:**  otis-get-callback-times **This appears to be the wrong function**

**Parameters:**

+------------------------+---------------------------------------------------+
|   Key                  | Description                                       |
+========================+===================================================+
|  adults                | Required. Integer.                                |
+------------------------+---------------------------------------------------+
|  children              | Required. Integer.                                |
+------------------------+---------------------------------------------------+
|  Income types          | Key should be named income_[income type]. Value   |
|                        | should be integer                                 |
+------------------------+---------------------------------------------------+
|  standard              | Basic, ami, or fpl. Defaults to fpl if not        |
|                        | provided.                                         |
+------------------------+---------------------------------------------------+
|  max                   | Percentage max income to calculate. Number.       |
|                        | Defaults to 300 if not provided                   |
+------------------------+---------------------------------------------------+

**Requires:**  Income Limits asset

**Returns** An object with values for

+------------------------+---------------------------------------------------+
|   Key                  | Description                                       |
+========================+===================================================+
|  income                | Integer; total income                             |
+------------------------+---------------------------------------------------+
|  incomeFlag            | 0 if not over-income; 1 if over-income.           |
+------------------------+---------------------------------------------------+
|  maxIncome             | Calculated maximum income                         |
+------------------------+---------------------------------------------------+

.. note:: Unemployment benefits are computed at the passed value times 4.3 to convert weekly to monthly for calculating income.

**Status:**  Complete


OTIS Validate Payments
=========================

**Function name:**  otis-validate-payments

**Purpose**: Takes a string of input from the user and returns an array of numbers that represent which types of payments we need to collect income information for.

**Parameters:**  event.payments (the user's input to the do you have any of these payments question)

**Requires:**  Nothing

**Returns:** An array of payment types to ask for income information from the user.

**Status:**  Complete.

OTIS Validate Benefit Types
===============================

**Function name:**  otis-validate-payments

**Purpose**: Takes a string of input from the user and returns an array of numbers that represent which types of benefits we need to collect income information for.

**Parameters:**  event.payments (the user's input to the do you have any of these benefits question)

**Requires:**  Nothing

**Returns:** An array of benefit types to ask for income information from the user. These are numerical values of 1-5 that are used to route the user through income questions.


OTIS Validate Benefit Types
===============================

**Function name:**  otis-validate-payments

**Purpose**: Takes a string of input from the user and returns an array of numbers that represent which types of benefits we need to collect income information for.

**Parameters:**  event.payments (the user's input to the do you have any of these benefits question)

**Requires:**  Nothing

**Returns:** An array of benefit types to ask for income information from the user.

**Status:**  Complete.

OTIS Validate Money Input
============================
**Function name:**  otis-validate-money-input

**Purpose**: Takes a string of input from the user and returns the string if it is a number or 0 if it is not. This can then be used to route users to retry their input or move on to the next step.

**Parameters:**  event.amount (the user's input in response to a money question)

**Requires:**  Nothing

**Returns:** A number. -1 is returned if it is not a valid amount.

**Status:**  Should be updated to accommodate for dollar formatting ($,. within the data).


Load marital statuses
==========================
**Function name:**  otis-load-marital-statuses

**Purpose**: Returns list of marital statuses for user to select from.

**Parameters:** event.langcode (may be null)

**Requires:**  None

**Returns:** A string of marital statuses for display based on the language code provided.


Load languages
==========================
**Function name:**  otis-load-languages

**Purpose**: Returns list of languages for user to select from.

**Parameters:** event.langcode (may be null)

**Requires:**  None

**Returns:** A string of languages for display based on the language code provided.

Load genders
==========================
**Function name:**  otis-load-genders

**Purpose**: Returns list of genders for user to select from.

**Parameters:** event.langcode (may be null)

**Requires:**  None

**Returns:** A string of genders for display based on the language code provided.


Load ethnicities
==========================
**Function name:**  otis-load-ethnicity

**Purpose**: Returns list of ethnicity options for user to select from.

**Parameters:** event.langcode (may be null)

**Requires:**  None

**Returns:** A string of ethnicities for display based on the language code provided.


Load races
==========================
**Function name:**  otis-load-races

**Purpose**: Returns list of races for user to select from.

**Parameters:** event.langcode (may be null)

**Requires:**  None

**Returns:** A string of races for display based on the language code provided.


OTIS Validate Race
============================
**Function name:**  otis-validate-race

**Purpose**: Takes a string of input from the user and returns whether it is a valid selection or not. This can then be used to route users to retry their input or move on to the next step.

**Parameters:**  event.race (the user's input)

**Requires:**  Nothing; values are stored in the function as an array

**Returns:** A string, either the name of the race the user selected OR 0 if it is invalid.


OTIS Validate Ethnicity
============================
**Function name:**  otis-validate-ethnicity

**Purpose**: Takes a string of input from the user and returns whether it is a valid selection or not. This can then be used to route users to retry their input or move on to the next step.

**Parameters:**  event.ethnicity (the user's input)

**Requires:**  Nothing; values are stored in the function as an array

**Returns:** A string, either the name of the race the user selected OR -1 if it is invalid.

OTIS Validate Gender
======================

**Function name:**  otis-validate-gender

**Purpose**: Takes a string of input from the user and returns whether it is a valid selection or not. This can then be used to route users to retry their input or move on to the next step.  The returned strings align with Legal Server's supported genders.

**Parameters:**  event.gender (the user's input)

**Requires:**  Nothing; values are stored in the function as an array

**Returns:** A string, either the name of the gender the user selected OR -1 if it is invalid.

OTIS Validate Marital Status
===============================

**Function name:**  otis-validate-marital-status

**Purpose**: Takes a string of input from the user and returns whether it is a valid selection or not. This can then be used to route users to retry their input or move on to the next step.  The returned strings align with Legal Server's supported marital statuses.

**Parameters:**  event.maritalStatus (the user's input)

**Requires:**  Nothing; values are stored in the function as an array

**Returns:** A string, either the name of the marital status the user selected OR -1 if it is invalid.

OTIS Validate Preferred Language
==================================

**Function name:**  otis-validate-preferred-language

**Purpose**: Takes a string of input from the user and returns whether it is a valid selection or not. This can then be used to route users to retry their input or move on to the next step.  The returned strings align with Legal Server's supported languages.

**Parameters:**  event.language (the user's input)

**Requires:**  Nothing; values are stored in the function as an array

**Returns:** A string, either the name of the language the user selected OR -1 if it is invalid.

OTIS Validate Year
======================
**Function name:**  otis-validate-year

**Purpose**: Takes a string of input from the user and returns whether it is a valid year. This can then be used to route users to retry their input or move on to the next step.

If the user enters a 2 digit year, it is assumed to be 19xx if the string is greater than 10.

**Parameters:**  event.year (the user's input)

**Requires:** none

**Returns:** A number (either the 4 digit year or a 0 representing invalid data)

.. note:: Would be nice to not allow future years to be included.

OTIS Validate Day of Month
===============================
**Function name:**  otis-validate-day-of-month

**Purpose**: Takes a string of input from the user and returns whether it is a valid number between 1 and 31 for  months with 31 days 1 and 30 for days with 30 days, and between 1 - 29 days for February. This can then be used to route users to retry their input or move on to the next step.

**Parameters:**  event.day (the user's input), event.month (the user's previous input for the month)

**Requires:**  none

**Returns:** A number (either the day or a 0 representing invalid data)


OTIS Validate Month
===============================
**Function name:**  otis-validate-month

**Purpose**: Takes a string of input from the user and returns whether it is a valid month. This validates both numbers (1 - 12) and text input such as November, november, nov, or Nov. This can then be used to route users to retry their input or move on to the next step.

**Parameters:**  event.month (the user's input)

**Requires:**  none

**Returns:** A number (either the day or a 0 representing invalid data)


OTIS Calculate Age
===================

**Function name:**  otis-calculate-age

**Purpose**: Calculates an age based on a date of birth.

**Parameters:**  event.day, event.month, and event.year (provided by the user)

**Requires:**  none

**Returns:** A number


OTIS Poverty Estimate
=======================

**Function name:**  otis-poverty-estimate

**Purpose**: Gets the estimated over-income threshold for users based on household size.

**Parameters:**  event.children and event.adult. Both should be numbers.

**Requires:**  API call to get poverty income.

**Returns:** An object containing:

* income, which represents the total income
* household_size, which represents the number of adults and children in the household

.. note:: This is the function to determine whether a user passes the initial basic income screening similar to what appears on IllinoisLegalAid.org/get-legal-help.

OTIS validate total income
============================

**Function name:**  otis-validate-total-income

**Purpose**: Gets the estimated over-income threshold for users based on household size.

**Parameters:**

* event.children and event.adult. Both should be numbers.
* event.standard which is the income standard to use.  This defaults to the federal poverty level.
* event.max which is the maximum income percentage to use.  This defaults to 300.
* Wage frequency, which is the wage frequency

**Requires:**  API call to get poverty income.

**Returns:** An object containing:

* income, which is the total monthly income
* incomeFlag, which is 0 or 1.  1 represents overincome
* maxIncome, which is the calculated maximum income based on the selected standard and allowable percentage.

.. note:: This is the function to determine whether a user passes the income screening for a specific organization.





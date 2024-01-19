============================
Twilio token updates
============================

All of our Twilio to IllinoisLegalAid.org calls require the use of Bearer tokens. These are acquired at the start of our OTIS and eviction bot flows and passed into the functions as needed.

Each flow should use the widget flow below to get and set the tokens:

* Get standard token requires a call to the https://ilao-8092.twil.io/oauth-get-token function. This will return a body containing the bearer token.
* To get a nonstandard token, make a call to the https://ilao-8092.twil.io/oauth-get-custom-token
* Set the tokens in a set variables function to set them in flow.variables
* Reference them in function calls with a name of token. For example, to use the standard token (stored as std_token in variables) in the update_triage_user function, pass a parameter named token with a value of {{flow.variables.std_token}}.  the function can then access it as event.token.

(Previously, these had been added manually to each function)



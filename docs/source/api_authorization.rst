====================
API Authorization
====================

API authorization requires a user-based OAuth token in order to access ILAO's APIs.

This requires within the website:

* Setting up an account for the specific user.  The user should have the most limited role possible to access the services they need to access.
* Create an API consumer.  Consumers should not be shared.  Consumers should:

  * Have a descriptive label (for example twilio-sms, legal-aid-chicago-cms)
  * Have a scope of API consumer
  * Have a strong secret

.. note:: we may need to define additional roles to accommodate API grants.

The API user will need to be provided with:

* the UUID for the consumer
* the secret used in the consumer
* the username of the account created to access the API
* the password of the account created to access the API

To generate a bearer token, the API user will need to:

* Post a request to https://www.illinoislegalaid.org/oauth/token
* The body of the request should include form data of:

  * client_id, which is the UUID of the consumer
  * grant_type, which should be password
  * client_secret, which is the secret associated with the consumer
  * username
  * password

The resulting request is a JSON packet containing:

* token_type
* expires_in, which is the number of seconds the token is good for.
* access_token, which is the access token to use
* refresh_token, which can be used to renew an expired access_token with no additional interaction.


.. warning:: To set someone up with API access,  see Gwen.




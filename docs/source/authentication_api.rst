=========================
Authentication API
=========================

The authentication API requires an API key issued by ILAO. The endpoint is https://www.illinoislegalaid.org/api/authorization-check. It accepts a single parameter, role, and will return true or false if the email is active and associated with the role.

It expects 2 header values:

* x-api-key, which is the API key ILAO provides.
* x-user-email, which is the email to check against

.. code:: 

   curl --location 'https://www.illinoislegalaid.org/api/authorization-check?role=ltf_grantee' \
   --header 'x-api-key: [Key]' \
   --header 'X-User-Email: [Email]' \

This will return one of two responses:

* If the email is associated with an active account with the specific role: 

.. code:: 
   
   {"authorized":true,"email":"[Email]"}
   
* If the email is not associated with an active account with the specific role: 

.. code:: 
   
   {"authorized":false,"email":[Email]"}
   
   
  

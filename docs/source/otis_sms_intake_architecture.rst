=====================
General architecture
=====================


This architecture applies to all of our SMS integrations.

Twilio Studio
--------------

The logical flow for the SMS is managed in Twilio Studio.  Each live version requires two phone numbers and two flows, one for development and one for production.  The production version should not be edited in Twilio studio but should be "deployed" by copying the development version and associating the production phone number with the newly deployed branch.

Deployed versions use a naming convention of [Name]-[language code][Month][Day][FullYear].  A letter may follow if there have been multiple deployments in the same day.  For example Eviction-enMay132021 or Eviction-enMay132021a.

Development versions should be named using a conviction of [Name]-Dev-[language code]; for example Eviction-Dev-en.


Twilio Functions
------------------
Twilio functions are used to:

* perform validation that is more complex than the split based on variables widget in Twilio studio

* interact with ILAO's API and other services
* any complex functionality

Twilio functions are stored in the ilao_service and are called using run function widgets in Twilio studio.

ILAO APIs
-----------
Online intake over SMS relies on ILAO's JSONAPI and other APIs for data synchronization.



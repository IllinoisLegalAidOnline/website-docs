=================================
LegalServer CustomField Support
=================================

LegalServer supports sending information via the jsonPayload transfer to custom fields that exist in an OTIS partner's instance of LegalServer. LegalServer's documentation: https://apidocs.legalserver.org/docs/ls-apis/ccfa12a1ae1df-online-intake-import

Options
==========
LegalServer allows custom field data to be transferred using two different methods:
  * jsonPayload; or
  * custom_fields

jsonPayload allows ILAO to create custom fields that do not need to match exactly to the partner's custom field and do not need to be mapped.

Naming convention
==================
To easily identify custom fields that need to be transferred to a specific OTIS partner, the following naming convention must be followed:
"[org]_custom_[partner's custom field]" 
In practice, the guided navigation field will look like: "lac_custom_applicant_pronouns_675" and when viewing the raw field name, "lac_custom_applicant_pronouns_675_358"

.. warning:: When creating the lookup values for the custom field, they must match exactly to the partner's lookup values

Using custom fields
====================
An OTIS partner may ask specific questions where the answers can be transferred via the Qualifiers (see :ref:`otis-qualifiers-label`) section of guided navigation. 

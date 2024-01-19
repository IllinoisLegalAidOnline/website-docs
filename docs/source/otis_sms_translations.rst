==========================
OTIS SMS Translations
==========================

To pull the text for translation:

* Open the English flow in Twilio Studio
* Copy the underlying JSON to notepad or other plain text editor
* Open the utilities service in Twilio functions
* Replace the text in the source.json file with the updated text
* Save and deploy
* Copy the url for the studio-parser function. This will generate parsed text.

Open Microsoft Word:

* Paste the text into a new document
* Using advanced find and replace:

  * Replace <eol> with Field name: and 2 paragraph marks
  * Replace | with a single paragraph mark



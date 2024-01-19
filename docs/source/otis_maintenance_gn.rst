======================================
Creating triage in Guided Navigation
======================================

Steps to create Dialogues & Segments
--------------------------------------
Step 1
^^^^^^^^
Create a new Dialogue within LegalServer by searching Guided Navigation within the Admin tab. New Dialogues should be created as Interactive Dialogue (plus in the top right of the list of interactive dialogues). 

Step 2
^^^^^^^^
Create new Segments within the Dialogue. Each Segment should have only one question or instruction. Each question within a segment is made by creating a custom field and custom lookup values. Custom fields and lookup values can be create from within the Segment by selecting Create Field in the top right corner of the Segment.

[image: create_field]

.. note:: Custom Fields should follow the naming convention "ilao-[issue]_short title". 

[image: field_name]

Step 3
^^^^^^^^
Choose New Custom Lookup from the types. The Custom Lookup will automatically be given the same name as the Custom Field. Assign answer options as Lookup values.

[image: lookup_values]

Step 4
^^^^^^^^
Add the Custom Field to the Segment by adding an element, select Field to capture from the dropdown, and find the field using the "ilao-[issue)_short title" provided earlier. Once the correct field is identified, give the field a Label. The label will be displayed to the applicant as the question.

To add instructions to a segment, simply Add element, select Instructions and complete the box with the text you want to display to the applicant. 

Step 5
^^^^^^^^
[add output expressions]

Step 6
^^^^^^^^
[create outcomes]
[within Dialogue or switch to another]
[rest-export]

Step 7
^^^^^^^
[Create Primary Form] - 

* New Intake Form - give name like, "GN-SNAP" to easily identify the form. 
* A description is not necessary. 
* Create New Process Containing This Form = yes; 
* Active = yes; 
* Add Continue Button = yes; 
* Process type = Intake. 
* Under Form Elements select Block and then choose Dialog Runner and Add. 
* Within the Dialogue Runner, choose the Dialogue created above. 
* Scroll to the bottom and Continue.

Create a Navigation Dialogue, which will route the user to the appropriate Interactive Dialogue. 
Add the Dialogue Runner Block to the form where the user should see the Dialogues.

[further expansion here]

Step 8
^^^^^^^
[Update Process created in Step 7]:

* Rename with the following naming convention ilao-GN-[top legal issue]_[more specific legal issue]. You may not have a more specific legal issue. Two examples of names are ilao-GN-HSG_landlord and ilao-GN-SNAP. 
* ***Process can be used with the Guided Navigation API must be set to yes.***
* For ease of adding the legal issue to SMS and the website, copy to Process UUID and paste it in the Process Description

.. _Authoring:

===================================
Authoring legal content by type
===================================

Content format is set based on a hierarchy using the content blocks included in the content. The content format is set to the first rule that applies:

* to IICLE, if the content contains an IICLE block
* to Easy Form, if the content is not an IICLE and contains the Automated Documents block
* to Decision tree, if the content 

   * is not an IICLE or Easy Form and
   * contains the Decision Tree block
   
* to Guide if it is none of the above and has a legal_bundle block.
* to How-to if it contains a process_step or portal_layout_timeline block
* to Blank form if it contains form download or form link
* to Link if it contains a Link block
* to Download if it contains a File block
* to Video if it contains a Video block
* to Decision tree if none of the above are true and it contains the A2J author block
* to Decision tree if none of the above are true

   * and it contains the Docassemble-embed block
   * and it has Docassemble type of "Decision tree"

* to Easy Form if none of the above are true

   * and it contains the Docassemble-embed block
   * and it has Docassemble type of "Easy form"

* to FAQ if none of the above are true and it contains at least one Q&A block
* to Text article if nothing else applies.
   

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   cms_legal_content_guides
   cms_legal_content_howto
   cms_legal_content_text_articles
   cms_legal_content_easyforms
   cms_legal_content_iicles
   cms_legal_content_videos
   cms_legal_content_static_forms
   cms_legal_content_link
   cms_legal_content_download
   cms_legal_content_docassemble
   cms_legal_content_qa

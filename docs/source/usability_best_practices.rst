========================
Usability best practices
========================

Purpose
=======

The following are suggestions for best practices related to usability of website content. These suggestions are based on the `Yale ITS Services <https://usability.yale.edu/>`_ usability and web accessibility guide.

Labeling
========
Strong labels and titles help a visitor determine whether a page, link, or content under a heading will have the desired information. Users typically scan titles, headings, and links first, and long bodies of text only after they have decided that doing so is likely to be worth their time. To maximize usability, use labels that provide users a good `information scent <https://www.nngroup.com/articles/information-scent/#:~:text=Information%20scent%20is%20a%20relative,looking%20for%20a%20facial%20cleanser.>`_.
The best labels are familiar to users already, using language they already use in their daily lives. The best labels are visitor-oriented, not site-owner- or producer-oriented. Avoid using unfamiliar words.

Headings
========

Headings and subheadings organize the content and are important for usability and accessibility. People with limited or no vision depend on screen reading software to read aloud the text on the screen. Using headings properly provides a hierarchy of content that allows users to navigate more efficiently.  

Benefits of Headings
====================

Screen reader users can navigate a page according to its headings, listen to a list of all headings, and skip to a desired heading to begin reading at that point. Screen reader users can use headings to skip the repeated blocks of content like headers, menus, and sidebars, for example.

Organizing pages using headings is one of the best accessibility strategies available.

Using Headings
==============

Headings are ranked <h1> through <h6> with the <h1> representing the most important idea on the page, and sub-sections organized with <h2> level headings. These sub-sections can themselves be divided with <h3> level headings, and so on.

* It is best to plan out a heading structure before composing a page. Doing so will help you both select appropriate heading levels and keep your thoughts organized overall.

* All pages should at least have a <h1> level heading giving the title of the page.

* Do not skip heading levels to be more specific (for example, do not skip from <h2> to <h5>). It is permissible to skip headings in the other direction if the outline of the page calls for it (for example, from <h5> to <h2>).

* Do not select heading levels based on their appearance. Select the appropriate heading rank in your hierarchy.

* Do not use bold instead of a heading. One of the most common accessibility mistakes is making text bold when a heading is needed. Though the text may look like a heading, the underlying code is not set correctly, and screen reader users will not benefit. 

* If you bold text to create the appearance of a heading, a screen reader will still read it as paragraph text. Conversely, do not use a heading style to make text big and bold if the text is not an actual heading.

* Do not overuse headings. In most cases, content editors will not need more than <h2> rank headings and the occasional <h3> rank. Only for exceptionally long or complex pages would <h5> and <h6> be necessary.

Generally, the title of the page should be the largest heading. Other headings and subheadings should have less visual weight according to their importance.



Maintain Visual Hierarchy
=========================

For web pages to be usable, the visual design should guide the eye through the most important parts of the page. Users generally do not read every word on the page. Rather, they scan the page looking for information that is relevant for their goals.

Design large, visually distinct headings and subheadings to help users find their way. Generally, the title of the page should be the largest heading. Other headings and subheadings should have less visual weight according to their importance. Likewise, reserve more saturated, attention-grabbing colors for more important areas of the page.

Design Legible Text
===================

To make text as easy-to-read as possible on the web, consider the following suggestions:

* Use generous font sizes for body text. Most browsers have a default font-size of 16px, and there is seldom reason to go below this size.

* Use generous line height / leading for paragraphs of text, to ensure that text is readable.

* Use left alignment for most text, and always for long blocks of text.

* Provide high color contrast between text and background. Consider using an `accessibility color contrast checker <https://webaim.org/resources/contrastchecker/>`_ to guarantee high contrast. Ensure that hover states also have high contrast.

* Consider limiting line lengths to no more than approximately 80 characters.

Images
======

Images, including photographs and graphic elements, may be the most important thing on your web site. People respond to images more readily than they do to lines of text. They will help create a mood for your site, and what they convey will be what people take away when they leave your site.

With that in mind, you should pay attention to the following when selecting images:

Aesthetic Considerations
========================

Every photo tells a story. Are your images telling the stories you want them to tell? If you’re not sure, ask people to view your site and let you know what they are feeling from seeing your photos. If you have a photo of a group of people sitting around a table, that doesn’t say much (it could represent anything). So try to use photos whose stories are immediately relevant to your content. Details often speak loudest. Maybe the objects on the table would say more than the people sitting around it. A photo doesn’t have to speak volumes, just a clear phrase.

Photos have color, composition, and movement. Do the colors in your photos blend well with the site’s color palette? Does the photo's composition lend itself to your site's mood? Does any movement in the photo elicit an emotional response, or feeling, that supports the site?

If you have humans in your photos, do they offer a fair representation of whom you are trying to attract to your site? Are they biased in any way, or do they suggest bias? In which direction are they looking? Do their eyes point inward, to more of the site, or to its edges, away from it?

How many photos are on a page? Do they compete with one another, and cancel one another out? Or do they harmonize well?

Technical aspects
=================

The web doesn’t require high-resolution images, but they should not look pixelated or out of focus. If you start with an image of at least 1MB, it should be OK. If not sure, start with higher res; you can always bring it down.

Make sure your photos meet the aspect ratio of the box that will house them (for instance, 4:3 or 2:3). You can crop photos to meet this. Make sure you select photos that will actually work for that aspect ratio. 


Image Guidelines
================

Understanding what makes good alt text is subtle and important. It should be brief: less than 250 characters. It should convey the purpose of the image, not describe the image. When writing alt text, consider what details are most important. The same image can have quite different alt text depending on its context. 

Some other best practices include:

* Avoid “image of”, “photo of”, etc, unless the medium is particularly important.
* Avoid using the title attribute instead of alt text. Keyboard-only users or mobile users may never see the title.
* Image links should describe the purpose of the link, and must never describe the image.
* Decorative images should have blank or empty alt text
* Complex images, like charts or graphs, should have a description located near the image. The image’s alt text should describe where the nearby image is.
* Posters, flyers, and the like must have the same information presented in nearby text/
* Provide color contrast and other design elements to help color-blind users

Charts, Graphs, and Other Complex Images
========================================

For charts, graphs, diagrams, illustrations, and other complex images, simple alt text may not be sufficient to convey the information. In such cases, the information should be provided in addition to text on the page. For charts and graphs, provide a data table with the equivalent information. For flow charts and diagrams, a discussion of the relevant information in the following paragraphs may be best. 

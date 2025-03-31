=============================
User journey: Diagnosis flow
=============================

After a visitor completes the debt start, they are taken through a Landbot diagnosis tool (the Landbot id and information is stored in the debt tool configuration).

Once the diagnosis is complete:

* The problem profile is updated to store the city, county, zip code, and zip suffix
* A debt problem entity is created that stores:

  * the problem profile ID
  * the taxonomy term of the problem type (as current problem)
  * any other provided field data is stored
  
* One or more debt entities are created

  * For users who don't use the prioritization feature:
  
    * Exactly 1 debt entity is created
    * The debt name is stored  
    * The term reference for the debt type is stored
    * any other provided field data is stored
    
  * For users who use the prioritization feature:
  
    * One debt entity is created for each type of debt returned
    * The debt type is stored to the Prioritized debt type taxonomy term id
  
 
Once completed, the user is then directed to their summary and next steps, or to a prioritization summary, depending on how the responded to the diagnosis tool.

**Real Estate Terminal App Idea (for Sellers) Pseudocode**

*Functionalities*

***Main View***
1. Options shown and require user input too choose
* Manage Property List
* Manage Client List
* Seller Portal
* Exit

***Manage - Property List for sale***

1. Current property list json file with the following header: Property ID (autogenerated), Suburb, Price, Number of Bed/s, Number of car space/s

2. User provided with option to add, edit or delete from the property list 

3. Depending on chosen step, ask user input 
* Add - ask each detail, autogenerated property ID, output summary to confirm the details, edit if needed, out summary to confirm details, confirm added!

* Edit - property ID or suburb required, pull up information (if there are 2 properties in the area, ask to choose which one), confirm which details to edit, summarise new version, save!

* Delete - property ID or suburb required, pull up information (if there are 2 properties in the area, ask to choose which one), pull up summary and confirm planned deletion, delete!


***Manage -  Client List***

1. Current client list json file with the following header: Client ID (autogenerated), Suburb/s Interested in, Budget Price, Number of Beds, Number of car space/s

* Price fixed

* Allows for multiple suburb list interest(how?)

* Number of room or car space either range or minimum(range how?)

2. User provided with option to add, edit or delete from the Client list 
* Add - ask each detail, autogenerated client ID, output summary to confirm the details, edit if needed, out summary to confirm details, confirm added!

* Edit - customer first name or last name, pull up information (if there are 2 Annas, ask to choose which one), confirm which details to edit, summarise new version, save!

* Delete - customer first name or last name required, pull up information (if there are 2 Annas, ask to choose which one), pull up summary and confirm planned deletion, delete!

***Seller Portal***

* Able to Pick a Client ID or First/Last name and will provide a list of available properties for sale within the client's requirements (dictionary)

Notes:
1. Can only enter name for client
2. Can only input one suburb
3. No range - is it possible 
# LoreliDejesus_T1A3 - Real Estate App Idea (for Sellers)

The *RealSeller* app is designed to aid sellers working in the real estate industry:

* To manage their growing Client and Property lists 
* To increase efficiency by automating the Client-to-Property match (and vice versa) based on requirements specified

With overall objective of increasing seller profitibaility through the help of the app. 

____
**R1: Answers to all the documentation requirements below.**

Completed all R1-R8 notes with headers below.

____

**R2: Readme. separate heading for each documentation requirement and answers organised under the appropriate headings.**

Completed all R1-R8 notes with headers below.

___

**R4: Provide full attribution to referenced sources (where applicable).**

TBC 
___

**R4: Provide a link to your source control repository**

[Loreli De Jesus Github Repository](https://github.com/DJ-Lor/LoreliDejesus_T1A3)

[Loreli De Jesus Github Deck Presentation](https://github.com/DJ-Lor/LoreliDejesus_T1A3)
___

**R5: Identify any code style guide or styling conventions that the application will adhere to. Reference the chosen style guide appropriately.**

TBC 

___

**R6: Develop a list of features that will be included in the application. It must include: (1) at least THREE features (2) describe each feature**


1. Feature 1: Add a new Property or a Client to the current list

    * There is a current list maintained in json file for each Client and Property list.

    * There will be two main classes utilised, namely Client and Property classes.

    * User input required for each detail (example: Suburb or Price) to be added to the file(json). Code handling will use the json import to utilise the file as intended. 

    * There will be a Client or Property ID that will be generated. This will be explained in detail in the latter part of the readme document. 

    * A confirmation of the new Client or Property details will be shown to the user and confirmed saved. This is utilising the classes for each. 

    * Option asked if the user would like to go back to the main menu or exit. 

2. Feature 2: Edit a current Property or a Client from the current list

    * Editing a current list will utilise the import json functions to open, read and write on the file. 

    * User input will utilise the Client of Property ID as the main identifier and required information to pull up the list that requires an edit. 

    * A .capitalize() will be used for client inputs so it matches against the dictionary key to update.

    * A confirmation of the update done will be displayed.

    * Option asked if the user would like to go back to the main menu or exit. 


3. Feature 3: Delete a current Property or a Client from the current list

    * Deleting a current list will utilise the import json functions to open, read and write on the file. 

    * User input will utilise the Client of Property ID as the main identifier and required information to pull up the list that requires deletion. 

    * The Client or Property information will be displayed to confirm if the user would like to proceed with the deletion.

    * A confirmation of the update done will be displayed.

    * Option asked if the user would like to go back to the main menu or exit. 

4. Feature 4: Prospective Opportunity Portal (Client-to-Property match (and vice versa) based on requirements specified

    * Able to Pick a Client ID or Property ID and will provide a list of available opportunities(Properties/Clients) within the given requirements.

    * Example 1: Inputted Client ID will output all the properties in that given suburb and priced less than or equal to that client's budget

    * Example 2: Inputted Property ID will output all the properties in that given suburb and priced equal to or more than the property's selling price

    * This feature will require the json import to open, read and write. 

    * This feature will require the two json files (Client and Property) to interact via the matched IDs and display the required information. 


5. Feature 5: Main Menu 

    ***Main View***
    
    * Options shown and will require a user input to navigate the app 
        * Manage Property List
        * Manage Client List
        * Prospective Opportunity Portal
        * Exit
    
    * Navigating the terminal app experience requires usage of loops and conditional control statements in order to arrive to the chosen experience.

    * The main menu also utilises error handling to ensure that the app does not crash when user input deviates from the options required as input. 


6. Feature 6: ID generator 

    * The unique identifier for each Property or Client on the json lists are the IDs. 

    * The ID is 'auto-generated' via a function utilising a simple json file with a dictionary key ('ID') and a value int starting from 100 (without a range limit). 

    * The code utilises the json import functions to interact with the file and add an increment of 1 for every new entry. 

    * This is then utilised in the respective Client and Property classes. 

    * Refer to code below: 

    ``` python
    def id_generate():

    with open('json_files/id.json', 'r') as openfile:
        # Reading from json file
        id_obj = json.load(openfile)
        (id_obj)["ID"] = (id_obj)["ID"]+1

    with open('json_files/id.json', 'w') as openfile:
        json.dump(id_obj, openfile, indent=4, separators=(',',': '))
    return ((id_obj)["ID"])

    def id_display():

    with open('json_files/id.json', 'r') as openfile:
        # Reading from json file
        id_obj_r = json.load(openfile)
        return id_obj_r["ID"]


____

**R7: Develop and utilise a suitable project management platform to track the app's implementation plan.**

* Utilised Trello's kanban approach by diving my tasks into main headers for (1) Features and (2) Admin related to development. 

* In each column, the specific tasks are outlined along with the estimated deadline for completion. 

* Target date of completion is located at the bottom right of each card. This is color coordinated. 

    * Green means done
    * Yellow means deadline is fast-approaching
    * Red means deadline has passed and is delayed

![Project Management Progress 1](docs/Trello_Screenshot_Progress_1.png)























_____________
***Manage - Property List for sale***

1. Current property list is a json file with the following header: Property ID (autogenerated), Suburb, Price 

Example:

``` json 
[
    {
        "ID": 246,
        "SUBURB": "Bondi",
        "PRICE": 830000
    },
    {
        "ID": 810,
        "SUBURB": "Bondi",
        "PRICE": 750000
    },
    {
        "ID": 121,
        "SUBURB": "Coogee",
        "PRICE": 950000
    },
    {
        "ID": 141,
        "SUBURB": "Randwick",
        "PRICE": 650000
    }
]
```

2. User provided with option to add, edit or delete from the property list 

3. Features: 

* Feature 1: Add a Property - ask each detail, autogenerated property ID, confirm added!

* Feature 2: With the property ID required, this will pull up information > confirm which details to edit > user input to edit > summarise new version > save!

* Delete - property ID required, pull up information, pull up summary and confirm planned deletion, delete!


***Manage -  Client List***

1. Current client list json file with the following header: Client ID (autogenerated), Name, Email, Suburb Interested in (only choose 1), Budget Price

```
[
    {
        "ID": 6789,
        "NAME": "David",
        "EMAIL": "david@gmail.com",
        "SUBURB": "Bondi",
        "PRICE": 830000
    },
    {
        "ID": 12345,
        "NAME": "LDJ",
        "EMAIL": "david@gmail.com",
        "SUBURB": "Maroubra",
        "PRICE": 900000
    }
]

```

2. User provided with option to add, edit or delete from the Client list 
* Add - ask each detail, autogenerated client ID, confirm added!

* Edit - client ID required, pull up information, confirm which details to edit, summarise new version, save!

* Delete - client ID required, pull up information, pull up summary and confirm planned deletion, delete!

***Prospective Opportunity Portal***

* Able to Pick a Client ID or Property ID and will provide a list of available opportunities(properties/clients) within the given requirements.

* Example 1: Inputted Client ID will output all the properties in that given suburb and priced less than or equal to that client's budget

* Example 2: Inputted Property ID will output all the properties in that given suburb and priced equal to or more than the property's selling price

***Client and Property ID***

1. This is utilising a json file that increments by 1 for each new property or client list generated. This starts from 100 and without a range limit.

```
# ID generator for both client and property ID 
def id_generate():

    with open('id.json', 'r') as openfile:
        # Reading from json file
        id_obj = json.load(openfile)
        (id_obj)["ID"] = (id_obj)["ID"]+1

    with open('id.json', 'w') as openfile:
        json.dump(id_obj, openfile, indent=4, separators=(',',': '))
    return ((id_obj)["ID"])




# Printing the ID once saved
def id_display():

    with open('id.json', 'r') as openfile:
        # Reading from json file
        id_obj_r = json.load(openfile)
        return id_obj_r["ID"]

```


Notes:
1. Can only enter name for client
2. Can only input one suburb
3. Check that email is actually email provided
5. Check client price inputted is not a string
7. dollar sign for property price and budget
9. No matched prop or client in search - out put Come back again note
10. enter text instead of property price and iny


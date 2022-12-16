**Real Estate Terminal App Idea (for Sellers) Pseudocode**

*Functionalities*

***Main View***
1. Options shown and require user input too choose
* Manage Property List
* Manage Client List
* Prospective Opportunity Portal
* Exit

***Manage - Property List for sale***

1. Current property list json file with the following header: Property ID (autogenerated), Suburb, Price 

Example:

```[
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

3. Depending on chosen step, ask user input 
* Add - ask each detail, autogenerated property ID, confirm added!

* Edit - property ID required, pull up information, confirm which details to edit, summarise new version, save!

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


Notes:
1. Can only enter name for client
2. Can only input one suburb
3. Check that email is actually email provided
4. Need to spit out client ID or property ID once added? 
5. Check client price inputted is not a string
6. ID generator for both client and property ID  - explain in readme
7. dollar sign for property price and budget
9. No matched prop or client in search - out put Come back again note

Davo says C1.ID self init should 
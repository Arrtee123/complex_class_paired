# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays

As a user
So I can keep track of cards sent and to be sent
I want to be able to mark a birthday card for a year as "done"

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE
class Birthdays:

    def __init__(self):
        self.birthdays = []

    def add_birthay(self, name, birthday):
        # Parameters:
        #     name: string
        #     birthday: Date object
        # Side-effects:
        #     Add a dictionary item containing a nested dictionary in the following format.        
        #     {name: name, birthday: birthday, sent: False}
        pass

    def edit_birthday(self, name, birthday):
        # Parameters:
        #     birthday: date object
        # Side-effects:
        #     changes birthday property of given name to the new given birthday
        pass

    def edit_name(self, name, new_name):
        # Parameters:
        #     name: string
        # Side-effects:
        #     updates name to the new name
        pass

    def birthday_reminder(self, days=14):
        # Parameters:
        #     days(optional): integer (defaults to 14 days)
        # Returns:
        #     A list of dictionary items containing friends with birthdays coming up in the given time
        pass

    def age(self, name):
        # Parameters:
        #     name: string
        # Returns:
        #     age (int) of friend with given name
        pass

    def mark_done(self, name):
        Parameters:
            name: string
        Side effects:
            Change done key to True for given name





```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE



## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

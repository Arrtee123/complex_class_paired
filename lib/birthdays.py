from datetime import date
from dateutil.relativedelta import *

class Birthdays:

    def __init__(self):
        self.birthdays = []

    def add_birthday(self, name, birthday):
        # Parameters:
        #     name: string
        #     birthday: Date object
        # Side-effects:
        #     Add a dictionary item containing a nested dictionary in the following format.        
        #     {name: name, birthday: birthday, sent: False}
        self.birthdays.append({"name": name, "birthday": birthday, "sent": False, "ages_sent":[]})
        return None

    def edit_birthday(self, name, birthday):
        # Parameters:
        #     birthday: date object
        # Side-effects:
        #     changes birthday property of given name to the new given birthday
        for item in self.birthdays:
            if item["name"] == name:
                item["birthday"] = birthday
        return None

    def edit_name(self, name, new_name):
        for item in self.birthdays:
            if item["name"] == name:
                item["name"] = new_name

    def age(self, name):
        for item in self.birthdays:
            if name == item["name"]:
                difference =  relativedelta(date.today(),item["birthday"])
                return difference.years +1
        

    def reminder(self, reminder_days=14):
        reminder_list = []
        reminder_period = date.today() + relativedelta(days=reminder_days)
        for item in self.birthdays:
            birthday = item["birthday"]
            difference =  relativedelta(reminder_period,birthday)
            if (difference.months == 0 and difference.days <=14):
                reminder_list.append(item)
            upcoming_age = self.age(item['name'])
            if upcoming_age not in item["ages_sent"]:
                item["sent"] = False

        return reminder_list
            
            


    def mark_done(self, name):
        for item in self.birthdays:
            if name == item["name"]:
                upcoming_age = self.age(name)
                item["ages_sent"].append(upcoming_age)
                item["sent"] = True
        
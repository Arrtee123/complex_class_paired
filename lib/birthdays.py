import datetime
import dateutil

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
        self.birthdays.append({"name": name, "birthday": birthday, "sent": False})
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
        pass

    def reminder(self, days=14):
        # Parameters:
        #     days(optional): integer (defaults to 14 days)
        # Returns:
        #     A list of dictionary items containing friends with birthdays coming up in the given time
        today = datetime.now()
        difference = relativedelta(today,date_of_birth).days

def age_checker(dob):
    today = datetime.now()
    try:
        date_of_birth = datetime.strptime(dob, "%Y-%m-%d")
    except:
        raise Exception("The date provided is in an invalid format or type")
    date_of_birth = datetime.strptime(dob, "%Y-%m-%d")
    
    difference = relativedelta(today,date_of_birth).years
    if difference >=16:
        return "Access is granted"
        
        

    def age(self, name):
        # Parameters:
        #     name: string
        # Returns:
        #     age (int) of friend with given name
        pass

    def mark_done(self, name):
        # Parameters:
        #     name: string
        # Side effects:
        #     Change done key to True for given name
        pass
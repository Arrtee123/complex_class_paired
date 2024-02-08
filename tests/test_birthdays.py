from datetime import date

from lib.birthdays import Birthdays

def test_initialisation():
    birthday = Birthdays()
    assert isinstance(birthday, Birthdays) == True
    assert birthday.birthdays == []

def test_add_birthdays():
    bd = Birthdays()
    date_ = date(1994, 1, 7)
    bd.add_birthday("Hassan", date_)
    assert bd.birthdays == [{"name": "Hassan", "birthday": date(1994, 1, 7), "sent": False}]

def test_edit_birthday():
    bd = Birthdays()
    date_ = date(1999, 1, 7)
    bd.add_birthday("Hassan", date_)
    bd.edit_birthday("Hassan", date(1994, 1, 7))
    assert bd.birthdays == [{"name": "Hassan", "birthday": date(1994, 1, 7), "sent": False}]

def test_edit_name():
    bd = Birthdays()
    date_ = date(1999, 1, 7)
    bd.add_birthday("Hassan", date_)
    bd.edit_name("Hassan", "Rachel")
    assert bd.birthdays == [{"name": "Rachel", "birthday": date(1999, 1, 7), "sent": False}]

def test_birthday_reminder():
    bd = Birthdays()
    date_ = date(1999, 2, 10)
    bd.add_birthday("Hassan", date_)
    assert bd.reminder() == [{"name": "Hassan", "birthday": date(1999, 2, 10), "sent": False}]

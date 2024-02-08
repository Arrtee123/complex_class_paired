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
    assert bd.birthdays == [{"name": "Hassan", "birthday": date(1994, 1, 7), "sent": False, "ages_sent":[]}]

def test_edit_birthday():
    bd = Birthdays()
    date_ = date(1999, 1, 7)
    bd.add_birthday("Hassan", date_)
    bd.edit_birthday("Hassan", date(1994, 1, 7))
    assert bd.birthdays == [{"name": "Hassan", "birthday": date(1994, 1, 7), "sent": False,  "ages_sent":[]}]

def test_edit_name():
    bd = Birthdays()
    date_ = date(1999, 1, 7)
    bd.add_birthday("Hassan", date_)
    bd.edit_name("Hassan", "Rachel")
    assert bd.birthdays == [{"name": "Rachel", "birthday": date(1999, 1, 7), "sent": False,  "ages_sent":[]}]

def test_birthday_reminder():
    bd = Birthdays()
    date_ = date(1999, 2, 10)
    bd.add_birthday("Hassan", date_)
    assert bd.reminder() == [{"name": "Hassan", "birthday": date(1999, 2, 10), "sent": False, "ages_sent":[]}]

def test_birthday_reminder_no_reminder_set():
    bd = Birthdays()
    date_ = date(1999, 1, 10)
    bd.add_birthday("Hassan", date_)
    assert bd.reminder() == []

def test_birthday_reminder_with_days_variable():
    bd = Birthdays()
    date_ = date(1999, 2, 28)
    bd.add_birthday("Hassan", date_)
    assert bd.reminder(30) == [{"name": "Hassan", "birthday": date(1999, 2, 28), "sent": False,  "ages_sent":[]}]

def test_ages_checker():
    bd = Birthdays()
    date_ = date(1999, 2, 28)
    bd.add_birthday("Hassan", date_)
    assert bd.age("Hassan") == 25

def test_mark_done():
    bd = Birthdays()
    date_ = date(1999, 2, 28)
    bd.add_birthday("Hassan", date_)
    bd.mark_done("Hassan")
    assert bd.birthdays == [{"name": "Hassan", "birthday": date(1999, 2, 28), "sent": True,  "ages_sent":[25]}]


def test_mark_done_with_reminder_reset():
    bd = Birthdays()
    bd.birthdays.append({"name": "Rachel", "birthday": date(1989, 1, 11), "sent": True,  "ages_sent":[35]})
    date_ = date(1999, 2, 10)
    bd.add_birthday("Hassan", date_)
    bd.mark_done("Hassan")
    bd.reminder()
    assert bd.birthdays == [{"name": "Rachel", "birthday": date(1989, 1, 11), "sent": False,  "ages_sent":[35]}, {"name": "Hassan", "birthday": date(1999, 2, 10), "sent": True,  "ages_sent":[25]}]


def test_mark_done_with_reminder_reset_and_age_sent_added():
    bd = Birthdays()
    bd.birthdays.append({"name": "Rachel", "birthday": date(1989, 2, 11), "sent": False,  "ages_sent":[34]})
    bd.mark_done("Rachel")
    bd.reminder()
    assert bd.birthdays == [{"name": "Rachel", "birthday": date(1989, 2, 11), "sent": True,  "ages_sent":[34, 35]}]
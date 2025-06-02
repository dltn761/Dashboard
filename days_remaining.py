import time
import datetime

today = datetime.date.today()
last_day = datetime.date(2026, 4, 30)
skillbridge_day = datetime.date(2026, 1, 1)


def days_left():
    days_remaining = (last_day - today).days
    if days_remaining <= 0:
        return "It's finally here!"
    else:
        return f"{days_remaining} days left until you're out of the Navy!"

def skillbridge_days_left():
    skillbridge_days_remaining = (skillbridge_day - today).days
    if skillbridge_days_remaining <= 0:
        return "Time to be an intern!"
    else:
        return f"{skillbridge_days_remaining} until you become an intern!"

def question():
    requested = int(input("What would you like to know today? "))
    if requested == 1:
        print(days_left())
    elif requested == 2:
        print(skillbridge_days_left())
    else:
        print("Please choose a correct input")
        

if __name__ == "__main__":
    question()

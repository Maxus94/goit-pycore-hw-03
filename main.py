from datetime import datetime, timedelta
import random, re

def get_days_from_today():
    current_date = datetime.today().date()
    print(current_date)
    any_date = input("Input date YYYY-MM-DD ")    
    try:
        any_date = datetime.strptime(any_date, "%Y-%m-%d").date()        
    except ValueError:
        print(f"Date \"{any_date}\" has wrong format")
    else:
        print(any_date)        
        diff_days = current_date - any_date
        print(f"{diff_days.days} days difference")

# get_days_from_today()

def get_numbers_ticket(min, max, quantity):    
    list = random.sample(range(min, max+1), quantity)    
    list.sort()
    print(list)

# get_numbers_ticket(1, 36, 5)
# get_numbers_ticket(1, 49, 6)

def normalize_phone(phone_number):
    print(re.sub("[^0123456789+]", "", phone_number))
    pass

normalize_phone("kjhjk8+90897kjh86")
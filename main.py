from datetime import datetime, timedelta
import random, re

def get_days_from_today():
    current_date = datetime.today().date()    
    any_date = input("Input date YYYY-MM-DD ")
    try:
        any_date = datetime.strptime(any_date, "%Y-%m-%d").date()        
    except ValueError:
        print(f"Date \"{any_date}\" has wrong format")
        return
    else:        
        diff_days = current_date - any_date
        return diff_days.days

# print(f"difference {get_days_from_today()} days")

def get_numbers_ticket(min, max, quantity):    
    list = random.sample(range(min, max+1), quantity)    
    list.sort()
    return(list)

# print(get_numbers_ticket(1, 36, 5))
# print(get_numbers_ticket(1, 49, 6))

def normalize_phone(phone_number):
    phone_number=re.sub("[^0123456789+]", "", phone_number)
    
    if (phone_number[0]!="+"):
        phone_number = re.sub("^[0]", "+380", phone_number)
        phone_number = re.sub("^[3]", "+3", phone_number)
    return(phone_number)

# raw_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]

# sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


def get_upcoming_birthdays(users):
    current_date = datetime.today().date()
    congratulation_dates = []
    for user in users:
        user_birthday=datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        user_birthday_this_year = datetime(year=current_date.year, month=user_birthday.month, day=user_birthday.day)
        user_birthday_this_year = user_birthday_this_year.date()
        diff_dates = user_birthday_this_year - current_date
        diff_dates = diff_dates.days
        if (diff_dates >= 0) and (diff_dates <= 7):            
            congratulation_date = user_birthday_this_year
            if(user_birthday_this_year.weekday() == 5):
                congratulation_date = user_birthday_this_year + timedelta(days = 2)
            elif(user_birthday_this_year.weekday() == 6):
                congratulation_date = user_birthday_this_year + timedelta(days = 1)                                        
            congratulation_date = congratulation_date.strftime("%Y.%m.%d")
            congratulation_dates.append({"name": user["name"], "congratulation_date":congratulation_date})        
    return(congratulation_dates)




# users=[{"name": "Maxim", "birthday": "1973.11.29"},
#     {"name": "TT", "birthday": "1920.11.15"},
#     {"name": "Nina", "birthday": "1946.11.08"},
#     {"name": "T", "birthday": "2018.11.24"},
#     {"name": "Inna", "birthday": "1985.11.26"},
#     {"name": "Ya", "birthday": "1973.11.30"},
#     {"name": "Yu", "birthday": "1973.12.03"},
#     {"name": "M", "birthday": "1915.12.03"},
#     {"name": "Ja", "birthday": "1912.11.28"},
#     {"name": "Vika", "birthday": "1985.11.23"}]

# print(get_upcoming_birthdays(users))
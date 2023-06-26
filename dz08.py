from datetime import datetime, timedelta
from collections import defaultdict
import calendar


def get_birthdays_per_week(users) -> dict:
    
    birthdays = defaultdict(list)
    weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    result = dict()  
    
    date_now = datetime.now().date() #datetime(2023, 12, 26).date() datetime(2020, 2, 25).date()
    date_start = date_now + timedelta(days=(5 - date_now.weekday()))
    date_end = date_start + timedelta(days=6)
    
    for user in users:
        
        name = user['name']
                
        if not isinstance(user['birthday'], datetime):
            user['birthday'] = datetime.strptime(user['birthday'], '%d.%m.%Y')
            
        if calendar.isleap(user['birthday'].year) and not calendar.isleap(date_now.year):
            user['birthday'] = user['birthday'] + timedelta(days=1)
                                         
        if date_start.year != date_end.year and date_start.month != user['birthday'].month:
            birthday = user['birthday'].date().replace(year=date_end.year)
        else:
            birthday = user['birthday'].date().replace(year=date_start.year) 
        
        if date_start <= birthday <= date_end:                 
            if birthday.weekday() in [5, 6]:
                weekday = 0
            else:
                weekday = birthday.weekday()
            birthdays[weekday].append(name)

    birthdays = dict(sorted(birthdays.items()))
     
    for weekday, names in birthdays.items():       
        weekday_name = weekday_names[weekday]
        result[weekday_name] = names

    return result


# Приклад використання
users = [
    {'name': 'John', 'birthday': datetime(1977, 7, 5)},
    {'name': 'Alice', 'birthday': datetime(1983, 7, 7)},
    {'name': 'Bob', 'birthday': '04.07.1986'},
    {'name': 'Emma', 'birthday': datetime(2004, 6, 28)},
    {'name': 'Sam', 'birthday': datetime(1986, 7, 4)},
    {'name': 'Linda', 'birthday': datetime(2001, 12, 30)},
    {'name': 'Tom', 'birthday': datetime(1993, 1, 2)},
    {'name': 'Bill', 'birthday': datetime(2000, 2, 29)}
]

if __name__ == '__main__':
    for weekday, names in get_birthdays_per_week(users).items():       
        print(f"{weekday}: {', '.join(names)}")
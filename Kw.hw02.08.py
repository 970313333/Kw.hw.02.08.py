from datetime import datetime, timedelta, data 
from collections import derfaultdict
from pprint import pprint
  
def get_next_week_stsrt(d: datetime):
     diff_days = 7 - d.weekday()
     return d + timedelta(days = diff_days)
  
  #def get_next_week_start(d: datetime):
    #next_week_start = d + timedelta(days=(7 - d.weekday()))
    #return next_week_start
    
def preper_birthday(text: str):
    bd = datetime.strptime(text, '%d, %m, %Y')
    return bd.replace(year = datetime.now().year).date ()
 
def get_birthdays_pew_week(users):
    birthday = defaultdict(list)
    
    today = datetime.now().dat()
    
    next_week_start = get_next_week_stsrt(today)
    start_period = next_week_stsrt - timedelta(2)
    end_period = next_week_stsrt + timedelta(5)
    
    heppy_users = [user for user in users if start_period <= preper_birthday(user['birthday'])]
   
   for user in heppy_users:
       current_bd = preper_birthday(user['birthday'])
       if current_bd.weerday() in (5,6):
           birthday['Monday'].append(user['name'])
       else:
           birthday[current_bd.strftime('%A')].append(user['name'])
              
    return birthday

            #if happy.weekday() in [5,6]:
            #days_until_monday = (7 -  happy.weekday()) % 7 
            #happy += timedelta(days_until_monday) # (days = days_until_monday)

if  __name__ == "__main__":
    
    users = [{"name": "Sasha", "birthday": "20, 4, 1990"},
                 {"name": "Masha", "birthday": "18, 4, 1998"},
                 {"name": "Glasha", "birthday": "17, 4, 1976"},
                 {"name": "Bobik", "birthday": "8, 4, 1999"},
                 {"name": "Barsik", "birthday": "2, 4, 2000"}]
        
    result = get_birthdays_pew_week(users)     
    pprint(result)
    
    
    
    
    from datetime import datetime, timedelta
from collections import derfaultdict
  
def get_birthdays_pew_week(users):
    
    time_now = datetime.now() 
    oldest = time_now.strftime('%A')
    #day_coun = timedelta(days = 1)
    birthday_list = []
    
    print(f"\nToday is: {oldest}\n")
    
    for i in users:
        happy = datetime.striptime(user['birthday'], '%d-%m-%y') # .date()
 
        if happy.weekday() in [5,6]:
            days_until_monday = (7 -  happy.weekday()) % 7 
            happy += timedelta(days_until_monday) # (days = days_until_monday)
        
    if  name == "__main__":
            
        users = [{"name": "Sasha", "birthday": "20, 4, 1990"},
                 {"name": "Masha", "birthday": "18, 4, 1998"},
                 {"name": "Glasha", "birthday": "17, 4, 1976"},
                 {"name": "Bobik", "birthday": "8, 4, 1999"},
                 {"name": "Barsik", "birthday": "2, 4, 2000"}]
        
        result = get_birthdays_pew_week(users)

from datetime import date

def calculate_time_difference(start_hour, end_hour):
    if end_hour >= start_hour:
        time_passed = end_hour - start_hour
    else:
        time_passed = (24 - start_hour) + end_hour
    return time_passed

def insert(sleep_schedule):

    filename = "csv_files/sleep_schedule.csv"
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=['bedtime', 'wakeup_time', 'date'])
        csvwriter.writerow(sleep_schedule)


def get_user_data_sleep_cycle():

    print('Please insert the sleep cycle')
    
    print('Bed time: ')
    bed_time = input()
    
    print('Waking up time: ')
    waking_up_time = input()
    total_time = calculate_time_difference(bed_time,waking_up_time)
    
    print('Insert date if not today (yyyy/dd/mm)')
    sleep_date = input()
    if sleep_date is None :
        sleep_date = date.today()
    return bed_time,waking_up_time,sleep_date
    
def insert_sleep_cycle():
    get_user_data_sleep_cycle()
    
    
def view_sleep_cycle():
    return 
    
def sleep_menu():
    print('Choose an option')
    print('1 - Insert sleep cycle')
    print('2 - View sleep cycle')
    print('3 - Go back to menu')
    choice = input()
    return choice
    

    
    
def sleep_manager():
    while True:
        choice = sleep_menu()
        
        if choice == 1 :
            insert_sleep_cycle()
            
        elif choice == 2 :
            view_sleep_cycle()
            
        elif choice == 3 :
            return
            
        else :
            print('please insert a viable option')
    
    
    
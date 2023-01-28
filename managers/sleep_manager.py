
from datetime import date
import csv 


def calculate_time_difference(start_hour, end_hour):
    if end_hour >= start_hour:
        time_passed = end_hour - start_hour
    else:
        time_passed = (24 - start_hour) + end_hour
    return time_passed


def get_user_input_sleep_cycle():

    print('Please insert the sleep cycle')
    
    print('Bed time: ')
    bed_time = int (input())
    
    print('Waking up time: ')
    waking_up_time = int (input())
    
    total_time = calculate_time_difference(bed_time,waking_up_time)
    
    print('Insert date if not today (yyyy/dd/mm)')
    sleep_date = input()
    
    if sleep_date is '' :
        sleep_date = date.today()
        
    return bed_time,waking_up_time,sleep_date,total_time


def insert_sleep_cycle_to_dataset(sleep_schedule):

    filename = "csv_files/sleep_schedule.csv"
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(sleep_schedule)
  
    
def insert_sleep_cycle():

    user_data = get_user_input_sleep_cycle()
    print(user_data)
    insert_sleep_cycle_to_dataset(user_data)
    
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
        
        if choice == '1' :
            insert_sleep_cycle()
            
        elif choice == '2' :
            view_sleep_cycle()
            
        elif choice == '3' :
            return
            
        else :
            print('Please insert a viable option')
    
    
    
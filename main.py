


import csv
import subprocess
import sys


sys.path.insert(1, 'Desktop/coding projects/manager_2000/scripts')

import sleep_schedule 

def productivity_tracker():
    return


def dictionary():
    return




while True:
    print('Choose a thing')
    print('1 - insert sleep cycle')
    print('2 - calculate food program')
    print('3 - productivity tracker')
    print('4 - close')

    choice = input()

    if choice == '4':
        break
    elif choice == '1':  # sleep cycle
        sleep_schedule.sleep_manager()

    elif choice == '2':  # calculate food program
        insert_sleep_cycle()

    elif choice == '3':  # productivity tracker
        productivity_tracker()

    elif choice == '4':  # dictionary
        dictionary()

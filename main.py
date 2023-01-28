


import csv
import subprocess
import sys
from managers import sleep_manager



def productivity_tracker():
    return


def dictionary():
    return




while True:
    print('Choose a thing')
    print('1 - Sleep manager')
    print('2 - Diet manager')
    print('3 - Task manager')
    print('4 - Dictionary')
    print('5 - close')

    choice = input()

    if choice == '1':
        sleep_manager.sleep_manager()

    elif choice == '2':  
        insert_sleep_cycle()

    elif choice == '3':  
        productivity_tracker()

    elif choice == '4': 
        dictionary()
        
    elif choice == '5': 
        break

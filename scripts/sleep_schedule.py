


def calculate_time_difference(first_time, second_time):
    if first_time > 12:
        first_time = 24 - first_time
    else:
        first_time *= -1
    return second_time + first_time


def insert(sleep_schedule):
    # Name of CSV file
    filename = "csv_files/sleep_schedule.csv"

    # Writing to CSV file
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=['bedtime', 'wakeup_time', 'date'])
        csvwriter.writerow(sleep_schedule)


def insert_sleep_cycle():
    print('Please insert the sleep cycle')
    print('Bed time: ')
    bed_time = input()
    print('Waking up time: ')
    waking_up_time = input()
    total_time = calculate_time_difference(bed_time,waking_up_time)
    print('Insert date if not today (dd/mm/yyyy)')
    date = input()

    return
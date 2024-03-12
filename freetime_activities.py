import sys
import random as rand

def add_activity():
    reading = sys.argv[1]
    activities = []
    input_file = open(reading, "r")
    for line in input_file:
        activities.append(line)
    while True:
        activity = input('Enter another activity: ')
        if activity in activities:
            print('Already have it. ')
        else:
            activities.append(activity)
            input_file = open(sys.argv[1], 'w')
            for activity in activities:
                input_file.write(f'{activity}\n ')
        if activity == '':
            break
    return activities



def main():
    reading = sys.argv[1]
    activities = []
    input_file = open(reading, "r")
    for line in input_file:
        activities.append(line)
    answer = input('What would you like to do: add activities or see activities? ')
    if answer == 'add activities':
        add_activity()
    if answer == 'see activities':
        reading = sys.argv[1]
        activities = []
        input_file = open(reading, "r")
        for line in input_file:
            activities.append(line)
        for activity in activities:
            print(f'{activity}\n')

if __name__ == '__main__':
    main()
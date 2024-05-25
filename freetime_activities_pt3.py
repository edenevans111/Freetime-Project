from freetime_activities_pt2 import Activities
import random


def readlines(input_file):
    with open(input_file) as file:
        return file.readlines()

def make_class(item):
    instance = Activities(f'{item}')
    return instance

def main():
    free_times = readlines('list_of_activities.csv')
    activities = {activity.lower(): make_class(activity) for activity in free_times}
    answer = input('What would you like to do?:\n'
                   'Generate activity\n'
                   'Show list of activities\n')
    if answer == 'Generate activity':
        decision = random.choice(free_times)
        print(f'{decision}')
        next = input('What now?')
        if next == 'finished':
            activities[decision.lower()].new_note()
            activities[decision.lower()].print_all_notes()

# Tomorrow I should work on making the html page for this project



if __name__ == '__main__':
    main()
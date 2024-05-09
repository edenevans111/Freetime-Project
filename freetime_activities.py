import freetime_activities_pt2
import random

def make_list():
    activities = []
    while True:
        activity = input('Add activity: ')
        if activity == '':
            break
        else:
            activities.append(activity)
    return activities
# I think we also need a function that will turn each item in the list to classes

def main():
    activities = make_list()
    answer = input('What would you like to do?:'
                   'Generate activity'
                   'Show list of activities')
    if answer == 'Generate activity':
        random.choice(activities)
        print()
    # we want this one to generate an activity from the list
    # then we want it to print that activity and its note

if __name__ == '__main__':
    main()
from freetime_activities_pt2 import Activities
import random


def readlines(input_file):
    with open(input_file) as file:
        return file.readlines()

def make_classes(lst):
    for item in lst:
        note = input(f'What is the note for {item}? \n')
        instance = Activities(item, note)

def main():
    free_times = readlines('list_of_activities.csv')
    make_classes(free_times)
    answer = input('What would you like to do?:\n'
                   'Generate activity\n'
                   'Show list of activities\n')
    if answer == 'Generate activity':
        decision = random.choice(free_times)
        print(f'{decision}')
        if input == '':
            new_note = input(f'Enter a new note for {decision} : ')
            Activities.new_note(Activities, f'{new_note}')
            Activities.print_all_notes(Activities, )

if __name__ == '__main__':
    main()
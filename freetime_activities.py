from freetime_activities_pt2 import Activities
import random

def make_list(): # This whole thing works for making the list
    lst = []
    while True:
        item = input('Add activity: ')
        if item == '':
            break
        else:
            lst.append(item)
    return lst

def write_lines(lst): # I need to test this to make sure that it works
    output_filename = 'list_of_activities.csv'
    with open(output_filename, 'w') as file:
        for item in lst:
            file.write(f'{item}\n')
    return output_filename

def make_classes(lst):
    for item in lst:
        note = input(f'What is the note for {item}? \n')
        instance = Activities(item, note)



def main():
    free_times = make_list()
    write_lines(free_times)
    # I think maybe it would be a good idea to have a different file make the list
    # then the one that does stuff with the list will
    make_classes(free_times)
    answer = input('What would you like to do?:\n'
                   'Generate activity\n'
                   'Show list of activities\n')
    if answer == 'Generate activity':
        decision = random.choice(free_times)
        print(Activities.print_activty_note(f'{decision}'))
    # then we want it to print that activity and its note

if __name__ == '__main__':
    main()
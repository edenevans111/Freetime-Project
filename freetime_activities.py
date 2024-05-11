import freetime_activities_pt2 as activities
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
        instance = activities(f'{item}') # Need to figure out the problem here

# I think we also need a function that will turn each item in the list to classes

def main():
    free_times = make_list()
    write_lines(free_times)
    answer = input('What would you like to do?:\n'
                   'Generate activity\n'
                   'Show list of activities\n')
    if answer == 'Generate activity':
        random.choice(free_times)
        print(random.choice(free_times)) # this should print the activity class and last note
    # we want this one to generate an activity from the list
    # then we want it to print that activity and its note

if __name__ == '__main__':
    main()
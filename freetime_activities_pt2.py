import sys
#for this file I need to have it read the file made in pt1
#then I need it to randomly come up with one of the activities
#I would also like to have it save a note for each activity
#about where I left off the last time I did it
def read_file(input):
    filename = input
    input_file = open(filename, 'r')
    activities = []
    for line in input_file:
        activity = input_file.readline()
        activities.append(line)
    return activities

def get_activity(lst):
    pass

def main():
    print(read_file(sys.argv[1]))

if __name__ == '__main__':
    main()
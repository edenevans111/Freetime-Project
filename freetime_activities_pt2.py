class Activities:
    all_activities = []

    def __init__(self, activity):
        self.activity = activity
        self.notes = []
        Activities.all_activities.append(self.activity)

    def new_note(self, note): #need to be sure there is a note before printing
        self.notes.append(note)

    def print_all_notes(self):
        for note in self.notes:
            return f'{self.activity} : {note}\n'

    def print_all_activities(self):
        for self.activity in Activities.all_activities:
            print(self.activity)

    def delete_activity(self, activity):
        Activities.all_activities.remove(f'{activity}')
        del self
        print(f'{activity} has been deleted')

    def print_activty_note(self, activity):
        print(f'{activity} : {self.notes[-1]}')
    def __str__(self):
        if self.notes[-1]:
            return f'{self.activity} : {self.notes[-1]}'
        else:
            return f'{self.activity}'
    def __repr__(self):
        return f'{self.activity}, {self.notes}'



def main():
    print('view activities\n'
               'add activity\n'
               'delete activity\n'
                "view activity's notes\n"
                'find activity\n')
    answer = input('Which would you like to do?\n')
    if answer == 'view activities':
        for activity_obj in Activities.all_activities:
            print(activity_obj)
    if answer == 'add activity': #this is where a new activity is added with a note
        new_activity = input('What is the new activity?')
        new_activity = Activities(new_activity)
        new_note_obj = input(f'What is the note for {new_activity}')
        Activities.new_note(new_note_obj)
    else:
        print('You have not written programming for that yet')



if __name__ == '__main__':
    main()

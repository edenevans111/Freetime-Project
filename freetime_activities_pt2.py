class Activities:
    all_activities = []

    def __init__(self, activity): # This works
        # This should take in an activity and then ask for the first note
        self.activity = activity
        note = input(f'What is the first note for {self.activity}? \n')
        self.notes = []
        self.notes.append(note)
        Activities.all_activities.append(self.activity)
        print('Added', self.activity)

    def new_note(self): # This works
        note = input('Enter the new note: \n')
        self.notes.append(note)

    def print_all_notes(self): # This works
        print(f'{self.activity} : \n')
        for note in self.notes:
            print(f'{note}')

    def print_all_activities(self): # Don't think I need this
        for self.activity in Activities.all_activities:
            print(self.activity)

    def delete_activity(self, activity): # Don't think I need this either
        Activities.all_activities.remove(f'{activity}')
        del self
        print(f'{activity} has been deleted')

    def __str__(self):
        if self.notes:
            return f'{self.activity} : {self.notes[-1]}'
        else:
            return f'{self.activity}'
    def __repr__(self):
        return f'{self.activity}, {self.notes}'



def main():
    crocheting = Activities('Crocheting')
    crocheting.new_note()
    crocheting.print_all_notes()



if __name__ == '__main__':
    main()

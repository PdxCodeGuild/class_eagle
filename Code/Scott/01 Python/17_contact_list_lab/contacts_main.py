import json

class ContactList:
    
    def __init__(self):
        self.contacts = []

    def load(self):
        # load contacts from a file
        with open('contacts.json', 'r') as f: # open file to read
            file_data = json.load(f) # Turn into python dict from string
        self.contacts = file_data['contacts'] # only take the contacts value in the dictionary
        return self.contacts
    
    def count(self):
        return len(self.contacts)
    
    def save(self):
        data = {'contacts': self.contacts} # append to a greater contacts dictionary
        output_data = json.dumps(data) # turn python dict into json
        with open('contacts.json', 'w') as f: # open file to write
            f.write(output_data) # write to file

    def print(self): # Simple print statement
        print(self.contacts) # TODO format this function so output looks prettier

    def add(self, name, phone_number, email):
        # Create a new dict object
        new_contact = {'name' : name, 
                        'phone_number' : phone_number,
                        'email' : email}
        self.contacts.append(new_contact) # append dict to the list
        return self.contacts
    
    def remove(self, name):
        index_removal = 0 
        for i in range(len(self.contacts)): # run through every index in the list of dicts of contacts
            contact = self.contacts[i] # just to simplify the list into current dict / contact
            if contact['name'] == name: # if the current contact's dict has a name that equals the one we want then...
                index_removal = i # save the index with that name
                break # break for loop
        self.contacts.pop(index_removal) # remove contact from the list
    
    def update(self, old_name, new_name, new_phone_number, new_email):
        # Lines 45-50 have the same structure as the remove function
        index_replacement = 0 
        for i in range(len(self.contacts)):
            contact = self.contacts[i]
            if contact['name'] == old_name:
                index_replacement = i
                break

        # rather than remove the index with the given name, we just replace all the data in that index
        self.contacts[index_replacement]['name'] = new_name 
        self.contacts[index_replacement]['phone_number'] = new_phone_number
        self.contacts[index_replacement]['email'] = new_email


contact_list = ContactList() # create an instance of our class
contact_list.load()
print(contact_list.load())
print('Welcome to the Contact List App (CLA)')
while True:
    command = input('Enter a command: ')
    if command == 'load':
        contact_list.load()
        print(f'Loaded {contact_list.count()} contacts.')
    elif command == 'save':
        contact_list.save()
        print(f'Saved {contact_list.count()} contacts.')
    elif command == 'print':
        contact_list.print()
    elif command == 'add':
        print('Enter info of contact to add:')
        name = input('Name: ')
        phone_number = input('Phone Number: ')
        email = input('Email: ')
        contact_list.add(name, phone_number, email)
    elif command == 'remove':
        name = input('Name of contact to remove: ')
        contact_list.remove(name)
    elif command == 'update':
        print('Enter info of contact to add:')
        old_name = input('Name of contact to update: ')
        new_name = input('New Name: ')
        new_phone_number = input('New Phone Number: ')
        new_email = input('New Email: ')
        contact_list.update(old_name, new_name, new_phone_number, new_email)
    elif command == 'help':
        print('Available commands:')
        print('load   - load all contacts from the file')
        print('save   - save contacts to a file')
        print('print  - print all contacts')
        print('add    - add a new contact')
        print('remove - remove a contact')
        print('update - update a contact')
        print('exit   - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
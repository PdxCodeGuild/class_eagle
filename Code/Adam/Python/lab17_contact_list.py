'''
Lab 17: Contact List
'''

import json


class ContactList:
    
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.contacts = []
    
    # load contacts from a file
    def load(self):
        # 1) open 'contacts.json' with option 'r' for read
        with open('./Code/Adam/contacts.json', 'r') as file:
        # 2) get the text from the file
            text = file.read()
        # 3) convert the text into a python dictionary (json.loads)
            data = json.loads(text)
        # 4) get the list of contacts out of the dictionary
        # 5) assign the list of dictionaries to self.contacts
        self.contacts = data['contacts']
    
    # return the number of contacts
    def count(self):
        return len(self.contacts)
    
    # save contacts to a file
    def save(self):
        # 1) open 'contacts.json' with open 'w' for write
        with open('./Code/Adam/contacts.json', 'w') as file:
        # 2) put self.contacts in a dictionary with the key 'contacts'
        # 3) convert the dictionary to a json string (json.dumps)
        # 4) write the json string to the file
            ...

    # print out all the contacts
    def print(self):
        # loop over self.contacts
        for contact in self.contacts:
        # print the information for each contact on a separate line
            print(f'''
            Name: {contact.name}
            Phone Number: {contact.phone_number}
            Email: {contact.email} 
            ''')

    def add(self, name, phone_number, email):
        # create a new dictionary using the 3 parameters
        # add the new dictionary to self.contacts
        self.contacts.append(name, phone_number, email)
    
    # remove the contact from our contact list
    def remove(self, name):
        # find the contact in self-contacts with the given name
        # remove the element at that index
        name = self.contacts[name]
        ...
    
    # update the contact with new info
    def update(self, old_name, new_name, new_phone_number, new_email):
        # find the contact in self.contacts with the given old_name
        # set that contacts' name, phone number, etc to the given values
        ...
    

contact_list = ContactList() # create an instance of our class
contact_list.load()
print('Welcome to the Contact List App (CLA)')
while True:
    command = input('Enter a command: ')
    if command == 'load':
        contact_list.load()
        print(f'Loaded ${contact_list.count()} contacts.')
    elif command == 'save':
        contact_list.save()
        print(f'Saved ${contact_list.count()} contacts.')
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
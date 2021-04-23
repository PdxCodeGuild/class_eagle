import json
from datetime import datetime

class ContactList:
    
    def __init__(self):
        self.contacts = []
        self.activity_log = []

    def load(self):
        # load contacts from a file
        with open('contacts.json', 'r') as file:
            text = file.read()
        self.contacts = json.loads(text)

    def count(self):
        # return the number of contacts
        con_count = len(self.contacts['contacts'])
        return con_count
    
    def save(self):
        # save contacts to a file
        with open('contacts.json', 'w') as file:
            data_json = json.dumps(self.contacts, indent=4)
            file.write(data_json)
        self.activity_log.append(f'Contacts saved. @ {datetime.now()}')

    def print(self):
        # print out all the contacts
        for contact in self.contacts['contacts']:
            print(f'''
            Name: {contact['name']}
            Phone number: {contact['phone_number']}
            E-Mail: {contact['email']}
            ''')

    def add(self, name, phone_number, email):
        # add a new todo item
        self.contacts['contacts'].append({
            'name': name,
            'phone_number': phone_number,
            'email' : email
        })
        self.activity_log.append(f'Added {name} to contacts list. @ {datetime.now()}')
    
    def remove(self, name):
        # remove the contact from our contact list
        for i in range(len(self.contacts['contacts'])):
            if name in self.contacts['contacts'][i]['name']:
                del self.contacts['contacts'][i]
        self.activity_log.append(f'Removed {name} from contacts list.  @ {datetime.now()}')
    
    def update(self, old_name, new_name, new_phone_number, new_email):
        # update the contact with new info
        for i in range(len(self.contacts['contacts'])):
            if old_name in self.contacts['contacts'][i]['name']:
                self.contacts['contacts'][i]['name'] = new_name
                self.contacts['contacts'][i]['phone_number'] = new_phone_number
                self.contacts['contacts'][i]['email'] = new_email
        self.activity_log.append(f'Updated {old_name} to {new_name}. @ {datetime.now()}')

    def log(self):
        for activity in self.activity_log:
            print(activity)
    
contact_list = ContactList() # create an instance of our class
contact_list.load()
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

    elif command == 'log':
        contact_list.log()

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

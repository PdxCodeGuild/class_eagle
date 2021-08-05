import json

class ContactList:

    def __init__(self):
        self.contacts = []

    def load(self):
        # load contacts from a file
        with open('cont_dict.json', 'r')as file:
            text = file.read()
        text_dict = json.loads(text)
        self.contacts = text_dict['contacts']
        # print(self.contacts)

    def count(self):
        # return the number of contacts
        return len(self.contacts)

    def save(self):
        # save contacts to a file
        contacts_dict = {'contacts': self.contacts}
        contacts_dict_str = json.dumps(contacts_dict, indent=4)
        with open('cont_dict.json', 'w')as file:
            file.write(contacts_dict_str)

    def print(self):
        # print out all the contacts
        print(self.contacts)

    def add(self, name, phone_number, email):
        # add a new todo item
        new_contact ={
            'name': name,
            'phone_number': phone_number,
            'email': email
        }
        self.contacts.append(new_contact)

    def remove(self, name):
        # remove the contact from our contact list
        for i in range(len(self.contacts)):
            if name in self.contacts[i]['name']:
                del(self.contacts[i])

    def update(self, old_name, new_name, new_phone_number, new_email):
        # update the contact with new info
        for i in range(len(self.contacts)):
            if old_name in self.contacts[i]['name']:
                self.contacts[i]['name']=new_name
                self.contacts[i]['phone_number']=new_phone_number
                self.contacts[i]['email']=new_email



contact_list = ContactList()  # create an instance of our class
contact_list.load()
print(contact_list.count())
print(contact_list.contacts[0])
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


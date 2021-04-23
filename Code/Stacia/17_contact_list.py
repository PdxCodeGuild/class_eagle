import json

def __init__(self):
    self.json = r'C:\Users\16616\Desktop\pdx_code\code\class_eagle\Code\Stacia\contacts.json'
    
    def load_it(self):
        # load contacts from a file
        self.load_it = json.loads(self.contacts)

    def count(self):
        # return the number of contacts
        self.count = 0
        for i in range (len(self.contacts)):
            self.count +=1
        return self.count
    def save(self):
        # save contacts to a file
        jason.dumps(self.load)

    def print(self):
        # print out all the contacts
        self.print = self.contacts

    def add(self, name, phone_number, email):
        # add a new todo item
        #1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
        self.contacts[name]:{"name": name, "phone_number": phone_number ,"email": email}
        
    def remove(self, name):
        # remove the contact from our contact list
        self.remover = del self.contacts[name]
       
    def update(self, old_name, new_name, new_phone_number, new_email):
        # update the contact with new info
        #{ari_scale[ari_score]['grade_level']}
        self.add = {self.contacts}.update({ 'old_name' : new_name new_phone_number , new email})
       
       
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
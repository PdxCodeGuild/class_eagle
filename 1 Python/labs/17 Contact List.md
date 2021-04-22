

# Contact List

Let's write class for managing a contact list. Copy the code below into a file and fill in the functions. Save the following files below to your personal code folder. To open the file, look at the [File IO doc](../docs/File%20IO.md), to parse the JSON into a Python dictionary, look at [json module](../../0%20General/07%20JSON,%20CSV,%20&%20XML.md#json).


**contacts.json**
```json
{
    "contacts": [{
        "name": "Dora M. Smith",
        "phone_number": "919-781-7129",
        "email": "doramsmith@hotmail.com"
    },{
        "name": "Annette D. Berube",
        "phone_number": "662-319-6954",
        "email": "annette@gmail.com"
    },{
        "name": "Austin M. Pigott",
        "phone_number": "478-777-8878",
        "email": "austin@aol.com"
    }]
}
```

**lab17_contact_list.py**
```python
class ContactList:
    
    def __init__(self):
        self.contacts = []
    

    def load(self):
        # load contacts from a file
        ...
    
    def count(self):
        # return the number of contacts
        ...
    
    def save(self):
        # save contacts to a file
        ...

    def print(self):
        # print out all the contacts
        ...

    def add(self, name, phone_number, email):
        # add a new todo item
        ...
    
    def remove(self, name):
        # remove the contact from our contact list
        ...
    
    def update(self, old_name, new_name, new_phone_number, new_email):
        # update the contact with new info
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
```


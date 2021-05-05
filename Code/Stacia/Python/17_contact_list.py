import json
contact_file = r'C:\Users\16616\pdx_code\class_eagle\Code\Stacia\Python\contacts.json'
class ContactList:
    def __init__(self):
        self.contacts = []
        #self.file = self
    
    def load(self):
    # load contacts from a file
        with open (contact_file, "r") as file:
            text = file.read()
        
        data = json.loads(text) #convert to dictonary
        self.contacts = data["contacts"] #this is a list of dictonarys I can call
        print (data)
        

    def count(self):
        # return the number of contacts
        return len(self.contacts)  
        
       
    def save(self):
        # save contacts to a file
        
        
          # put the loaded  json into a dictonary using "contacts" as a key  
        data = {"contacts" :self.contacts} 
        # convert the dictonary to a json string 
        save_file = json.dumps(data, indent = 4, sort_keys = True) 
        # save the json string in place. 
        with open (contact_file, "w") as file:
            file.write(save_file)

    def print(self):
        #loop over all contacts
        print ()
        for contact in self.contacts: #self.load ["contacts"]:self. load and self. contacts are different fuctions of this class and contacts is not of .load 
    # print out all the contacts
           # print (self.file['name'+'phone_number'+"email"])
            
            
            print ({contact['name']})
            print ({contact['phone_number']})
            print ({contact['email']})
            print ( )
    def add(self, name, phone_number, email):

        print (self.contacts)
        #make a new dictonary 
        new_contact = {   
        'name': name,
        'phone_number': phone_number,
        "email" : email }
        self.contacts.append(new_contact) #add to list of dictonarys. #_______This is not working!!!!

    def remove(self, name):
        # remove the contact from our contact list
        
        for i in range(len(self.contacts)):
            if name == self.contacts[i]["name"]:
                
                self.contacts.remove(self.contacts[i])
            if name not in  self.contacts[i]["name"]:
                print ("name not found")  
                


def update(self, old_name, new_name, new_phone_number, new_email):
        # update the contact with new info
        for i in range(len(self.contacts['contacts'])):
            if old_name in self.contacts['contacts'][i]['name']:
                self.contacts['contacts'][i]['name'] = new_name
                self.contacts['contacts'][i]['phone_number'] = new_phone_number
                self.contacts['contacts'][i]['email'] = new_email

contact_list = ContactList() # create an instance of our class
contact_list.load()
print (contact_list)
 
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
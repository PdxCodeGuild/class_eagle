import requests as req
import json

# I use a class here because I wanted more practice with them after the most recent labs
class FavQuotesInterpreter:
    def __init__(self):
        # Save the general URL and app token for the API
        self.url = 'https://favqs.com/api/' 
        self.auth = 'Token token="b35a811f370be0add8fb856670c711fa"'
    
    def get_qotd(self): # Get the quote of the day (qotd)
        response = req.get(self.url+'qotd', headers={'Authorization': self.auth})
        return response.json() # Returns the python dict of data

    def get_quote_by_keyword(self, page_num, keyword):
        response = req.get(self.url+'quotes', 
        headers={'Authorization': self.auth},
        params={
            'page': page_num,
            'filter': keyword
        })

        return response.json() # Returns the python dict of data on that page for that keyword

    def print_response(self, data, resp_type):  # The response type variable is needed becasue the 2 queries responses have different JSON structures
        output = []
        if resp_type == 'qotd': 
            output.append(f'\n\t"{data["quote"]["body"]}"\n\t\t--{data["quote"]["author"]}\n') # If it's the qotd then just format the quote and return it
        elif resp_type == 'keyword_search':
            for quote in data["quotes"]:
                output.append(f'\n\t"{quote["body"]}"\n\t\t--{quote["author"]}\n') # If it's a keyword search, format each one using a for loop, then append them to the output list
        return output # Returns an array of quotes
    
    def search_engine(self): # Basic function to keep the search engine aspect seperated
        keyword = input('What keyword are you searching by?: ')
        pg_num = 1 # Start on the first page of results
        pg_turn = ''

        while True: 
            pg_data = self.get_quote_by_keyword(pg_num, keyword)  # Make the query using the class
            class_resp = self.print_response(pg_data, 'keyword_search') # Format using the class
            for i in range(len(class_resp)):
                print(str(class_resp[i])) # Convert to string from the class's response

            # Here we change what we print out for all use cases to make it more intuitive to navigate and prevent user input error
            if pg_data['last_page'] == False and pg_num > 1: # Any middle page
                print(f'You are on page {pg_num}')
                pg_turn = input(r'Enter "Next Page", "Last Page", or "Exit" to navigate: ')
            elif pg_data['last_page'] == False and pg_num == 1: # The First page
                print(f'You are on page {pg_num}')
                pg_turn = input(r'Enter "Next Page" or "Exit" to navigate: ')
            elif pg_data['last_page'] == True and pg_num == 1: # The First AND Last Page
                print(f'You are on the only page with results')
                pg_turn = input(r'Enter "Exit" to exit to main menu: ')
            elif pg_data['last_page'] == True: # The Last page
                print(f'You are on page {pg_num} of {pg_num}')
                pg_turn = input(r'Enter "Last Page" or "Exit" to navigate: ')
                
            pg_turn = str(pg_turn)
            pg_turn.lower()

            if pg_turn == 'next page': # If the user specifies to go forward a page
                if pg_data['last_page'] == True: # AND that is the last page
                    print('invalid input') # It's invalid
                else: # AND it's NOT the last page
                    pg_num += 1 # move to the next page
                    continue # go to top of while loop (ln 42)
            elif pg_turn == 'last page': # If the user specifies to go back a page
                if pg_num == 1: # AND we are on the first page
                    print('invalid input') # It's invalid
                else: # AND it's NOT the first page we're on
                    pg_num -= 1 # move back a page
                    continue # go to top of while loop (ln 42)
            elif pg_turn == 'exit': # If the use specifies to exit
                break # break (Which exits the whole function because there's nothing after this while loop)
            else: # Catchall for any other invalid input
                print('invalid input')

## class END here

fqi = FavQuotesInterpreter() # Create local version of class

# REPL for function input
while True:
    # Specifiy user's choice and format their response into a string
    user_choice = input(r'Enter "QOTD" for the quote of the day, "Search" to search via keyword, or "Exit" for exiting the app: ') 
    user_choice = str(user_choice)
    user_choice.lower()

    if user_choice == 'qotd': # IF they want the quote of the day
        class_resp = fqi.print_response(fqi.get_qotd(), 'qotd') # Then get the quote and print response functions from the class
        print(str(class_resp[0])) # Format response from class so we can print it
    elif user_choice == 'search': # IF they want to search via keyword
        fqi.search_engine() # THEN run the search_engine function
        continue # And when they get back, GO TO top of this while loop (ln 86)
    elif user_choice == 'exit': # IF they want to exit the app
        print('Goodbye!') # Say Adios!
        break # Leave this while loop (This ends the script because there is nothing after this while loop in the script)
    else: # Catchall for any other invalid input
        print('invalid input')



# Example Response from get_qotd() function
# {
#     "qotd_date":"2021-04-27T00:00:00.000+00:00",
#     "quote": {
#         "id":26539,
#         "dialogue":false,
#         "private":false,
#         "tags":
#             ["god","life","religion"],
#         "url":"https://favqs.com/quotes/albert-camus/26539-i-would-rathe-",
#         "favorites_count":2,
#         "upvotes_count":1,
#         "downvotes_count":0,
#         "author":"Albert Camus",
#         "author_permalink":"albert-camus",
#         "body":"I would rather live my life as if there is a God and die to find out there isn't, than live my life as if there isn't and die to find out there is."
#         }
# }

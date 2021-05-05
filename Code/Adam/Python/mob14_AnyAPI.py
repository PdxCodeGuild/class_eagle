# Mob 14: Any API


import requests
import pprint

search_word = input('What drink would you like? ').lower()

url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?'
params = {'s':search_word}
response = requests.get(url, params = params)
data = response.json()


#pprint.pprint(data)

drink_names = []
drinks = data['drinks']
#pprint.pprint(drinks)
drink_options = {}
for drink in drinks:
    print(drink['strDrink'])
    drink_names.append(drink['strDrink'])          
    ingredient_list = []
    key_ring = list(drink.keys())
    for key in key_ring:
        if 'strIngredient' in key_ring:
            drink_options[drink['strDrink']] = drink['strInstructions']   
#print(drink_names)
#print(drink_options)
#print(key_ring)
    measure_list = []
    for key in key_ring:
        if  "Ingredient" in key:
            ingredient_list.append(drink[key])
        if "Measure" in key:
            measure_list.append(drink[key])
        masterlist =[]
    for i in range(len(ingredient_list)):
        if ingredient_list[i] != None and  measure_list[i] != None:
            temp = ingredient_list[i] + measure_list[i]
            masterlist.append(temp)
    for item in masterlist:
        print(item)
    print(drink['strInstructions'])
    print()

    # for i in range(len(masterlist)):
    drink['ingredients'] = masterlist
    # pprint.pprint(drink)
#print(masterlist)
#pprint.pprint(drink_options)
#print(ingredient_list)
#print(measure_list)           

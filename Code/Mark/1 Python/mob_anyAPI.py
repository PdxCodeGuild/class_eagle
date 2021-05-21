import requests
import pycountry



def get_gen(country_id,name):
    gen_response = requests.get('https://api.genderize.io/', params = {'name': name, 'country_id': country_id})
    gen_data = gen_response.json()
    return gen_data['gender']


def get_age(country_id,name):
    age_response = requests.get('https://api.agify.io/', params = {'name': name, 'country_id' : country_id})
    age_data = age_response.json()
    return age_data['age']


def get_name():
    name_response = requests.get('https://randomuser.me/api/')
    name_data = name_response.json()
    return name_data['results'][0]['name']['first']


while True:
    name = input('Enter your name: ')
    if name == "":
        name = get_name()
    user_nat = []
    user_gen = []
    user_age = []
    nat_response = requests.get("https://api.nationalize.io/", params = {'name': name})
    nat_data = nat_response.json()

    if nat_data['country'] == []:
        print('No country found!')
    else:
        for country in nat_data['country']:
            user_nat.append(country['country_id'])
        break


for nat in user_nat:
    user_gen.append(get_gen(nat, name))
    user_age.append(get_age(nat, name))


for i in range(len(user_nat)):
    nation = pycountry.countries.get(alpha_2 = user_nat[i])
    print(f'In {nation.name}, the age for someone with the name {name} would be {user_age[i]}.Their gender might be {user_gen[i]}.')





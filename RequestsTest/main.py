import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8f17792eb2c71c7020fab13e00ee915a'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
body_create = {
    "name": "Покемончик",
    "photo_id": 10
}
body_change = {
    "pokemon_id": "260670",
    "name": "New pokemon",
    "photo_id": 9
}
body_take = {
    "pokemon_id": "260670"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''pokemon_id = response_create.json()['id']
print(pokemon_id)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

response_take = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_change)
print(response_take.text)
           
           
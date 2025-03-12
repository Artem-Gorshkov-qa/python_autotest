import requests
import pytest 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8f17792eb2c71c7020fab13e00ee915a'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 22619
def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200
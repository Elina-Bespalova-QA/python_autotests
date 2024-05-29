import requests 



URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '83365c3cbf1f8042a691fe94b2225968'
HEADER = {'Content-Type' : 'application/json','trainer_token' : TOKEN,}
id = '27956'

body_registration = {
    "trainer_token": TOKEN,
    "email": "elinagrishentseva@eandex.ru",
    "password": "MaxDar_2708"
}
body_confirmation = {
    "trainer_token": TOKEN   
}

body_create = {
    "name":"Бульбазавр",
    "photo":"https://dolnikov.ru/pokemons/albums/001.png"
}

body_knockout = {
    "pokemon_id":id
}

body_put_pokemons = {
    "pokemon_id": id,
    "name": "lilu",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_add_pokeball = {
    "pokemon_id": id
}


'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons',headers = HEADER, json = body_create )
print(response_create.text)'''


response_put_pokemons = requests.put(url = f'{URL}/pokemons', headers= HEADER, json = body_put_pokemons )
print(response_put_pokemons.text)

response_add_pokeball = requests.post(url= f'{URL}/trainers/add_pokeball', headers= HEADER, json = body_add_pokeball )
print(response_add_pokeball.text)

response_knockout = requests.post(url = f'{URL}/pokemons/knockout', headers = HEADER, json = body_knockout)
print(response_knockout.text)

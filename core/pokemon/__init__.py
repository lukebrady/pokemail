# This file contains functions that reads a random Pokemon to disk and returns the JSON object with its details.
import requests
import random

# read_poke_file reads the list of Pokemon and returns the list.
def read_poke_file():
    # The array that will be returned with the list of Pokemon.
    pokemon = []
    with open('configuration/pokemon_list.txt') as p:
        for line in p:
            pokemon.append(line[:-1])
    return pokemon

# get_random_pokemon chooses a random Pokemon.
def get_random_pokemon(pokemon_list):
    num = random.randint(0, len(pokemon_list) - 1)
    return pokemon_list[num]

# get_pokemon_info retrieves a pokemon's statistics from the pokemon API.
def get_pokemon_info(pokemon):

    # The URL that will be queried.
    url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(str(pokemon).lower())
    print(url)
    # GET the pokemons information.
    try:
        req =requests.get(url=url)
        return req.json()
    except requests.HTTPError as e:
        print(e)
    return None
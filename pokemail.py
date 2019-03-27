#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from core import pokemon
from core import smtp
from core import  pokedb

poke_arr = pokemon.read_poke_file()

users = pokedb.get_all_email()

for user in users:
    p = pokemon.get_random_pokemon(pokemon_list=poke_arr)
    info = pokemon.get_pokemon_info(p)
    smtp.send_pokemon(info['name'],info['sprites']['front_default'],user)
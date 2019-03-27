#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from core import pokemon
from core import smtp

poke_arr = pokemon.read_poke_file()
users = ['lbrad23105@gmail.com']
for user in users:
    p = pokemon.get_random_pokemon(pokemon_list=poke_arr)
    info = pokemon.get_pokemon_info(p)
    smtp.send_pokemon(info['name'],info['sprites']['front_default'],user)
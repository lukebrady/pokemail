#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from core import pokemon

#ps.send_pokemon('h',[])
poke_arr = pokemon.read_poke_file()
p = pokemon.get_random_pokemon(pokemon_list=poke_arr)
info = pokemon.get_pokemon_info(p)

print(info['name'])
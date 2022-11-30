from service.pokeservice import obter_dados_pokemon_id

p, _ = obter_dados_pokemon_id(1)
print(p.estatisticas)
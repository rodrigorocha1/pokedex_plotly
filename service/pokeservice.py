import aiohttp
import asyncio
import time

import requests

from entidades.pokemon import Pokemom
from typing import List

start_time = time.time()


async def get_pokemon(session, url) -> Pokemom:
    async with session.get(url) as resp:
        pokemon = await resp.json()
        pokemon = Pokemom(**pokemon)
        return pokemon


async def get_all_pokemon(inicio, fim) -> List[Pokemom]:
    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        tasks = []
        for number in range(inicio, fim + 1):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            # print(asyncio.ensure_future(get_pokemon(session, url)))
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

        original_pokemon = await asyncio.gather(*tasks)
        fim_time = time.time()
        print(f'Tempo execução assicrona: {fim_time - start_time}')

        return original_pokemon


def obter_dados_pokemon_id(id_pokemon: int) -> Pokemom:
    """
    Faz a chamada da api e retorna em um objeto
    :param id_pokemon: id do pokemon int
    :return: objeto do tipo pokemon
        """

    start_time = time.time()
    url = f'https://pokeapi.co/api/v2/pokemon/{id_pokemon}'

    req = requests.get(url)
    if req.status_code == 404:
        pokemon = ''
    else:
        pokemon = Pokemom(**req.json())
    fim_time = time.time()
    print(f'Tempo execução Normal: {fim_time - start_time}')

    return pokemon, req.status_code

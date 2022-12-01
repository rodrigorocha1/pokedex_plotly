import requests

from entidades.cor_tipo_pokemon import Cor
from typing import Dict, List


class Pokemom:
    def __init__(self, **kwargs):
        self._id = kwargs['id']
        self._name = kwargs['name']
        self._tipos = [tipos['type']['name'] for tipos in kwargs.get('types')]
        self._cor = ''.join([cor.value for cor in Cor if self._tipos[0] in cor.name])
        self._habilidade = [habilidades['ability']['name'] for habilidades in kwargs['abilities']]
        # self._img = kwargs['sprites']['other']['official-artwork']['front_default'] if \
        #     kwargs['sprites']['other']['official-artwork']['front_default'] is not None else kwargs['sprites'][
        #     'other']['home']['front_default']

        self._img = kwargs['sprites']['other']['home']['front_default'] \
            if kwargs['sprites']['other']['home']['front_default'] is not None else \
            kwargs['sprites']['other']['official-artwork']['front_default']

        self._estatisicas = {kwargs['stats'][i]['stat']['name']:
                                 kwargs['stats'][i]['base_stat'] for i in
                             range(len(kwargs['stats']))}

        self._moves = [kwargs['moves'][i]['move']['name'] for i in range(len(kwargs['moves']))]
        # self._locations = self.__get_location(kwargs['location_area_encounters'])
        self._locations = self.__get_location(kwargs['location_area_encounters'])

    def __get_location(self, url: str) -> List[str]:
        req = requests.get(url)

        if req.status_code == 404:
            location = []
        else:  # req.json()['location_area']['name'] for i in range(len(req.json()['location_area']))
            location = req.json()
        return [location[i]['location_area']['name'] for i in range(len(location))]

    @property
    def locations(self):
        return self._locations

    @property
    def moves(self) -> List[str]:
        return self._moves

    @property
    def name(self) -> str:
        return self._name

    @property
    def id(self) -> int:
        return self._id

    @property
    def tipos(self) -> List[str]:
        return self._tipos

    @property
    def img(self) -> str:
        return self._img

    @property
    def cor(self) -> str:
        return self._cor

    @property
    def habilidade(self) -> List[str]:
        return self._habilidade

    @property
    def estatisticas(self) -> Dict[str, int]:
        return self._estatisicas

from entidades.cor_tipo_pokemon import Cor
from app import *
from layouts.gerador_cartoes import gerar_cartoes


def tela_pokemon(lista_pokemons, tipo=None):
    estilo = {'width': '305px',
              'left': '150px',
              'right': '85px',
              'height': '400px',
              }
    if tipo in [cor.name for cor in Cor]:
        return dbc.Row([  # inicio
            dbc.Col(
                dbc.Card(gerar_cartoes(pokemon),
                         style=estilo,
                         color=f'{pokemon.cor}'

                         ), id=f'id_card_{pokemon.id}',
                style={'padding': '10px'},
                width="auto")
            for pokemon in lista_pokemons if tipo in pokemon.tipos]
        )
    return dbc.Row([  # inicio
        dbc.Col(
            dbc.Card(gerar_cartoes(pokemon),
                     style=estilo,
                     color=f'{pokemon.cor}'

                     ), id=f'id_card_{pokemon.id}',
            style={'padding': '10px'},
            width="auto")
        for pokemon in lista_pokemons]
    )

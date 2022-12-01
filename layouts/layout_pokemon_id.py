from dash import html, callback_context, dcc
from dash.dependencies import Input, Output, State
from app import *
from layouts.gerador_cartoes import gerar_cartoes
import dash_bootstrap_components as dbc
from service.pokeservice import obter_dados_pokemon_id


def layout_pokemon_id(id_pokemon: int):
    pokemon, status_code = obter_dados_pokemon_id(id_pokemon)
    if status_code == 404:
        return dbc.Alert(f"Pokemon {id_pokemon} não encontrado", color="danger", id='id_alert'),
    return dbc.Row([  # inicio
        dbc.Col(
            dbc.Card(
                gerar_cartoes(pokemon),
                style={'width': '305px',
                       'left': '450px',
                       'right': '85px',
                       'height': '400px',
                       },
                color=f'{pokemon.cor}'

            ), id=f'id_card_{pokemon.id}',
            style={'padding': '10px'},
            width="auto"
        )
    ]
    )

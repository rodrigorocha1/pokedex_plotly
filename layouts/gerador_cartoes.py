from dash import dcc

from entidades.pokemon import Pokemom
from app import *


def gerar_cartoes(pokemon: Pokemom):
    return [

        dbc.CardImg(src=pokemon.img,
                    id=f'{pokemon.name}',
                    style={'width': '200px',
                           'height': '150px',
                           'margin-left': '50px',
                           'top': '0px'}),
        dbc.CardBody(
            [
                html.H5(f"{pokemon.id} -  {pokemon.name.capitalize()}",
                        className="card-title",
                        title=pokemon.name,
                        id=f'nome_pokemon_{pokemon.id}', ),
                html.P(f"{' - '.join(pokemon.tipos).title()}"),

                html.Div([
                    html.P(f'HP : {pokemon.estatisticas[0]["hp"]}'),
                    dbc.Progress(value=pokemon.estatisticas[0]["hp"],
                                 color="success",
                                 className="mb-3",
                                 style={"width": "141px",
                                        "height": "10px",
                                        "margin-left": "100px",
                                        "margin-top": "10px"}),

                ])

            ],
        )
    ]

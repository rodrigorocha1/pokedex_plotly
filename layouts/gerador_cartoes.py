from dash import dcc, html
from entidades.pokemon import Pokemom
from app import *
import dash_bootstrap_components as dbc


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
                html.H5(f"{pokemon.id}-{pokemon.name.capitalize()}",
                        className="card-title",
                        title=pokemon.name,
                        id=f'nome_pokemon_{pokemon.id}', style={'font-size': '17px', 'text-align': 'justify'}),
                html.P(f"{' - '.join(pokemon.tipos).title()}"),
                dbc.Tabs(
                    [
                        dbc.Tab([
                            dbc.Row(
                                [
                                    dbc.Col(html.Div(f"{chave.upper()} - {valor}"), md=8,
                                            style={'font-size': '12px'}),
                                    dbc.Col(dbc.Progress(value=valor, style={"height": "10px"}), md=4,
                                            style={'margin-top': '5px'})
                                ]
                            ) for chave, valor in pokemon.estatisticas.items()

                        ],
                            label="Stats", label_style={'color': 'black'}),
                        dbc.Tab(pokemon.habilidade, label="Habilites", label_style={'color': 'black'}),
                    ]
                ),
            ],
        )
    ]

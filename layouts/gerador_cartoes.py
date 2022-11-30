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
                        id=f'nome_pokemon_{pokemon.id}', style={'font-size': '18px', 'text-align': 'justify'}),
                html.P(f"{' - '.join(pokemon.tipos).title()}"),
                dbc.Tabs(
                    [
                        dbc.Tab([
                            dbc.Row(
                                [
                                    dbc.Col(html.Div(f"{chave} - {valor}"), md=6,
                                            style={'font-size': '12px',
                                                   'text-align': 'justify'}),
                                    dbc.Col(dbc.Progress(value=valor), md=6,
                                            style={'margin-top': '5px'})
                                ]
                            ) for chave, valor in pokemon.estatisticas.items()

                        ],
                            label="Stats", ),
                        dbc.Tab(pokemon.habilidade, label="Habilites"),
                    ]
                ),
            ],
        )
    ]

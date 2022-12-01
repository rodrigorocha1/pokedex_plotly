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
                                    dbc.Col(html.Div(f"{chave.upper()} - {valor}", id=f'id_stats_name_{chave}'), md=8,
                                            style={'font-size': '12px', 'margin-top': '1px'}),
                                    dbc.Col(
                                        dbc.Progress(value=valor, style={"height": "10px"}, id=f'id_progress_{chave}'),
                                        md=4,
                                        style={'margin-top': '5px'})
                                ]
                            ) for chave, valor in pokemon.estatisticas.items()

                        ],
                            label="Stats", label_style={'color': 'black'}, id='id_label_stats'),
                        # dbc.Tab(pokemon.habilidade, label="Habilites", label_style={'color': 'black'}),
                        dbc.Tab([
                            dbc.Row(
                                [
                                    habilidade.capitalize()
                                ], style={'margin-left': '5px'}, id=f'id_habilidade_{habilidade}'
                            ) for habilidade in pokemon.habilidade
                        ]
                            , label="Habilites", label_style={'color': 'black'}, id='label_habilidade'),
                        dbc.Tab([
                            dbc.Row(
                                [
                                    moves.capitalize()
                                ], style={'margin-left': '5px'
                                          }, id=f'id_moves_{moves}'
                            ) for moves in pokemon.moves
                        ]
                            , label="Moves", label_style={'color': 'black'}, id='label_habilidade',
                            style={"height": "120px", "overflow-y": "auto"}),
                    ]
                ),
            ],
        )
    ]

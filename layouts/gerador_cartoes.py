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
                html.H5(f"{pokemon.id} -  {pokemon.name.capitalize()}",
                        className="card-title",
                        title=pokemon.name,
                        id=f'nome_pokemon_{pokemon.id}', ),
                html.P(f"{' - '.join(pokemon.tipos).title()}"),
                dbc.Tabs(
                    [
                        dbc.Tab([
                            dbc.Row(
                                [
                                    dbc.Col(html.Div("Linha 1"), md=6),
                                    dbc.Col(dbc.Progress(value=2), md=6,
                                            style={'margin-top': '5px'})
                                ]
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(html.Div("Linha 2"), md=6),
                                    dbc.Col(dbc.Progress(value=2), md=6,
                                            style={'margin-top': '5px'})
                                ]
                            )

                        ],

                            label="Stats"),
                        dbc.Tab("tab2_content", label="Habilites"),

                    ]
                    # dbc.Row(
                    #     [
                    #         dbc.Col(html.Div("Linha 1"), md=6),
                    #         dbc.Col(dbc.Progress(value=pokemon.estatisticas[0]["hp"]), md=6, style={'margin-top': '5px'})
                    #     ]
                    # ),
                    # dbc.Row(
                    #     [
                    #         dbc.Col(html.Div("Linha 2"), md=6),
                    #         dbc.Col(dbc.Progress(value=pokemon.estatisticas[0]["hp"]), md=6, style={'margin-top': '5px'})
                    #     ]
                    # ),
                    # dbc.Row(
                    #     [
                    #         dbc.Col(html.Div("Linha 3"), md=6),
                    #         dbc.Col(dbc.Progress(value=pokemon.estatisticas[0]["hp"]), md=6, style={'margin-top': '5px'})
                    #     ]
                    # ),
                    # dbc.Row(
                    #     [
                    #         dbc.Col(html.Div("Linha 4"), md=6),
                    #         dbc.Col(dbc.Progress(value=pokemon.estatisticas[0]["hp"]), md=6, style={'margin-top': '5px'})
                    #     ]
                    # ),
                    # dbc.Row(
                    #     [
                    #         dbc.Col(html.Div("Linha 5"), md=6),
                    #         dbc.Col(dbc.Progress(value=pokemon.estatisticas[0]["hp"]), md=6, style={'margin-top': '5px'})
                    #     ]
                    # ),
                    # dbc.Row(
                    #     [
                    #         dbc.Col(html.Div("Linha 6"), md=6),
                    #         dbc.Col(dbc.Progress(value=pokemon.estatisticas[0]["hp"]), md=6, style={'margin-top': '5px'})
                    #     ]
                ),

                # dbc.Progress(value=pokemon.estatisticas[0]["hp"],
                #              style={"width": "100px",
                #                     "height": "20px",
                #                     "margin-left": "200px",
                #                     "top": "300px"}),

            ],
        )
    ]

from dash import callback_context, dcc
from dash.dependencies import Input, Output, State
from app import *
from entidades.cor_tipo_pokemon import Cor
from layouts.layout_pokemon_padrao import tela_pokemon
from layouts.layout_pokemon_id import layout_pokemon_id
from layouts.barra_lateral import barra_lateral
import dash_bootstrap_components as dbc
from service.pokeservice import get_all_pokemon
from asyncio import run

# =========  Layout  =========== #


app.layout = html.Div([
    dbc.Row([
        barra_lateral,
        dbc.Col([
            html.Div(

                [
                    html.P(id="id_paragrafo",

                           style={"position": "absolute",
                                  "width": "847px",
                                  "height": "50px",
                                  "left": "427px",
                                  "background": "#212946",
                                  "color": "rgba(255, 255, 255, 0.6)",
                                  "top": "0px"}),

                    dbc.Input(id="input_pokemon",
                              placeholder="Buscar Pokémons #0000",
                              type="number",
                              style={"position": "absolute",
                                     "width": "847px",
                                     "height": "50px",
                                     "left": "427px",
                                     "background": "#212946",
                                     "color": "rgba(255, 255, 255, 0.6)",
                                     "top": "121px"}, size='sm'),

                    html.Button("Pesquisar ",
                                id="id_busca_pokemon",
                                style={"position": "absolute",
                                       "width": "95px",
                                       "height": "50px",
                                       "left": "1179px",
                                       "top": "121px",
                                       "background": "#469EF1"}),

                ]
            ),
            html.Div(
                [
                    dcc.Tabs(
                        id='id_tab_tipo_pokemon',
                        value='Pokemons Comuns',
                        parent_className='custon_tabs',
                        children=[
                            dcc.Tab(
                                label='Pokemons Comuns',
                                value='tab-1',
                                id='id_pokemons_comuns'

                            ),
                            dcc.Tab(
                                label='Other Forms',
                                value='tab-2',
                                id='id_other_form'
                            ),
                            dcc.Tab(
                                label='Mega Forms',
                                value='tab-3',
                                id='id_mega_forms'
                            ),
                            dcc.Tab(
                                label='Alola Forms',
                                value='tab-4',
                                id='id_alola_forms'
                            ),
                            dcc.Tab(
                                label='Forms',
                                value='tab-5',
                                id='id_forms'
                            ),
                            dcc.Tab(
                                label='Galar Forms',
                                value='tab-6',
                                id='id_galar_forms'
                            ),
                            dcc.Tab(
                                label='+ Forms',
                                value='tab-7',
                                id='id_more_form'
                            ),
                            dcc.Tab(
                                label='Gmax Forms',
                                value='tab-8',
                                id='id_gmax_form'
                            ),
                            dcc.Tab(
                                label='Hisui Forms',
                                value='tab-9',
                                id='id_hisui_forms'
                            ),
                            dcc.Tab(
                                label='Origin forms ',
                                value='tab-10',
                                id='id_origin_forms'
                            ),

                        ]

                    ),
                    html.Div(id='tabs_pokemon'),

                ],
                id='id_resultado_busca',
                style={"position": "absolute",
                       "width": "1231px",
                       "height": "695px",
                       "left": "280px",
                       "top": "287px",
                       "overflow-y": "scroll",
                       'overflow-x': 'hidden'})
        ], md=10)
    ], id='id_layout_principal'),

], style={"position": "relative",
          "width": "1512px",
          "height": "982px",
          "background": "#121936",
          "box-shadow": "0px 4px 4px rgba(0, 0, 0, 0.25)"},
    id='id_barra_lateral')


@app.callback(Output('tabs_pokemon', 'children'),
              [Input('id_tab_tipo_pokemon', 'value'),
               Input('id_busca_pokemon', 'n_clicks'),
               [Input(f"{cor.name}", "n_clicks") for cor in Cor]],
              State('input_pokemon', 'value')
              )
def render_page_pokemons(tab, *_):
    ctx = callback_context
    value = ctx.states_list[0].get('value')
    if tab == 'tab-1':  # Pokemons Comuns
        if value is None or value == 0 or value == '':
            inicio = 1
            fim = 905

            lista_pokemons = run(get_all_pokemon(inicio, fim))

            return tela_pokemon(lista_pokemons, ctx.triggered_id)
        else:
            return layout_pokemon_id(int(value))
    if tab == 'tab-2':  # Other Forms
        if value is None or value == 0 or value == '':
            inicio = 10001
            fim = 10032

            lista_pokemons = run(get_all_pokemon(inicio, fim))
            return tela_pokemon(lista_pokemons, ctx.triggered_id)
        else:
            return layout_pokemon_id(int(value))
    if tab == 'tab-3':  # Mega Forms
        if value is None or value == 0 or value == '':
            inicio = 10033
            fim = 10090
            lista_pokemons = run(get_all_pokemon(inicio, fim))
            return tela_pokemon(lista_pokemons, ctx.triggered_id)
        else:
            return layout_pokemon_id(int(value))
    if tab == 'tab-4':  # Alola Forms
        if value is None or value == 0 or value == '':
            inicio = 10091
            fim = 10115
            lista_pokemons = run(get_all_pokemon(inicio, fim))
            return tela_pokemon(lista_pokemons, ctx.triggered_id)
        else:
            return layout_pokemon_id(int(value))
    if tab == 'tab-5':  # Forms
        if value is None or value == 0 or value == '':
            inicio = 10116
            fim = 10160
            lista_pokemons = run(get_all_pokemon(inicio, fim))
            return tela_pokemon(lista_pokemons, ctx.triggered_id)
        else:
            return layout_pokemon_id(int(value))
    if tab == 'tab-6':  # Galar Forms
        if value is None or value == 0 or value == '':
            inicio = 10161
            fim = 10180
            lista_pokemons = run(get_all_pokemon(inicio, fim))
            return tela_pokemon(lista_pokemons, ctx.triggered_id)
        else:
            return layout_pokemon_id(int(value))
    if tab == 'tab-7':  # + Forms
        if value is None or value == 0 or value == '':
            inicio = 10182
            fim = 10194
            lista_pokemons = run(get_all_pokemon(inicio, fim))
            return tela_pokemon(lista_pokemons, ctx.triggered_id)
        else:
            return layout_pokemon_id(int(value))
    if tab == 'tab-8':  # Gmax Forms
        if value is None or value == 0 or value == '':
            inicio = 10195
            fim = 10228
            lista_pokemons = run(get_all_pokemon(inicio, fim))
            return tela_pokemon(lista_pokemons, ctx.triggered_id)
        else:
            return layout_pokemon_id(int(value))
    if tab == 'tab-9':  # Hisui Forms
        if value is None or value == 0 or value == '':
            inicio = 10229
            fim = 10244
            lista_pokemons = run(get_all_pokemon(inicio, fim))
            return tela_pokemon(lista_pokemons, ctx.triggered_id)
        else:
            return layout_pokemon_id(int(value))
    if tab == 'tab-10':  # Origin forms
        if value is None or value == 0 or value == '':
            inicio = 10245
            fim = 10249
            lista_pokemons = run(get_all_pokemon(inicio, fim))
            return tela_pokemon(lista_pokemons, ctx.triggered_id)
        else:
            return layout_pokemon_id(int(value))


if __name__ == "__main__":
    app.run_server(port=8051, debug=True)

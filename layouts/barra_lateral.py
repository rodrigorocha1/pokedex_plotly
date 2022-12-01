from dash import html, callback_context
from dash.dependencies import Input, Output, State
from app import *
from entidades.cor_tipo_pokemon import Cor
import dash_bootstrap_components as dbc

barra_lateral = dbc.Col([
    html.Div([

        html.Img(src='assets/Screenshot_1.png',
                 style={"position": "absolute",
                        "height": "53.63px",
                        "left": "49px",
                        "right": "1000px",
                        "top": "27.25px", },
                 id='id_img')
    ]),
    dbc.ButtonGroup(
        [
            dbc.Button(''.join(cor.name).capitalize(),
                       id=f'{cor.name}',
                       style={'background-color': f'{cor.value}'}) for cor in Cor

        ],

        vertical=True,
        style={"top": "200px",
               "left": "60px",
               "width": "150px"}
    )

], md=2,
    style={"position": "absolute",
           "width": "283px",
           "height": "982px",
           "left": "0px",
           "top": "0px",
           "background": "#212946",
           "border-radius": "10px", })



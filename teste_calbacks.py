# Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Read in data and manipulate
who_data = pd.read_csv("https://covid19.who.int/WHO-COVID-19-global-data.csv")
pops = pd.read_csv(
    "https://gist.githubusercontent.com/curran/0ac4077c7fc6390f5dd33bf5c06cb5ff/raw/605c54080c7a93a417a3cea93fd52e7550e76500/UN_Population_2019.csv")

pops = pops[['Country', '2020']]
pops['2020'] = pops['2020'] * 1000

who_data.rename(columns={'New_cases': 'New Cases', 'Cumulative_cases': 'Cumulative Cases', 'New_deaths': 'New Deaths',
                         'Cumulative_deaths': 'Cumulative Deaths'}, inplace=True)

country_choices = who_data['Country'].unique()
metric_choices = who_data.columns[4:]

# Initialize graph
fig = px.line(who_data, x="Date_reported", y="New Cases")

# Define cards
card1 = dbc.Card([
    dbc.CardBody([
        html.H4("Card title", className="card-title", id="card_num1"),
        html.P("Current Population", className="card-text", id="card_text1")
    ])
],
    style={'display': 'inline-block',
           'width': '33.3%',
           'text-align': 'center',
           'color': 'white',
           'background-color': 'rgba(37, 150, 190)'},
    outline=True)

card2 = dbc.Card([
    dbc.CardBody([
        html.H4("Card title", className="card-title", id="card_num2"),
        html.P("This is some card text", className="card-text", id="card_text2")
    ]
    )],
    style={'display': 'inline-block',
           'width': '33.3%',
           'text-align': 'center',
           'color': 'white',
           'background-color': 'rgba(37, 150, 190)'},
    outline=True)

card3 = dbc.Card([
    dbc.CardBody([
        html.H4("Card title", className="card-title", id="card_num3"),
        html.P("This is some card text", className="card-text", id="card_text3")
    ]
    )],
    style={'display': 'inline-block',
           'width': '33.3%',
           'text-align': 'center',
           'color': 'white',
           'background-color': 'rgba(37, 150, 190)'},
    outline=True)

# Define app layout
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Country', value='tab-1', style=tab_style, selected_style=tab_selected_style,
                children=[
                    html.Div([
                        dcc.Dropdown(
                            id='dropdown1',
                            options=[{'label': i, 'value': i} for i in country_choices],
                            value=country_choices[0]
                        )
                    ], style={'width': '50%',
                              'display': 'inline-block',
                              'text-align': 'center'}
                    ),
                    html.Div([
                        dcc.Dropdown(
                            id='dropdown2',
                            options=[{'label': i, 'value': i} for i in metric_choices],
                            value=metric_choices[0]
                        )], style={'width': '50%',
                                   'display': 'inline-block',
                                   'text-align': 'center'}
                    ),
                    html.Div([
                        card1,
                        card2,
                        card3
                    ]),
                    html.Div([
                        dcc.Graph(figure=fig, id='country_plot')
                    ])
                ]),
        dcc.Tab(label='Spread', value='tab-2', style=tab_style, selected_style=tab_selected_style,
                children=[
                    html.P('Some stuff will go here eventually.')

                ])
    ])
])


# @app.callback(
#     Output('card_num1','children'),
#     Output('card_num2','children'),
#     Output('card_num3','children'),
#     Output('card_text1','children'),
#     Output('card_text2','children'),
#     Output('card_text3','children'),
#     Input('dropdown1','value')
# )

# def update_cards(country_select):
#     new_df = who_data[(who_data.Country==country_select)]
#     c_pop = pops[pops.Country==country_select]['2020'].unique()[0]

#     card1 = dbc.Card([
#         dbc.CardBody([
#             html.H4(c_pop, className="card-title",id="card_num1"),
#             html.P(f"Current Population of {country_select}", className="card-text")
#         ])
#     ],
#     style={'display': 'inline-block',
#            'width': '33.3%',
#            'text-align': 'center',
#            'background-color': 'rgba(37, 150, 190)'},
#     outline=True)


@app.callback(
    Output('country_plot', 'figure'),
    Input('dropdown1', 'value'),
    Input('dropdown2', 'value'))
def update_figure(country_select, metric_select):
    new_df = who_data[(who_data.Country == country_select)]
    country_df = pops[pops.Country == country_select]

    fig = px.line(new_df, x="Date_reported", y=metric_select,
                  title=f'<b>{metric_select} of COVID19 for {country_select}</b>',
                  color_discrete_sequence=["red"],
                  labels=dict(Date_reported="Date")
                  )
    fig.update_traces(mode='markers+lines', marker=dict(color="black", size=3), line=dict(width=2))
    fig.update_layout(title={'x': 0.5,
                             'xanchor': 'center',
                             'yanchor': 'top'})

    return fig


app.run_server(host='0.0.0.0', port='8050')
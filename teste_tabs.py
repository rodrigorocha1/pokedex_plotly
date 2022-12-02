from dash import Dash, html, dcc, Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.RangeSlider(1, 905, 100, pushable=99, value=[1, 100], id='my-range-slider', ),
    html.Div(id='output-container-range-slider', style={'color': 'red'})
])


@app.callback(
    Output('output-container-range-slider', 'children'),
    [Input('my-range-slider', 'value')])
def update_output(value):
    print(value)
    valor_inicial = value[0]
    valor_final = value[1]
    if valor_final - valor_inicial <= 105:
        return 'You have selected "{}"'.format(value)
    return 'Escolha valores no intervalo de 1 a 105'

if __name__ == "__main__":
    app.run_server(port=8052, debug=True)

import numpy as np
import plotly.express as px
from dash import Dash, Input, Output, callback_context, dcc, html
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

N = 3

app = Dash(__name__)


def make_figure0(n):
    x = np.linspace(0, 8, 81)
    y = x ** int(n)
    return px.scatter(x=x, y=y)


def make_figure1(n):
    x = np.linspace(0, 8, 81)
    y = x ** int(n)
    return px.scatter(x=x, y=y)


def make_figure2(n):
    x = np.linspace(0, 8, 81)
    y = x ** int(n)
    return px.scatter(x=x, y=y)


app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    dbc.Button(f"x^{i}", id=f"btn-{i}"))
                for i in range(N)
            ]
        ),
        dcc.Graph(id="graph"),
    ]
)


@app.callback(
    Output("graph", "figure"), [Input(f"btn-{i}", "n_clicks") for i in range(N)]
)
def update_graph(*_):
    ctx = callback_context

    print("ctx.triggered", ctx.triggered if ctx.triggered is not None else '')

    if not ctx.triggered:
        raise PreventUpdate
    else:
        n = ctx.triggered[0]["prop_id"].split(".")[0].split("-")[1]
    if n == "0":
        return make_figure0(n)
    if n == "1":
        return make_figure1(n)
    if n == "2":
        return make_figure2(n)


if __name__ == "__main__":
    app.run_server(debug=True)

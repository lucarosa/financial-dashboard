import pandas as pd
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from ..data.loader import DataSchema

from . import ids

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_months: list[str]= data[DataSchema.MONTH].to_list()
    unique_months = sorted(set(all_months))

    @app.callback(
        Output(ids.MONTH_DROPDOWN, "value"),
        [
            Input(ids.SELECT_ALL_MONTHS_BUTTON, "n_clicks"),
            Input(ids.YEAR_DROPDOWN, 'value')
        ],
    )
    def select_all_months(_: int, years: list[str]) -> list[str]:
        filtered_data = data.query("year in @years")
        return sorted(set(filtered_data[DataSchema.MONTH].to_list()))

    return html.Div(
        children=[
            html.H6("Month"),
            dcc.Dropdown(
                id=ids.MONTH_DROPDOWN,
                options=[{"label":month, "value": month} for month in unique_months],
                multi=True,
                value=unique_months
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_MONTHS_BUTTON,
                n_clicks=0,
            )

        ]
    )
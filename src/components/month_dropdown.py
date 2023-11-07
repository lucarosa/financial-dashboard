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
        Input()
    )
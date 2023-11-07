import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from ..data.loader import DataSchema
import plotly.express as px

from . import ids

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "children"),
        Input(ids.YEAR_DROPDOWN, "value")
    )
    def update_bar_chart(years: list[str]) -> html.Div:
        #this function takes as input what is specificed by the Input of the
        #callback above
        filtered_data = data.query("year in @years")
        if filtered_data.shape[0]==0:
            return html.Div("No data selected")

        def create_pivot_table() -> pd.DataFrame:
            pt = filtered_data.pivot_table(
                values=DataSchema.AMOUNT,
                index=[DataSchema.CATEGORY],
                aggfunc="sum",
                fill_value=0
            )
            return pt.reset_index().sort_values(DataSchema.AMOUNT, ascending=False)

        fig = px.bar(
            create_pivot_table(),
            x=DataSchema.CATEGORY,
            y=DataSchema.AMOUNT,
            color=DataSchema.CATEGORY
        )
        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)
    return html.Div(id=ids.BAR_CHART)






# MEDAL_DATA = px.data.medals_long()
# def render(app: Dash) -> html.Div:
#
#     @app.callback(
#         Output(ids.BAR_CHART, "children"),
#         Input(ids.NATION_DROPDOWN, "value")
#     )
#     def update_bar_chart(nations: list[str]) -> html.Div:
#         filtered_data = MEDAL_DATA.query("nation in @nations")
#
#         if filtered_data.shape[0]==0:
#             return html.Div("No data selected")
#
#         fig = px.bar(filtered_data, x='medal', y='count',
#                      color='nation',text='nation')
#         return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)
#     return html.Div(id=ids.BAR_CHART)
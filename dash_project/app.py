import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input
import plotly.express as px



data = pd.read_csv("/home/bull/Documents/bull-analytics/dash_project/data/tiktok_artists.csv")
# data = data.query("type == 'conventional' and region == 'Albany'")
# data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("total_ig_followers", ascending=False ,inplace=True)

app = dash.Dash(__name__)
app.title = "Artist Discovery Tool: MVP"


app.layout = html.Div(
    children=[
        html.H1(
            children="Artist Discovery: MVP",
            style={"fontsize": "48px", "color": "green", 'text-align': 'center'}
        ),
        html.P(
            children="This insights tool analyzes Tiktok's weekly Top 100 Tracks by comparing the number of Instagram followers of each artist.",
            style={"fontsize": "20px", "color": "black", 'text-align': 'center'}
        ),
        html.P(
            children="Week of {}".format(data['added_at'][0]),
            style={"font-size": "30px", "color": "black", 'text-align': 'center', 'font-weight':['bold']}),

        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Artist Popularity* (Based on Spotify's internal ranking system on a scale from 0 to 100)"),
                        dcc.Dropdown(
                            id="career-filter",
                            options=[
                                {"label": stage, "value": stage}
                                for stage in np.sort(data['Popularity-Index'].unique())
                            ],
                            value=">= 90",
                            clearable=False,
                            # className="dropdown",
                        ),
                    ]
                ),
            ]
        ),
     
        html.Div(
            children=dcc.Graph(
                id="ig-chart", config={"displayModeBar": False},
            )

        ),
    ]
)
@app.callback(
    Output("ig-chart", "figure"),
    
        [Input("career-filter", "value")],
        # Input("type-filter", "value"),
        # Input("date-range", "start_date"),
        # Input("date-range", "end_date"),
)
        
def update_charts(stage):
    mask = data['Popularity-Index'] == stage

    
    filtered_data = data.loc[mask, :][:10]
    ig_chart_figure = px.bar(filtered_data, x='artist', y='total_ig_followers',
                            labels={'artist':'Artist', 'total_ig_followers': 'Instagram Followers (1-Week Before Chart Appearance)'

                            },
                            width=1500, height=800
    

    )

    return ig_chart_figure



if __name__ == "__main__":
    app.run_server(debug=True)
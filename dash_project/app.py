import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input


data = pd.read_csv("one_month_trax.csv")
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
            children="This insights tools is designed to analyze Tiktok's Top 100 Weekly chart by identifying the artists with the biggest fanbase on Instagram prior to the record's first occurance on the chart.",
            style={"fontsize": "15px", "color": "black", 'text-align': 'center'}
        ),
        html.P(
            children="From the perspective of talent seekers and A&R professionals, one of the inherent risks when pouring more resources into a client is the possibility that they'll be no one on the other side to receive the creator's message. This tool mitigates that risk by ensuring that there is an existing audience to build off of",
            style={"fontsize": "15px", "color": "black", 'text-align': 'center'}),

        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Career Stage"),
                        dcc.Dropdown(
                            id="career-filter",
                            options=[
                                {"label": stage, "value": stage}
                                for stage in np.sort(data['Career Stage'].unique())
                            ],
                            # value="Indie",
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
    mask = data['Career Stage'] == stage

    
    filtered_data = data.loc[mask, :]
    ig_chart_figure = {
        "data": [
            {
                "x": filtered_data["artist"],
                "y": filtered_data["total_ig_followers"],
                "type": "bar",
                # "hovertemplate": "$%{y:.2f}<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Top Tiktok Artists by Instagram Fanbase",
                # "x": 0.05,
                # "xanchor": "left",
            }
            # "xaxis": {"fixedrange": True},
            # "yaxis": {"tickprefix": "$", "fixedrange": True},
            # "colorway": ["#17B897"],
        }
    }
    return ig_chart_figure



if __name__ == "__main__":
    app.run_server(debug=True)
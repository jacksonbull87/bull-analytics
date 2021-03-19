import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input
import plotly.express as px
import plotly.graph_objects as go



data = pd.read_csv("data/tiktok_artists.csv")
# data = data.query("type == 'conventional' and region == 'Albany'")
# data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("total_ig_followers", ascending=False ,inplace=True)

app = dash.Dash(__name__)
server = app.server
app.title = "Artist Discovery Tool: MVP"


app.layout = html.Div(

    children=[
        html.Div(
            children = [
        # <img src="assets/images/Square_Initials_WhiteonBlack.jpg" alt="A black, brown, and white dog wearing a kerchief">

        html.H1(
            children="Artist Discovery: MVP",
            style={"font-size": "48px", "color": "white", 'text-align': 'center'}
        ),
        html.P(
            children="Social media insights for trending artists on Tiktok's weekly Top 100 Chart",
            style={"font-size": "30px", "color": "white", 'text-align': 'center'}
        ),
        html.P(
            children="Week of {}".format(data['added_at'][0]),
            style={"font-size": "30px", "color": "white", 'text-align': 'center', 'font-weight':['bold']},
        ),
        

            ],
            className="header",
        ),

        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            html.P(
                            children="Stay Tuned for Updates!", className="updatebox-title"),
                            style={"font-size": "30px", "color": "black", 'text-align': 'center'}

                        ),
                    ],
                ),
            ],
            className="updatebox",
        ),

        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            html.P(
                            children="The Dataset", className="databox-title"),
                            style={"font-size": "30px", "color": "black", 'text-align': 'center'}

                        ),
            
                        html.P(
                            children="Consists of tracks that have entered the Top 100 within the last 30 days",
                            style={"fontsize": "28px", "color": "black", 'text-align': 'center',}
                        ),
                    ],
                ),
            ],
            className="databox",
        ),


        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Artist Popularity", className="menu-title",style={"fontsize": "10px", 'text-align': 'center'}),
                        dcc.Dropdown(
                            id="popularity-index",
                            options=[
                                {"label": popularity, "value": popularity}
                                for popularity in np.sort(data['Popularity-Index'].unique())
                            ],
                            value=">= 90",
                            clearable=False,
                            # className="dropdown",
                        ),
            
                        html.P(
                            children="*Based on Spotify's internal ranking system from 0 to 100",
                            style={"fontsize": "10px", "color": "black", 'text-align': 'center'}
                        ),
                    ],
                ),
            ],
            className="menu",
        ),
            
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="ig-chart", config={"displayModeBar": False},
                        figure={
                            "layout":{
                                "title":{
                                    "text": "chart text",
                                },
                            },
                        },
                    ),
                    className="topleftcard",
                    style={'display': 'inline-block'},
                ),
                html.Div(
                    children=dcc.Graph(
                        id="ig_gain", config={"displayModeBar": False},
                        figure={
                            "layout":{
                                "title":{
                                    "text": "chart text",
                                },
                            },
                        },
                    ),
                    className="topmiddlecard",
                    style={'display': 'inline-block'}
                ),
                html.Div(
                    children=dcc.Graph(
                        id="ig_engage", config={"displayModeBar": False},
                        figure={
                            "layout":{
                                "title":{
                                    "text": "chart text",
                                },
                            },
                        },
                    ),
                    className="toprightcard",
                    style={'display': 'inline-block'}
                ),
            ],
            className="wrapper",style={'width': '100%', 'display': 'inline-block'}
        ),
    ],
)
@app.callback(
    [Output("ig-chart", "figure"), Output("ig_gain", "figure"),Output("ig_engage", "figure")],
    
        [Input("popularity-index", "value")],
        # Input("type-filter", "value"),
        # Input("date-range", "start_date"),
        # Input("date-range", "end_date"),
)
        
def update_charts(popularity):
    mask = data['Popularity-Index'] == popularity

    
    filtered_data = data.loc[mask, :][:10]

    

    ig_chart_figure = px.bar(filtered_data.sort_values('total_ig_followers', ascending=False), x='artist', y='total_ig_followers',
                            title = "Top Artists by Total Instagram Followers (Pre-Chart)",
                            # color='artist',
                            labels={'artist':'Artist','total_ig_followers': 'Instagram Followers (1-Week Before Chart Appearance)'

                            },
                            width=500, height=500
    )
    ig_gain_figure = px.bar(filtered_data.sort_values('IG_Follower_Gain-%', ascending=False), x='artist', y='IG_Follower_Gain-%',
                            title = "Top Artists by Percent Instagram Gain (First Week into Chart)",
                            # color='artist',
                            labels={'artist':'Artist','IG_Follower_Gain-%': '% Gain Instagram Followers',

                            },

                            
                            width=500, height=500,
                            
    )
    ig_engage_figure = px.bar(filtered_data.sort_values('ig_eng', ascending=False), x='artist', y='ig_eng',
                            title = "Top Artists by Instagram Engagement (Current)",
                            labels={'artist':'Artist', 'ig_eng': 'Instagram Engagement Ratio',

                            },

                            
                            width=500, height=500,
                            
    )
    

    return ig_chart_figure,ig_gain_figure,ig_engage_figure



if __name__ == "__main__":
    app.run_server(debug=True)
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

data = pd.read_csv("one_month_trax.csv")
# data = data.query("type == 'conventional' and region == 'Albany'")
# data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("total_ig_followers", ascending=False ,inplace=True)

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Artist Discovery: MVP",),
        html.P(
            children="Analyze Weekly Tiktok Data",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["artist"],
                        "y": data["total_ig_followers"],
                        "type": "bar",
                    },
                ],
                "layout": {"title": "Top Tiktok Artists"},
            },
        ),
        # dcc.Graph(
        #     figure={
        #         "data": [
        #             {
        #                 "x": data["Artists"],
        #                 "y": data["Total IG Followers"],
        #                 "type": "bar",
        #             },
        #         ],
        #         "layout": {"title": "Avocados Sold"},
        #     },
        # ),
    ]
)



if __name__ == "__main__":
    app.run_server(debug=True)
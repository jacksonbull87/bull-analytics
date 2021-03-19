from cm_api import get_api_token
from data_agg import *
from cm_config import  config
from helper_funct1 import generate_yesterday_date
from data_agg import collect_artist_sppop
import datetime
import pandas as pd
from graph_maker import make_barplot

#get api token
api_token = get_api_token(config['refresh_token'])

#get yesterday's date
yesterday_date = generate_yesterday_date()

#get tiktok chart
data = get_tiktok_chart_data(api_token, 'tracks', yesterday_date, 'weekly')

#parse tiktok data into dataframe
dataframe = parse_tiktok_data(data)

#get chartmetric id and add to dataframe
dataframe = create_artist_id_feat(api_token, dataframe)

#remove timestamp from `added_at` feature
dataframe['added_at'] = pd.to_datetime(dataframe['added_at']).dt.date

#engineer date feature for 7 days before each record's first occurance on the chart
dataframe = create_before_tiktok_date_feat(dataframe)

#engineer track chart age
dataframe['track_age'] = dataframe['time_on_chart'].apply(lambda x: 'a month' if int(x) <= 30 else ('2 months' if 60 >= int(x) > 30 else 'over 2 months'))

#filter dataset down to 1-month old tracks
young_trax = dataframe.loc[dataframe['track_age'] == 'a month'].reset_index().drop(axis=1, labels='index')

#replace artist names with real artist names
young_trax = collect_true_artist_names(api_token, young_trax)

#collect instagram followers for `Before_Tiktok_Date`
young_trax = create_instagram_followers_before_feat(api_token, young_trax)

#Collect currect spotify popularity metric for each artist
young_trax = collect_artist_sppop(api_token, young_trax)

#Career Stage feature
young_trax['Career Stage'] = young_trax['artist_pop'].apply(lambda x: 'Established' if x >= 88 else ('Emerging' if x >= 80 else 'Indie'))

make_barplot(young_trax, 'artist', 'total_ig_followers')


if __name__ == "__main__":
    app.run_server(debug=True)


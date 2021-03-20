from cm_api import get_api_token
from data_agg import *
from cm_config import  config
from helper_funct1 import generate_yesterday_date
from data_agg import collect_artist_sppop
from data_agg import create_artist_ig_engagement_feat
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

#engineer track chart age
dataframe['track_age'] = dataframe['time_on_chart'].apply(lambda x: 'a month' if int(x) <= 30 else ('2 months' if 60 >= int(x) > 30 else 'over 2 months'))

#filter dataset down to 1-month old tracks
young_trax = dataframe.loc[dataframe['track_age'] == 'a month'].reset_index().drop(axis=1, labels='index')

#engineer date feature for 7 days before each record's first occurance on the chart
young_trax = create_before_tiktok_date_feat(young_trax)

#replace artist names with real artist names
young_trax = collect_true_artist_names(api_token, young_trax)

#collect instagram followers for `Before_Tiktok_Date`
young_trax = create_instagram_followers_before_feat(api_token, young_trax)

#Collect currect spotify popularity metric for each artist
young_trax = collect_artist_sppop(api_token, young_trax)

#Career Stage feature
young_trax['Popularity-Index'] = young_trax['artist_pop'].apply(lambda x: '>= 90' if x >= 90 else ('>=80' if x >= 80 else '< 80'))

#adding date for 7 days after record's first chart appearance
young_trax['Week_In_Chart_Date'] = young_trax['Before_Tiktok_Date'] + datetime.timedelta(days=14)

young_trax = create_instagram_followers_after_feat(api_token, young_trax)

#percent gain in IG followers
young_trax['IG_Follower_Gain-%'] = (young_trax['ig_followers_afters'] - young_trax['total_ig_followers'])/young_trax['total_ig_followers']*100

#adding instagram engagement before tiktok chart
young_trax = create_artist_ig_engagement_feat(api_token, young_trax)

#save dataset
young_trax.to_csv('/home/bull/Documents/artist-discovery-app/data/tiktok_artists.csv', index_label='index')

# make_barplot(young_trax, 'artist', 'total_ig_followers')





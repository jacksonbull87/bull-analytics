

def get_tiktok_chart_data(api_token, chart_type, date, interval, limit=100):
    #for apitoken import get_import_token
    #for chart_type, accepted values include 'tracks', 'videos', 'users'
    #date == YYYY-MM-DD
    #for interval, accepted values include 'daily', 'weekly'
    #returns a list of song metadata
    import requests
    response = requests.get(url='https://api.chartmetric.com/api/charts/tiktok/{}'.format(chart_type),
                            headers={'Authorization' : 'Bearer {}'.format(api_token)}, params={'date': date, 'interval': interval, 'limit': limit}
                                )
    if response.status_code == 200:
        data = response.json()
        chart = data['obj']
        return chart['data']
    else:
        print(response.status_code)
        print(response.text)

def parse_tiktok_data(data):
    #parses list of track dictionaries, drops non-isrc codes, returns pandas dataframe
    import pandas as pd
    data_bucket = []
    for track in data:
        track_tuple = (track['rank'], track['added_at'], track['name'], track['tiktok_artist_names'][0], track['isrc'], track['velocity'], track['cm_track'], track['time_on_chart'], track['release_dates'])
        data_bucket.append(track_tuple)

    df = pd.DataFrame(data_bucket, columns=['rank', 'added_at', 'title', 'artist', 'isrc', 'velocity', 'cm_id', 'time_on_chart', 'release_dates'])
    df.dropna(subset=['isrc'], inplace=True)
    return df


#this function takes a dataframe and iterates through `cm_id` to collect chartmetric artist IDs
#returns new dataframe with `cm_artist_id` feature
def create_artist_id_feat(api_token, dataframe):
    from cm_api import get_track_metadata
    bucket = []
    for row in dataframe.iterrows():
        track_id = row[1]['cm_id']
        artist_id = get_track_metadata(api_token, track_id)['artists'][0]['id']
        bucket.append(artist_id)

    dataframe['cm_artist_id'] = bucket
    return dataframe

#this function takes a dataframe and iterates through `added_at` and `time_on_chart` to create a date 7 days before the record's first occurance on the chart
#returns new dataframe with `Before_Tiktok_Date` feature
def create_before_tiktok_date_feat(dataframe):
    #takes in dataframe with `added_at` and `time_on_chart`
    #returns dataframe with new date feature
    import datetime
    bucket = []
    for row in dataframe.iterrows():
        add_date = row[1]['added_at'] #get add_date of chart
        days = int(row[1]['time_on_chart']) + 7 #adding 7 to total time on chart
        bucket.append(add_date - datetime.timedelta(days=days))

    dataframe['Before_Tiktok_Date'] = bucket
    return dataframe

#creates a new dataframe feature for total instagram followers at the time of `Before_Tiktok_Date`
#returns new dataframe with `total_ig_followers`
def create_instagram_followers_before_feat(api_token,dataframe):
    from cm_api import get_fan_metrics
    bucket = []
    import datetime
    for row in dataframe.iterrows():
        before_date = str(row[1]['Before_Tiktok_Date'])[:10]
        after_date = str(row[1]['Before_Tiktok_Date'] + datetime.timedelta(days=5))[:10]
        artist_id = row[1]['cm_artist_id']
        data = get_fan_metrics(api_token, artist_id,'instagram', str(before_date), str(after_date), field='followers')['followers']
        if len(data) > 0:
            tup = (data[0]['value'], data[-1]['value'])
            bucket.append(tup)
        else:
            tup = (None, None)
            bucket.append(tup) 

    dataframe['total_ig_followers'] = [x[0] for x in bucket]
    return dataframe

def create_instagram_followers_after_feat(dataframe):
    from cm_api import get_fan_metrics
    bucket = []
    for row in dataframe.iterrows():
        before_date = str(row[1]['Before_Tiktok_Date'])[:10]
        after_date = str(row[1]['Week_In_Chart_Date'])[:10]
        artist_id = row[1]['cm_artist_id']
        data = get_fan_metrics(api_token, artist_id,'instagram', str(before_date), str(after_date), field='followers')['followers']
        if len(data) > 0:
            tup = (data[0]['value'], data[-1]['value'])
            bucket.append(tup)
        else:
            tup = (None, None)
            bucket.append(tup) 

    dataframe['ig_followers_afters'] = [x[1] for x in bucket]
    return dataframe

#replaces `artist` with True artist name instead ofg the tiktok artist name which is often inaccurate
def collect_true_artist_names(api_token,dataframe):
    from cm_api import get_track_metadata
    bucket = []
    for row in dataframe.iterrows():
        track_id = row[1]['cm_id']
        artist_name = get_track_metadata(api_token, track_id)['artists'][0]['name']
        bucket.append(artist_name)

    dataframe['artist'] = bucket

    return dataframe

def collect_artist_sppop(api_token, dataframe):
    #iterates thru `cm_artist_id` returns current spotify popularity
    from cm_api import get_artist_metadata
    bucket = []
    for row in dataframe.iterrows():
        x = row[1]['cm_artist_id']
        artist_pop = get_artist_metadata(api_token, x)['cm_statistics']['sp_popularity']
        if (artist_pop):
            bucket.append(artist_pop)
        else:
            bucket.append(None)

    dataframe['artist_pop'] = bucket
    return dataframe


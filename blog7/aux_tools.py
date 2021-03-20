def summ_stat_playlist_artist_popularity(api_token, playlist_id):
    #takes in spotify playlist id and returns summary statistics of artist popularity on spotify
    from helper_funct import get_summary_statistics
    import pandas as pd
    from cm_api import get_artist_metadata, get_playlist_tracks
    data = get_playlist_tracks(api_token, 'spotify', playlist_id, 'current', 'us')
    bucket = []
    for track in data:
        tup = (track['cm_artist'][0])
        bucket.append(tup)
    df = pd.DataFrame(bucket, columns=['cm_artist_id'])

    bucket = []
    for row in df.iterrows():
        x = row[1]['cm_artist_id']
        artist_pop = get_artist_metadata(api_token, x)['cm_statistics']['sp_popularity']
        if (artist_pop):
            bucket.append(artist_pop)
        else:
            bucket.append(None)

    df['artist_pop'] = bucket

    print(get_summary_statistics(df['artist_pop'].dropna()))
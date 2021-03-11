# Artist Discovery Tool: MVP (*Work-In-Progress*)

## Description
This insights tools is designed to analyze the top trending tracks on Tiktok's weekly chart by identifying the artists with an above-average fanbase on Spotify prior to getting placed on the chart.

### Data Dictionary (*Sample*)

| Variable        | Description     | 
| :---:|:---: | 
| `added_at` | Date of Weekly Chart| 
| `Before_Tiktok_Date` | 7 days before record's first occurance on Tiktok chart. `added_at` - (`time_on_chart` + 7)| 
| `title`|Track's title|
|`artist`| Primary artist|
|`isrc`| isrc|
|`cm_track_id`| Chartmetric's unique ID associated with a track|
|`cm_artist_id`| Chartmetric's unique artist identification|
|`days_on_playlist`|Number of days spent on the chart at the time of `added_at`|
|`release_dates`|Track's release date|
|`total_spotify_followers`|# of Spotfiy followers 7 days before `added_at`|
|`total_ig_followers`|# of Instagram followers 7 days before `added_at`|
|`track_age`| age of record on chart; 1 month, 2 months, or over 2 months|


### Measurement

`total_ig_followers` - recorded 7 days before the record's first occurance on the chart

### Output

The output of the tool is a visualization showing the artists in the 75th percentile of `total_IG_followers`. The graph will update once a week

## Analysis
<img align="center" width="1000" height="800" src="https://github.com/jacksonbull87/bull-analytics/blob/main/blog7/visuals/track_age.jpeg">

- 11% of tracks have been on the Top 100 chart for 2 months
- 57% of the tracks have been on the chart for over 2 months
- 30% of the tracks have been on the chart for less than a month
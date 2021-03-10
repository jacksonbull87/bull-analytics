# Artist Discovery Tool: MVP (*Work-In-Progress*)

## Description
This insights tools is designed to analyze the top trending tracks on Tiktok's weekly chart by identifying the artists with an above-average fanbase on Instagram prior to getting placed on the chart.

### Data Dictionary (*Sample*)

| Variable        | Description     | 
| :---:|:---: | 
| `added_at` | Date of Weekly Chart| 
| `title`|Track's title|
|`artist`| Primary artist|
|`isrc`| isrc|
|`cm_track_id`| Chartmetric's unique ID associated with a track|
|`cm_artist_id`| Chartmetric's unique artist identification|
|`days_on_playlist`|Number of days spent on the chart at the time of `added_at`|
|`release_dates`|Track's release date|
|`total_IG_followers`|# of Instagram followers 7 days before `added_at`|


### Measurement

`total_IG_followers` - recorded 7 days before the record's first occurance on the chart

### Output

The output of the tool is a visualization showing the artists in the 75th percentile of `total_IG_followers`. The graph will update once a week

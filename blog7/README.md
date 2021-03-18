# Artist Discovery Tool: MVP (*Work-In-Progress*)

## Description
This insights tools is designed to analyze Tiktok's Top 100 Weekly chart by identifying the artists with an above-average fanbase on Instagram prior to getting placed on the chart. 

From the perspective of talent seekers and A&R professionals, one of the inherent risks when pouring more resources into a client is the possibility that they'll be no one on the other side to receive the creator's message. This tool mitigates that risk by ensuring that there is an an existing audience to build off of.

The sample dataset consists of the top 100 tracks trending on Tiktok for the week of March 9, 2021 **(2021-05-02 thru 2021-05-09)**

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
|`total_ig_followers`|# of Instagram followers on `Before_Tiktok_Date`|
|`track_age`| age of record on chart; 1 month, 2 months, or over 2 months|
|`Week_In_Chart_Date`| Date 7 day's after the record's first chart appearance|
|`ig_followers_afters`| # of Instagram followers on `Week_In_Chart_Date`|
|`IG_Follower_Gain-%`| % Gain in Instagram followers from `Before_Tiktok_Date` to `Week_In_Chart_Date`|



### Measurement

`total_ig_followers` - recorded 7 days before the record's first occurance on the chart

### Output

The output of the tool is a visualization showing the artists in the 75th percentile of `total_IG_followers`. The graph will update once a week

## Analysis
### Percentage of Track Age of Current Tiktok Chart (March 9th, 2021)
<img align="center" width="1000" height="700" src="https://github.com/jacksonbull87/bull-analytics/blob/main/blog7/visuals/track_age.jpeg">

- 11% of tracks have been on the Top 100 chart for 2 months
- 57% of the tracks have been on the chart for over 2 months
- 30% of the tracks have been on the chart for less than a month

Since this is a discovery tool, we're only concerned with the newest records. So the next step would be to filter this dataset down to artists who have only been on this chart for a month.
### Top 10 New Artists Trending on Tiktok Chart (Sorted by Total Instagram Following)
<img align="center" width="1000" height="700" src="https://github.com/jacksonbull87/bull-analytics/blob/main/blog7/visuals/top10_artistsIG.jpeg">

#### Insights
- 4 out of the 10 artists are Latin-American 
    - Wisin: 11,965,418 IG Followers **(Puerto Rico)**
    - Rauw Alejandro: 6,916,424 IG Followers **(Puerto Rico)**
    - Kali Uchis: 2,211,918 IG Followers **(Colombian-American)**
    - Teto: 1,107,185 IG Followers **(Brazil)**




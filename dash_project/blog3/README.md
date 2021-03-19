# Why Fandom Matters For Artists (Outliers, Pt. 2)
## Summary
This project uses social media data from the top trending artists on Tiktok during the week of January 21st, 2021 in order to analyze
how Olivia Rodrigo's massive fanbase helped her break multiple streaming records. 

<p align="center"> 
<img src="https://media.giphy.com/media/seqkUxQi2IbzZEBXes/giphy-downsized.gif">
</p>

[Link to Full Blog Post](https://bull-analytics.com/f/why-fandom-matters-for-artists-outliers-pt-2)


## Data Dictionary


| Variable        | Description                          |
| :---:|:---: |
| `added_at`    | Date of track's placement on Tiktok's weekly chart; January 21|
|`before_tiktok_date`|December 31|
| `title`|Track's title|
|`artist`| Primary artist|
|`isrc`| isrc|
|`velocity`|Average change in rank over a 7-day period|
|`cm_id`| Chartmetric's unique ID associated with a track|
|`time_on_chart`|Number of days spent on the chart at the time of `add_date`|
|`release_dates`|Track's release date|
|`cm_artist_id`| Chartmetric's unique artist identification|
|`slisteners_before`|Artist's total listeners on Spotify on `before_tiktok_date`; December 31|
|`slisteners_after`|Artist's total listeners on Spotify on `added_at` date; having been trending on Tiktok the past 7 days|
|`IG_f31`|# of Instagram followers on December 31|
|`IG_f21`|# of Instagram followers on January 21|
|`TW_f31`|# of Twitter followers on December 31|
|`TW_f21`|# of Twitter followers on January 21|
|`Tiktok_f31`|# of Tiktok followers on December 31|
|`Tiktok_f21`|# of Tiktok followers on January 21|
|`TW%`| Percent Increase in Twitter followers|
|`IG%`| Percent Increase in Instagram followers|
|`TK%`| Percent Increase in Tiktok followers|

## Insights
### Twitter Insights

<img align="left" width="1000" height="500" src="https://github.com/jacksonbull87/bull-analytics/blob/main/blog3/visuals/tw_f31.jpeg">

<img align="right" width="1000" height="500" src="https://github.com/jacksonbull87/bull-analytics/blob/main/blog3/visuals/tw_f21.jpeg">

#### Key-Takeaways

- No artist in this data sample moved from the middle 50% to the top 25% of total followers
- Olivia Rodrigo is the only artist in this sample to double their followers from Dec. 31 - Jan. 21

### Instagram Insights
<img align="left" width="1000" height="500" src="https://github.com/jacksonbull87/bull-analytics/blob/main/blog3/visuals/ig_f31.jpeg">

<img align="right" width="1000" height="500" src="https://github.com/jacksonbull87/bull-analytics/blob/main/blog3/visuals/ig_f21.jpeg">

#### Key-Takeaways

- Olivia Rodrigo is the only artist in this sample to move from the middle 50% to the top 25% of total IG followers
- Olivia Rodrigo is one of two artists in this sample who doubled their IG followers. The other artist is Papu DJ & L-Gante whose song, L-Gante Rkt, spent 35 days on the chart versus just 12 days for Drivers License.
- Despite Papu DJ and L-Gante doubling their followers to 17k, they still fall short of the median value (298k)

### Tiktok Insights
<img align="left" width="1000" height="500" src="https://github.com/jacksonbull87/bull-analytics/blob/main/blog3/visuals/tk_f31.jpeg">

<img align="right" width="1000" height="500" src="https://github.com/jacksonbull87/bull-analytics/blob/main/blog3/visuals/tk_f21.jpeg">

#### Key-Takeaways

- Olivia Rodrigo is the only artist in this sample to move from the middle 50% to the top 25% of total IG followers
- Olivia Rodrigo is one of two artists in this sample who doubled their Tiktok followers. The other artist is Erica Banks whose song, Buss It, spent 33 days on the chart versus just 12 days for Drivers License.
- Despite having doubled her Tiktok followers, Banks still falls short of the median value (1 million followers) with only 55k Tiktok followers
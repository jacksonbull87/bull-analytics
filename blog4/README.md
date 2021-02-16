# Understanding The Artist Growth Funnel
## Summary
This project analyzes data from artists previously on a non-Spotify, non-label playlist. The goal of the research is to find out what social media platforms have the strongest relationship with `Net Follower Gain/Loss(Spotify)`.

### Playlist Source
- Name: Alternative VIBES
- Curator: VIBE Lifestyle
- 117K
- Genre: Modern, Alternative Rock

### Dependent Variable
- `Net Follower Gain/Loss(Spotify)` - The difference in Spotify followers from a week before a track is added to the playlist and 1 week after the artist is removed from the playlist

### Social Media Platforms
- Instagram, Twitter, Tiktok

### Questions
- Which platform has the strongest relationship with `Net Follower Gain/Loss(Spotify)`

## Data Dictionary


| Variable        | Description     | 
| :---:|:---: | 
| `added_at`    | Date of track's placement on playlist| 
| `title`|Track's title|
|`artist`| Primary artist|
|`isrc`| isrc|
|`cm_track_id`| Chartmetric's unique ID associated with a track|
|`days_on_playlist`|Number of days spent on the chart at the time of `added_at`|
|`release_dates`|Track's release date|
|`cm_artist_id`| Chartmetric's unique artist identification|
|`before_pl_spfollowers`|Artist's total Spotify followers 7 days before `added_at`|
|`after_pl_spfollowers`|Artist's total Spotify followers 7 days after `removed_at`|
|`before_pl_igfollowers`|# of Instagram followers 7 days before `added_at`|
|`after_pl_igfollowers`|# of Instagram followers 7 days after `removed_at`|
|`before_pl_twfollowers`|# of Twitter followers 7 days before `added_at`|
|`after_pl_twfollowers`|# of Twitter followers 7 days after `removed_at`|
|`before_pl_tkfollowers`|# of Tiktok followers 7 days before `added_at`|
|`after_pl_tkfollowers`|# of Tiktok followers 7 days after `removed_at`|
|`Twitter`| Boolean value indicating whether artist has a Twitter account|
|`Instagram`| Boolean value indicating whether artist has an Instagram account|
|`Tiktok`| Boolean value indicating whether artist has a Tiktok account|
|`Net Follower Gain/Loss(Spotify)`| `after_pl_spfollowers` minus `before_pl_spfollowers` |
|`Net Follower Gain/Loss(Twitter)`|  `after_pl_twfollowers` minus `before_pl_twfollowers`|
|`Net Follower Gain/Loss(Instagram)`|  `after_pl_igfollowers` minus `before_pl_igfollowers` |
|`Net Follower Gain/Loss(Tiktok)`|  `after_pl_tkfollowers` minus `before_pl_tkfollowers`|

## Insights
### Twitter Insights

<img align="left" width="800" height="500" src="https://github.com/jacksonbull87/bull-analytics/blob/main/blog4/visuals/twscatter.png">

<img align="right" width="800" height="500" src="https://github.com/jacksonbull87/bull-analytics/blob/main/blog4/visuals/twbarplot.png">

#### Key-Takeaways

- Pearson’s Correlation: .60
- 74% of artists have Twitter accounts
- 26% do not have Twitter

### Instagram Insights
<!-- <img align="left" width="1000" height="500" src="https://github.com/jacksonbull87/bull-analytics/blob/main/blog3/visuals/ig_f31.jpeg">

<img align="right" width="1000" height="500" src="https://github.com/jacksonbull87/bull-analytics/blob/main/blog3/visuals/ig_f21.jpeg"> -->

#### Key-Takeaways



### Tiktok Insights
<!-- <img align="left" width="1000" height="500" src="https://github.com/jacksonbull87/bull-analytics/blob/main/blog3/visuals/tk_f31.jpeg">

<img align="right" width="1000" height="500" src="https://github.com/jacksonbull87/bull-analytics/blob/main/blog3/visuals/tk_f21.jpeg"> -->
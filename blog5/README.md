# Is Rock Dead?
## Summary
This project analyzes data from the top performing artists (by `Net Follower Gain/Loss(Spotify)`) who were added to Alternative VIBES playlist between July 10th and December 28. Among thos 18 artists, I analyzed the effect that engagement and reach has on my dependent variable.

### Playlist Source
- Name: Alternative VIBES
- Curator: VIBE Lifestyle
- 117K
- Genre: Modern, Alternative Rock

### Dependent Variable
- `Net Follower Gain/Loss(Spotify)` - The difference in Spotify followers from a week before a track is added to the playlist and 1 week after the artist is removed from the playlist

### Independent Variable
- `tk_engagement_before(likes per follower)` - Measured a week before the record's playlist `add_date`
- `Total Spotify Reach` - Sum of all playlist followers that the record was also added to while on Altnerative VIBES


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
|`tk_engagement_before(likes per follower)`| Measured a week before the record's playlist `add_date` |
|`Total Spotify Reach`|  Sum of all playlist followers that the record was also added to while on Altnerative VIBES |


# nba_hustle_stats
Many NBA coaches, players, media members, and fans like to claim that the teams who hustle and “want it more” are the teams that win games. The question is then “What exactly is hustle? And can we statistically measure its impact on winning basketball games?”

Luckily, nba.com has provided multiple statistics that they define as hustle plays, and they fall in line with what many basketball heads think of when they hear the word “hustle”. Before, these stats were never measured and so were considered thankless “dirty work” that helped a team win. Now as a data analyst, there is currently 3+ years of data I can use to determine how important hustle is when it comes to winning basketball games.

The first hustle stat listed on nba.com is the screen assist. Screen assists are “the number of times an offensive player or team sets a screen for a teammate that directly leads to a made field goal by that teammate.” I’ve found that screen assists per game do not have a significant correlation with offensive success. In the last three regular seasons from 2016-2019, screen assists only had a correlation coefficient of 0.0162 with effective field goal percentage and only 0.0336 in relation to offensive rating. Of course, screen assists still help an offense because they directly lead to made field goals. But trying to increase a team’s screen assist totals should not be a goal in itself when teams with the most screen assists don’t necessarily score the most efficiently. (Screen assists have no major change in importance for the playoffs)

Deflections are “the number of times a defensive player or team gets his hand on the ball on a non-shot attempt.” They can effectively stop fast breaks, prevent an open shot in half-court plays, and create steals. From year to year, higher league average deflections per game have led to lower league average defensive ratings. In the last three regular seasons, deflection rate (pace-adjusted deflections) has a correlation coefficient of -0.3602 in relation to defensive rating. The negative number is good for defense since the goal on that end is to give up less points. Although in the post-season, deflection rate has a major drop-off in importance. In the playoffs from 2017-2019, the correlation coefficient between it and defensive rating was only -0.0662. Further investigation and analysis are needed in order to explain why that is.

Loose balls recovered are ”the number of times a player or team gains sole possession of a live ball that is not in the control of either team”. There are two categories for loose balls recovered, offensive loose balls and defensive loose balls recovered.

Offensive loose balls recovered have no significant correlation with offensive success whether you look at offensive rating, true shooting percentage, or effective field goal percentage. They do have a very strong correlation with offensive rebounds per game (0.45) during the 2018, 2019, and halfway through the 2020 regular season. This tells me more about the flaws in the stat because some of these loose balls recovered can also be tracked as offensive rebounds. There’s a grey area where you can consider it a loose ball or just a rebounding opportunity. Even if in the long run, offensive loose balls recovered may not have a significant effect on offensive success, in a close one score game it can still be the difference between winning and losing. As for the postseason, there is no change in significance when it comes to offensive loose balls recovered.

Defensive loose balls recovered have a moderate correlation (0.2352) with deflections from 2018 to this current 2020 regular season. As for defensive success overall, defensive loose balls recovered have a moderate correlation (-0.2065) with defensive rating during the regular season. The last two postseasons in 2018 and 2019, defensive loose balls recovered have a rise in significance (-0.3224).

Unfortunately, loose balls recovered cannot be as accurate when measuring importance since there’s no data on opportunities per game. So, it can only be measured on a per game basis rather than a per possession.

Charges drawn, “the number of times a defensive player or a team draws a charge”, has nearly zero significance on defensive rating whether you split it by regular season or postseason. Most players don’t consistently try to draw charges, and it’s effectively a riskier way of contesting shots since it can automatically result in opponent free throws. But, charges can be more rewarding too since they can also result in opponent turnovers. Overall though, teams don’t need to focus on drawing more charges.

Contested two-point shots have an opportunity cost. The more contested 2s, the less steals, so these contests are probably a product of a conservative defensive approach. Contested twos have a strong correlation with defensive rating during the regular season, but it has a major drop-off in importance in the postseason. Meanwhile, steals consistently are of the same importance regular and postseason. I hypothesize this may be because teams in the playoffs have time to develop more specific game plans for their opponents. The 2017-2019 playoffs actually had a positive correlation (0.1078) between 2-point contest rate and defensive rating. An example of why can be seen through Russell Westbrook. Leaving him open for a mid-range shot is of higher value than contesting a layup. In the playoffs, all game plans are specifically crafted for your opponent rather than for 29 other teams in the regular season.

Contested three-pointers have near zero significance in team defensive rating. It’s wildly inconsistent and unpredictable from year to year. That’s why it’s well known amongst NBA data analysts that it’s more important that teams prevent three-point attempts rather than contest them at high rates.

Overall, hustle plays vary in importance and each stat can even change in significance from regular to postseason. The one hustle stat that remains important from regular season to postseason is defensive loose balls recovered. It’s the most classic hustle play that fans and media members glorify where players will dive on the floor and jump into the stands to save the ball out of bounds. The numbers show that it was always appropriate to appreciate these types of plays. 

The next step is to measure the impact of individual players with strong hustle stats. Maybe team-wise, not every player needs to hustle for team success. But maybe those hustle guys on your team carry a major impact on winning games.

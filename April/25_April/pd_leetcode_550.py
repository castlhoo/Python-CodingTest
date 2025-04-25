# Table: Activity

# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | player_id    | int     |
# | device_id    | int     |
# | event_date   | date    |
# | games_played | int     |
# +--------------+---------+
# (player_id, event_date) is the primary key (combination of columns with unique values) of this table.
# This table shows the activity of players of some games.
# Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.
 

# Write a solution to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date, then divide that number by the total number of players.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Activity table:
# +-----------+-----------+------------+--------------+
# | player_id | device_id | event_date | games_played |
# +-----------+-----------+------------+--------------+
# | 1         | 2         | 2016-03-01 | 5            |
# | 1         | 2         | 2016-03-02 | 6            |
# | 2         | 3         | 2017-06-25 | 1            |
# | 3         | 1         | 2016-03-02 | 0            |
# | 3         | 4         | 2018-07-03 | 5            |
# +-----------+-----------+------------+--------------+
# Output: 
# +-----------+
# | fraction  |
# +-----------+
# | 0.33      |
# +-----------+
# Explanation: 
# Only the player with id 1 logged back in after the first day he had logged in so the answer is 1/3 = 0.33

import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:

    player_day = activity[['player_id', 'event_date','games_played']]

    player_min_day = player_day.groupby(['player_id']).agg({'event_date':'min'}).reset_index()
    player_min_day.columns = ['player_id', 'first_login']

    merged = pd.merge(player_day, player_min_day, left_on = 'player_id', right_on = 'player_id', how = 'left')

    merged['next_days'] = merged['first_login'] + pd.Timedelta(days=1)

    login_set = set(zip(player_day['player_id'], player_day['event_date']))

    merged['next_day_login'] = merged.apply(lambda row : (row['player_id'], row['next_days']) in login_set, axis = 1)

    first_logins = merged[merged['event_date'] == merged['first_login']]

    fraction = round(first_logins['next_day_login'].mean(), 2)

    return pd.DataFrame({'fraction' : [fraction]})
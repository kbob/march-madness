# March Madness 2014

A quick and dirty Python script to analyze people's progress on the
March Madness pool.

The script calculates and prints each player's minimum and maximum
possible scores, based on the games that have been played.


## Recording a Game

Edit the global variable **actual** and change None to either 0 or 1.


## Adding a Player

Edit the global variable predictions and add a player and her predictions.
Please keep the players in alphabetical order.

To check your data entry, call `print_player` with your new player's name, run
the script, and check the data.


## Data

These are the global variables.

 - **scores** - how many points are awarded per game in each round.
 
 - **teams** - the names of the teams.  Feel free to change the spelling
    on these.
    
 - **width** - the width of the longest team's name
 
 - **predictions** - maps player names to their predictions.  See
   _Prediction Data Format_ below.
   
 - **p_width** - the width of the longest player's name   
 
 - **actual** - the actual winners of the games played so far.
   The format is the same as for predictions, except that the value
   `None` is used for games that have not yet been played.


## Prediction Data Format
 
Each prediction set is a list of lists of Booleans.  Each sublist
represents one round of the playoffs, so there are six inner lists,
and they have length  32, 16, 8, 4, 2, and 1.
 
Each game's prediction is recorded as 0 or 1.  0 means the team
listed formerly will win, and 1 means the latter team will win.
 
For example, in Round 1, I predicted that VCU would beat
SF Austin.  That games is in the first round (sublist 0), third game
(index 2), and VCU is listed before Austin, so I put a zero for that space.

    predictions['Bob'][0][2] = 0
    
The numbers are always 0 and 1.  The actual team names depend on which
teams were predicted for previous rounds.

The data is actually entered as a big map literal.

    predictions = {
        'Bob':                # player name
             [
              [0, 1, 0, ...], # 1st round: Fla, Pitt, VCU, ... (32 games)
              [0, 1, 1, ...], # 2nd round: Fla, UCLA, Syr, ... (16 games)
              [0, 1, 1, ...], # 3rd round: 8 games
              [0, 0, 0, 0,]   # 4th round: 4 games
              [0, 1],         # 5th round: 2 games
              [1]             # final game
             ],

    # ... other players
    }
 
 

# Program to create league schedule

Either provide the count of teams or a sorted list of teams (saved in a file) and the number of groups and this program
will distribute them evenly to groups and provide the schedule of games.

### Example command

```commandline
python3 league_distribution.py --teams_file demo_teams.txt -g 4 -r 
```

### Example output

```commandline
Generating league distribution for 16 teams in 4 groups

Group: A
A1: team-Semi-pro-1
A2: team-Beginner-4
A3: team-Pro-3
A4: team-Beginner-5

Group: B
B1: team-Semi-pro-3
B2: team-Beginner-8
B3: team-Pro-2
B4: team-Beginner-2

Group: C
C1: team-Semi-pro-2
C2: team-Beginner-1
C3: team-Beginner-7
C4: team-Pro-1

Group: D
D1: team-Beginner-3
D2: team-Beginner-6
D3: team-Semi-pro-4
D4: team-Pro-4


Group A matches:
Semi-pro-1 vs Beginner-4
Semi-pro-1 vs Pro-3
Semi-pro-1 vs Beginner-5
Beginner-4 vs Pro-3
Beginner-4 vs Beginner-5
Pro-3 vs Beginner-5

Group B matches:
Semi-pro-3 vs Beginner-8
Semi-pro-3 vs Pro-2
Semi-pro-3 vs Beginner-2
Beginner-8 vs Pro-2
Beginner-8 vs Beginner-2
Pro-2 vs Beginner-2

Group C matches:
Semi-pro-2 vs Beginner-1
Semi-pro-2 vs Beginner-7
Semi-pro-2 vs Pro-1
Beginner-1 vs Beginner-7
Beginner-1 vs Pro-1
Beginner-7 vs Pro-1

Group D matches:
Beginner-3 vs Beginner-6
Beginner-3 vs Semi-pro-4
Beginner-3 vs Pro-4
Beginner-6 vs Semi-pro-4
Beginner-6 vs Pro-4
Semi-pro-4 vs Pro-4
```
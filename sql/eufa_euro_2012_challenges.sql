-- 1. Show the matchid and player name for all goals scored by Germany.
SELECT matchid, player FROM goal
WHERE teamid LIKE 'GER';

-- 2. Show id, stadium, team1, team2 for just game 1012
SELECT id, stadium, team1, team2 FROM game
WHERE id LIKE 1012;

-- 3. Combine the two steps above into a single query to show the player, teamid, stadium and mdate for every German goal.
SELECT player, teamid, stadium, mdate
FROM game JOIN goal ON (id=matchid)
WHERE teamid LIKE 'GER';

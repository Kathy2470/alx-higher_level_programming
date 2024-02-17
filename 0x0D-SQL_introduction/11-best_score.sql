-- Script: best_score.sql
-- Description: Lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0, ordered by score (top first).

USE $1;

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

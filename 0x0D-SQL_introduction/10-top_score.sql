-- Script: top_score.sql
-- Description: Lists all records of the table second_table in the database hbtn_0c_0, ordered by score (top first).

USE $1;

SELECT score, name
FROM second_table
ORDER BY score DESC;

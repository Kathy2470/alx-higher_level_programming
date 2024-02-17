-- Script: update_score_bob.sql
-- Description: Updates the score of Bob to 10 in the table second_table.

USE $1;

UPDATE second_table
SET score = 10
WHERE name = 'Bob';

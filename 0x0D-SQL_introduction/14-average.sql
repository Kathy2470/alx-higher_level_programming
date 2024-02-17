-- Script: compute_average.sql
-- Description: Computes the score average of all records in the table second_table.

USE $1;

SELECT AVG(score) AS average
FROM second_table;

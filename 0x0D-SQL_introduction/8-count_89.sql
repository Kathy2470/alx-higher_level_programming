-- Script: count_89.sql
-- Description: Displays the number of records with id = 89 in the first_table table of the specified database.

USE $1;

SELECT COUNT(*)
FROM first_table
WHERE id = 89;

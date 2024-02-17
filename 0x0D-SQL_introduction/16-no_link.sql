-- Script: list_records_with_name.sql
-- Description: Lists all records of the table second_table with a name value in the database hbtn_0c_0.

USE $1;

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;

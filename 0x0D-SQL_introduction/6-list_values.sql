-- Script: list_table_values.sql
-- Description: Lists all rows of the table first_table from the specified database.

USE $1;

SELECT *
FROM first_table;

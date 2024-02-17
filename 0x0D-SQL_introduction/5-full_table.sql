-- Script: print_table_description.sql
-- Description: Prints the full description of the table first_table from the specified database.

USE $1;

SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY
FROM information_schema.columns
WHERE table_schema = DATABASE() AND table_name = 'first_table';

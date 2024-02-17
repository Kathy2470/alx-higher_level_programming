-- Script: insert_value.sql
-- Description: Inserts a new row into the table first_table in the specified database.

USE $1;

INSERT INTO first_table (id, name)
VALUES (89, 'Best School');

-- Script: list_tables.sql
-- Description: Lists all tables of a specified database.

USE $1;

SELECT table_name
FROM information_schema.tables
WHERE table_schema = DATABASE();

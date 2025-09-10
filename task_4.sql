-- Write a script that prints the full
-- description of the table books from the 
-- database alx_book_store in your MySQL server.

-- The database name will be passed as an argument of the 
-- mysql command
-- You are not allowed to use the DESCRIBE or EXPLAIN statements
-- The name of the file should be task_4.sql
-- All SQL keywords should be in uppercase
-- Repo:

-- GitHub repository: Intro_to_DB
-- File: task_4.sql


SELECT 
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_DEFAULT,
    COLUMN_KEY,
    EXTRA
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'books';




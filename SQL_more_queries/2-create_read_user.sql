-- Creates the database hbtn_0d_2 and the user user_0d_2.
-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2.

-- 1. Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- 2. Create the user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- 3. Grant SELECT privilege on the specific database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Check if the user exists
SELECT COUNT(*)
FROM mysql.user
WHERE User = 'user_0d_1' AND Host = 'localhost' INTO @user_exists;

-- If the user doesn't exist, create it
IF @user_exists = 0 THEN
    CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
END IF;

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

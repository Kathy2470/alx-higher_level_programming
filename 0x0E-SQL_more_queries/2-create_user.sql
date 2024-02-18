-- Check if the database hbtn_0d_2 exists
SELECT COUNT(*)
FROM information_schema.schemata
WHERE schema_name = 'hbtn_0d_2' INTO @db_exists;

-- If the database doesn't exist, create it
IF @db_exists = 0 THEN
    CREATE DATABASE hbtn_0d_2;
END IF;

-- Check if the user user_0d_2 exists
SELECT COUNT(*)
FROM mysql.user
WHERE User = 'user_0d_2' AND Host = 'localhost' INTO @user_exists;

-- If the user doesn't exist, create it
IF @user_exists = 0 THEN
   CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
END IF;

-- Grant SELECT privilege to user_0d_2 on database hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';



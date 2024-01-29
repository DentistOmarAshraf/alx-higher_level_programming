-- Create Database & new User & grant select privilege
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS
'user_0d_2'@'localhost'
IDENTIFIED WITH mysql_native_password BY
'user_0d_2_pwd';
FLUSH PRIVILEGES;
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

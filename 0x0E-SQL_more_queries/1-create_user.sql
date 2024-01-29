-- Creating User On MYSQL

CREATE USER IF NOT EXISTS
'user_0d_1'@'localhost'
IDENTIFIED WITH mysql_native_password BY
'user_0d_1_pwd';
FLUSH PRIVILEGES;
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
WITH GRANT OPTION;
FLUSH PRIVILEGES;

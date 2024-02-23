#!/bin/bash

mysql_password="choco@late123"

sql_file="0-list_databases.sql"

mysql -uroot -p$mysql_password < $sql_file

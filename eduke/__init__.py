import pymysql

# This line tricks Django into thinking mysqlclient 2.2.1 is installed
pymysql.version_info = (2, 2, 1, "final", 0) 
pymysql.install_as_MySQLdb()
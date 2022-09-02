import mariadb
import sys
def connection ():
    # Connect to MariaDB Platform
    try:
        conn = mariadb.connect(
            user="cabp0694",
            password="Octubre01+*",
            host="database-2.ctiwpcvye3t5.us-east-1.rds.amazonaws.com",
            port=3306,
            database="ProgIDB"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)


    return conn



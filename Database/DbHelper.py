import mysql.connector
import getpass

PASSWORD = getpass.getpass()
dbname = "courses_management"

class DbHelper:
    def __init__(self):
        while True:
            try:
                self.db = mysql.connector.connect(
                    host="localHost", user="root", password=PASSWORD, database=dbname
                )
                break
            except:
                print("Database does not exist.")
                self.create_database()

        self.db.autocommit = True
        self.cursor = self.db.cursor(buffered=True)

    def create_database(self):
        print(f"CREATING DB {dbname}")
        db = mysql.connector.connect(
            host="localHost",
            user="root",
            password=PASSWORD,
        )
        cursor = db.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {dbname}")
        cursor.close()
        db.close()

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
        for column_no in range(len(columns)):
            for keyword in columns[column_no]:
                query += keyword + " "
            end = ");" if column_no == len(columns) - 1 else ", "
            query += end
        self.cursor.execute(query)

    def execute(self, query, values, success_msg=""):
        try:
            self.cursor.execute(query, values)
            return True, success_msg
        except mysql.connector.Error as e:
            print(f"Something went wrong: {e.msg}, {e.errno}")
            return False, "Something went wrong."

    def generate_table(self):
        desc = self.cursor.description
        column_names = [col[0] for col in desc]
        table = [dict(zip(column_names, row)) for row in self.cursor.fetchall()]
        return table

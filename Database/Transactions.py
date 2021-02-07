from datetime import datetime


class Transactions:
    def __init__(self, dbHelper):
        self.table_name = "Transactions"
        self.columns = [
            ("TransID", "INT", "AUTO_INCREMENT", "PRIMARY KEY"),
            ("UserID", "INT", "NOT NULL"),
            ("CourseID", "INT", "NOT NULL"),
            ("IsCompleted", "INT", "NOT NULL", "DEFAULT 0"),
            ("DOPurchase", "DATE", "NOT NULL"),
            ("DOStart", "DATE"),
            ("DOEnd", "DATE"),
            ("FOREIGN KEY (UserID)", "REFERENCES Users(UserID)"),
            ("FOREIGN KEY (CourseID)", "REFERENCES Courses(CourseID)"),
        ]
        self.dbHelper = dbHelper
        self.dbHelper.create_table(self.table_name, self.columns)

    def add_transaction(self, user_id, course_id):
        query = (
            f"INSERT INTO Transactions (UserID, CourseID, DOPurchase) "
            f"VALUES (%s, %s, %s)"
        )
        return self.dbHelper.execute(
            query,
            (user_id, course_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            "Transaction successful!",
        )

    def remove_transaction(self, trans_id):
        query = f"DELETE FROM Transactions " f"WHERE TransID=%s"
        return self.dbHelper.execute(query, [trans_id], "Course removed!")

    def get_transactions(self, user_id="", course_id=""):
        query = f"SELECT * FROM Transactions WHERE "
        conditions, values = [], []
        if course_id:
            conditions.append("CourseID=%s")
            values.append(course_id)
        if user_id:
            conditions.append("UserID=%s")
            values.append(user_id)
        query += " AND ".join(conditions)
        e, message = self.dbHelper.execute(query, values)
        if not e:
            return [], message
        return self.dbHelper.generate_table(), "Success"

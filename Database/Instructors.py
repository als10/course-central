class Instructors:
    def __init__(self, dbHelper):
        self.table_name = "Instructors"
        self.columns = [
            ("UserID", "INT", "PRIMARY KEY"),
            ("JobDesc", "varchar(30)"),
            ("University", "varchar(50)"),
            ("Bio", "text"),
            ("FOREIGN KEY (UserID)", "REFERENCES Users(UserID)"),
        ]
        self.dbHelper = dbHelper
        self.dbHelper.create_table(self.table_name, self.columns)

    def register(self, user_id, job, uni, bio):
        query = (
            f"INSERT INTO Instructors (UserID, JobDesc, University, Bio) "
            f"VALUES (%s, %s, %s, %s)"
        )
        return self.dbHelper.execute(
            query, (user_id, job, uni, bio), "Instructor registered successfully!"
        )

    def update_instructor(self, user_id, job, uni, bio):
        query = (
            f"UPDATE Instructors "
            f"SET JobDesc=%s, University=%s, Bio=%s "
            f"WHERE UserID=%s"
        )
        return self.dbHelper.execute(
            query, (job, uni, bio, user_id), "Instructor details updated successfully!"
        )

    def delete_instructor(self, user_id):
        query = f"DELETE FROM Instructors " f"WHERE UserID=%s"
        return self.dbHelper.execute(
            query, [user_id], "Instructor deletion successful."
        )

    def get_instructor(self, user_id):
        query = f"SELECT * FROM Instructors WHERE UserID=%s"
        self.dbHelper.execute(query, [user_id])
        return self.dbHelper.generate_table()[0]

import re

website_regex = re.compile(
    r"^(?:http|ftp)s?://"  # http:// or https://
    r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
    r"localhost|"  # localhost...
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
    r"(?::\d+)?"  # optional port
    r"(?:/?|[/?]\S+)$",
    re.IGNORECASE,
)


class Courses:
    def __init__(self, dbHelper):
        self.table_name = "Courses"
        self.columns = [
            ("CourseID", "INT", "AUTO_INCREMENT", "PRIMARY KEY"),
            ("CourseName", "varchar(50)", "NOT NULL"),
            ("Description", "text"),
            ("Difficulty", "INT(1)", "NOT NULL", "default 0"),
            ("UserID", "INT", "NOT NULL"),
            ("Fees", "INT", "NOT NULL"),
            ("Duration", "varchar(20)", "NOT NULL", "default 'Not provided.'"),
            ("CourseLink", "TEXT", "NOT NULL"),
            ("FOREIGN KEY (UserID)", "REFERENCES Instructors(UserID)"),
        ]
        self.dbHelper = dbHelper
        self.dbHelper.create_table(self.table_name, self.columns)

    def add_course(
        self, instructor_id, course_name, desc, difficulty, fees, duration, link
    ):
        if not course_name:
            return False, "Please enter the course name."
        if not desc:
            desc = "No description provided."
        if not fees:
            fees = 0
        if len(duration.split()) < 2:
            duration = "Not provided."
        if not link:
            return False, "Please provide the course link."
        if re.match(website_regex, link) is None:
            return False, "Invalid link provided!"
        query = (
            f"INSERT INTO Courses (CourseName, Description, Difficulty, UserID, Fees, Duration, CourseLink) "
            f"VALUES (%s, %s, %s, %s, %s, %s, %s)"
        )
        return self.dbHelper.execute(
            query,
            (course_name, desc, difficulty, instructor_id, fees, duration, link),
            "Course added successsfully.",
        )

    def update_course(
        self, course_id, course_name, desc, difficulty, fees, duration, link
    ):
        if not course_name:
            return False, "Please enter the course name."
        if not desc:
            desc = "No description provided."
        if not fees:
            fees = 0
        if len(duration.split()) < 2:
            duration = "Not provided."
        if not link:
            return False, "Please provide the course link."
        query = (
            f"UPDATE Courses "
            f"SET CourseName=%s, Description=%s, Difficulty=%s, Fees=%s, Duration=%s, CourseLink=%s "
            f"WHERE CourseID=%s"
        )
        return self.dbHelper.execute(
            query,
            (course_name, desc, difficulty, fees, duration, link, course_id),
            "Course updated successfully.",
        )

    def delete_course(self, course_id):
        query = f"DELETE FROM Courses " f"WHERE CourseID=%s"
        return self.dbHelper.execute(query, [course_id], "Course deletion successful.")

    def search_courses(self, course_name="", user_id=0, course_id=0, sort_by=""):
        query = f"SELECT * FROM Courses, Users WHERE Courses.UserID = Users.UserID"
        values = []
        if course_name:
            course_name = "%" + course_name + "%"
            query += " AND CourseName LIKE %s"
            values.append(course_name)
        if user_id:
            query += " AND Courses.UserID=%s"
            values.append(user_id)
        if course_id:
            if type(course_id) == type(2):
                query += " AND CourseID=%s"
                values.append(course_id)
            else:
                query += " AND CourseID IN ("
                query += ",".join(["%s"] * len(course_id))
                query += ")"
                values.extend(course_id)

        if sort_by and "None" not in sort_by:
            query += f" ORDER BY {sort_by}"
        e, message = self.dbHelper.execute(query, values)
        if not e:
            return {}, message
        return self.dbHelper.generate_table(), "Success"

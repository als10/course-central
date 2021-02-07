from werkzeug.security import check_password_hash, generate_password_hash
import re

email_regex = re.compile(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")


class Users:
    def __init__(self, dbHelper):
        self.dbHelper = dbHelper
        self.table_name = "Users"
        self.columns = [
            ("UserID", "INT", "AUTO_INCREMENT", "NOT NULL", "PRIMARY KEY"),
            ("UserName", "varchar(10)", "UNIQUE", "NOT NULL"),
            ("FullName", "varchar(30)", "NOT NULL"),
            ("Email", "varchar(50)", "UNIQUE", "NOT NULL"),
            ("Password", "TEXT", "NOT NULL"),
            ("IsInstructor", "INT", "NOT NULL", "default 0"),
        ]
        self.dbHelper.create_table(self.table_name, self.columns)

    def login(self, username, password):
        user, message = self.get_user(username=username)
        if not user:
            return user, message
        if not check_password_hash(user["Password"], password):
            return False, "Username / Password was incorrect. Please try again!"
        return user, "Successfully logged in."

    def register(self, name, username, email, password, confirm, isInstructor):
        e = []
        if not name:
            e.append("Please enter your name.")
        if not username:
            e.append("Please enter a username.")
        if not email:
            e.append("Please enter your e-mail.")
        if not password:
            e.append("Please enter a password.")
        if e:
            return False, " ".join(e)

        e, message = self.checkUsernameAndEmail(username, email)
        if not e:
            return e, message

        e = self.validate_password(password)
        if e:
            return False, e

        if password != confirm:
            return False, "Passwords do not match!"

        query = (
            f"INSERT INTO Users (UserName, FullName, Email, Password, IsInstructor) "
            f"VALUES (%s, %s, %s, %s, %s)"
        )
        e, message = self.dbHelper.execute(
            query,
            (username, name, email, generate_password_hash(password), isInstructor),
        )
        if not e:
            return e, message
        return (
            self.get_user(username=username)[0]["UserID"],
            "User registered successfully!",
        )

    def update_user(self, user_id, name, username, email):
        e = []
        if not name:
            e.append("Please enter your name.")
        if not username:
            e.append("Please enter a username.")
        if not email:
            e.append("Please enter your e-mail.")
        if e:
            return False, " ".join(e)

        e, message = self.checkUsernameAndEmail(username, email, user_id)
        if not e:
            return e, message

        query = (
            f"UPDATE Users "
            f"SET FullName=%s, UserName=%s, Email=%s "
            f"WHERE UserID=%s"
        )
        e, message = self.dbHelper.execute(
            query,
            (name, username, email, user_id),
            "User details updated successfully.",
        )
        if not e:
            return e, message
        return user_id, message

    def delete_user(self, user_id):
        query = f"DELETE FROM Users " f"WHERE UserID=%s"
        return self.dbHelper.execute(query, [user_id], "User deletion successful.")

    def checkUsernameAndEmail(self, username, email, user_id=0):
        e, message = self.dbHelper.execute(
            f"SELECT * FROM {self.table_name} WHERE UserName=%s AND UserID!=%s",
            (username, user_id),
        )
        if not e:
            return e, message
        if len(self.dbHelper.generate_table()) > 0:
            return False, "Username already taken."

        if len(username) < 4:
            return False, "Username must contain at least 4 characters."

        e, message = self.dbHelper.execute(
            f"SELECT * FROM {self.table_name} WHERE Email=%s AND UserID!=%s",
            (email, user_id),
        )
        if not e:
            return e, message
        if len(self.dbHelper.generate_table()) > 0:
            return False, "Email already registered."

        if re.match(email_regex, email) is None:
            return False, "Invalid e-mail."
        return True, "Success"

    def get_user(self, user_id="", username=""):
        query = f"SELECT * FROM Users"
        values = []
        if user_id:
            query += f" WHERE UserID=%s"
            values = [user_id]
        elif username:
            query += f" WHERE UserName=%s"
            values = [username]
        e, message = self.dbHelper.execute(query, values)
        if not e:
            return e, message
        table = self.dbHelper.generate_table()
        if len(table) == 0:
            return False, "User not found. Please register first!"
        return table[0], "Success"

    def validate_password(self, password):
        errors = []
        if len(password) < 8:
            errors.append("Password must be at least 8 characters long.")
        if not any(x.isupper() for x in password):
            errors.append("Password must contain at least one uppercase letter.")
        if not any(x.islower() for x in password):
            errors.append("Password must contain at least one lowercase letter.")
        if not any(x.isdigit() for x in password):
            errors.append("Password must contain at least one digit.")
        m = " ".join(errors)
        return m

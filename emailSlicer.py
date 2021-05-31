import re
import sqlite3


def email_slicer(email):
    return re.split(r"@", email)


class User:

    def __init__(self, email):
        self.email = email

    def email_slicer(self):
        return re.split(r"@", self.email)

    @property
    def username(self):
        return self.email_slicer()[0]

    @property
    def domain(self):
        return self.email_slicer()[1]


def save_user():
    while True:
        file = input("Enter your filename here: ")
        if re.search(r".txt$", file):
            break
        print("File format not supported!")

    try:
        with open(file) as f:
            text = f.read()
    except FileNotFoundError:
        print("File not found!")
        return

    # DB Connection
    conn = sqlite3.connect("contact.db")
    cur = conn.cursor()

    address_book = re.findall(r"^From: ([\w._-]+@[\w._-]+\.[\w._-]+)", text, re.MULTILINE)
    address_book = set(address_book)

    batch = []

    for email in address_book:
        user = User(email)
        cur.execute(f"SELECT * FROM Users WHERE username='{user.username}'")
        if cur.fetchone() is None:
            record = (user.username, user.email)
            batch.append(record)

    if len(batch) > 0:
        with conn:
            conn.executemany("INSERT INTO Users (username, email) VALUES (?, ?)", batch)

    print("Done!")
    return


# DB Connection
# conn = sqlite3.connect("contact.db")
# cur = conn.cursor()
#
# # Create table only run once
# cur.execute("CREATE TABLE Users ('id' INTEGER NOT NULL,"
#             "'username' TEXT NOT NULL,"
#             "'email' TEXT NOT NULL,"
#             "PRIMARY KEY ('id' AUTOINCREMENT))")

if __name__ == "__main__":
    save_user()

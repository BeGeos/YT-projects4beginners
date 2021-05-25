import sqlite3
import json


# Connecting to DB
conn = sqlite3.connect("contacts.db")
cur = conn.cursor()

# Data example
example = {
    "contacts": [
        {
            "name": "myName",
            "mobile": "555-555-555",
            "home": "87678393"
        },
        {
            "name": "mySecondName",
            "mobile": "777-777-777",
            "home": "123456789"
        }
    ]
}


# create table for database with columns name, mobile and home
# run only once to create table
# cur.execute("""CREATE TABLE contacts ("id" INTEGER NOT NULL,
# "name" TEXT NOT NULL,
# "mobile" TEXT,
# "home" TEXT,
# PRIMARY KEY ("id" AUTOINCREMENT))""")


def create(data):
    for contact in data["contacts"]:
        try:
            cur.execute(f'INSERT INTO contacts (name, mobile, home) VALUES '
                        f'("{contact["name"]}", "{contact["mobile"]}", "{contact["home"]}")')
        except sqlite3.OperationalError as err:
            print(err)
            return

    conn.commit()
    print("New Record added!")
    return


# create(example)


def read(name=None):
    if not name:
        name = ""

    cur.execute(f'SELECT * FROM contacts WHERE "name" LIKE "%{name}%"')
    rows = cur.fetchall()
    records = {"results": []}

    for row in rows:
        record = {"name": row[1], "mobile": row[2], "home": row[3]}
        records["results"].append(record)

    pretty_records = json.dumps(records, indent=2)

    print(pretty_records)
    return


# read()


def _update_number(row):
    mobile = input("Enter a new mobile number (skip to leave unchanged): ")
    home = input("Enter a new home number (skip to leave unchanged): ")

    mobile = mobile if mobile != "" else row[2]
    home = home if home != "" else row[3]

    cur.execute(f'UPDATE contacts SET mobile="{mobile}", home="{home}" '
                f'WHERE name="{row[1]}"')

    conn.commit()
    return


def update(name):
    cur.execute(f'SELECT * FROM contacts WHERE "name" LIKE "%{name}%"')
    rows = cur.fetchall()

    if len(rows) == 1:
        row = rows[0]
        _update_number(row)
    else:
        print("Multiple results were found. Select which one: ")
        for row in rows:
            print(row)

        _id = input("Enter number here: ")
        cur.execute(f'SELECT * FROM contacts WHERE id={_id}')
        row = cur.fetchall()[0]
        _update_number(row)

    print("Number updated successfully!")
    return


def _delete_number(row):
    cur.execute(f'DELETE FROM contacts WHERE id={row[0]}')
    conn.commit()
    return


def delete(name):
    cur.execute(f'SELECT * FROM contacts WHERE "name" LIKE "%{name}%"')
    rows = cur.fetchall()

    if len(rows) == 1:
        row = rows[0]
        _delete_number(row)
    else:
        print("Multiple results were found. Select which one: ")
        for row in rows:
            print(row)

        _id = input("Enter number here: ")
        cur.execute(f'SELECT * FROM contacts WHERE id={_id}')
        row = cur.fetchall()[0]
        _delete_number(row)

    print("Number deleted successfully!")
    return


# Main logic
def main():
    while True:
        options = input("Select one of the options: Create (C) Read (R) Update (U) Delete (D) or Quit (Q) ")

        if options.lower() == "c":
            new_record = {
                "contacts": [
                    {
                        "name": input("Enter a name: "),
                        "mobile": input("Enter a mobile number: "),
                        "home": input("Enter a home number: ")
                    }
                ]
            }

            create(new_record)
        elif options.lower() == "r":
            name = input("Enter a name: ")
            read(name)
        elif options.lower() == "u":
            name = input("Enter a name: ")
            update(name)
        elif options.lower() == "d":
            name = input("Enter a name: ")
            delete(name)
        elif options.lower() == "q":
            print("Bye Bye")
            quit()
        else:
            print(f"No option {options} available!")


if __name__ == "__main__":
    main()

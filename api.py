import requests
import json
import sqlite3
from win10toast import ToastNotifier

API_URL = "https://randomuser.me/api/"

try:
    response = requests.get(API_URL)
    response.raise_for_status()

    status_code = response.status_code

    headers = response.headers

    data = response.json()

    with open("random_user.json", "w") as file:
        json.dump(data, file, indent=4)

    user = data["results"][0]
    name = user["name"]["first"] + " " + user["name"]["last"]
    email = user["email"]
    username = user["login"]["username"]
    location = user["location"]["city"] + ", " + user["location"]["country"]
    phone = user["phone"]

    sep = "--------------------------"
    print(sep)
    print("Random User Information:\n"+sep)
    print("Name:", name)
    print("Email:", email)
    print("Username:", username)
    print("Location:", location)
    print("Phone:", phone)
    print(sep)

    a = input("Extra information? Yes/*AnyKey ")
    if a == "Yes":
        print("Status Code:", status_code)

        print("Response Headers:")
        for header, value in headers.items():
            print(f"{header}: {value}")
        print(sep)
    else:
        print("Information has been saved to JSON file")

    conn = sqlite3.connect("emails.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS emails
                (name TEXT, email TEXT)''')

    c.execute("INSERT INTO emails (name, email) VALUES (?, ?)", (name, email))

    conn.commit()
    conn.close()

    # toaster = ToastNotifier()
    # toaster.show_toast("Random User Information",
    #                         f"Name: {name}\nEmail: {email}",
    #                         duration=3)

    print("Email address saved to SQLite database.")

except requests.exceptions.HTTPError as err:
    print("Error:", err)

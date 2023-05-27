# RandomPersonAPI
Using **Random User Generator API** - https://randomuser.me/ i am creating random user profile including name, email, username, location, phone.
It also saves the data to a JSON file, and stores the user's name and email in an SQLite database.

## Requirements
- Python 3
- `requests` library
- `json` library
- `sqlite3` library
- `win10toast` library

## Usage

1. Clone or download the script to your local machine.
2. Install the required libraries mentioned in the requirements section.
3. Run the script using the following command:
`python random_user_info.py`
5. The script will fetch random user information from the API, display the user's name, email, username, location, and phone number.
6. You will be prompted to enter whether you want to display extra information or not.
- If you enter "Yes", it will display the status code of the API response and the response headers.
- It will save the information to a JSON file anyway.
7. The script will then save the user's name and email to an SQLite database named `emails.db`.
8. If you have enabled the desktop notifications (uncommented the relevant code), a toast notification will also be displayed with the user's name and email.
9. The script will print a message confirming the successful saving of the email address to the database.

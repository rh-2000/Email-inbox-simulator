# Email Inbox Simulation
This repository contains a Python program that simulates an email inbox with a menu to allow the user to send, read, and modify emails.

## Email Class
The Email class is defined in email.py. It has the following properties:

* `from_address`: the email address of the sender
* `email_contents`: the contents of the email
* `has_been_read`: a boolean value indicating whether the email has been read or not
* `is_spam`: a boolean value indicating whether the email is spam or not

The Email class has the following methods:

* `mark_as_read()`: marks the email as read
* `mark_as_spam()`: marks the email as spam
* `__str__()` : returns a string format for the given email

## Inbox
The inbox list contains instances of the Email class. The program includes two email objects that are added to the inbox list each time it is run. The user can add new emails to the inbox using the `add_email()` method.

## Menu
The program presents a menu to the user with the following options:

* `read`: allows the user to read emails
* `all emails`: displays all emails in the inbox
* `all unread emails`: displays only the unread emails in the inbox
* `spam`: displays only the spam emails in the inbox
* `specific email`: allows the user to select a specific email to read
* `mark spam`: allows the user to mark an email as spam
* `send`: allows the user to send a new email and add it to the inbox
* `quit`: exits the program

## How to Run
To run the program, simply run the email.py file in your Python environment. The program will present a menu to the user, and the user can select options by entering the corresponding number or word.

Note that each time the program is run, the two email objects added to the inbox list will always appear in the inbox. If one or both are deleted, then the program is restarted, both will reappear.

#An Email Simulation

class Email():

    def __init__(self, from_address, email_contents):
        self.from_address = from_address
        self.email_contents = email_contents
        self.has_been_read = False
        self.is_spam = False

    def mark_as_read(self):
        self.has_been_read = True
        print("Email has been marked as read.")
    
    def mark_as_spam(self):
        self.is_spam = True
        print("Email has been marked as spam.")
    
    # returning a string format for the given email
    def __str__(self):
        return f"{self.from_address}, {self.email_contents}"

inbox = []

# setting up a couple of email objects to add to the inbox list
# after each new run of the program, these emails will always appear in the inbox
# (i.e. if one or both are deleted then the program is restarted, both will reappear)
email1 = Email('noreply@apple.com', 'Your recent purchase with Apple')
email2 = Email('support@hyperiondev.com', 'Welcome onboard the bootcamp!')
email3 = Email('bob@bob.com', 'wasssssup dog')

inbox.append(email1)
inbox.append(email2)

# using the email class to create a new object in this method
def add_email(e_from, e_contents):
    new_email = Email(e_from, e_contents)
    inbox.append(new_email)
    for i, mail in enumerate(inbox):
        print(f"{i+1}: {mail.from_address}, {mail.email_contents}")

def get_count():
    return len(inbox)

# reading all emails in the inbox using enumerate so i can print a counter(index) alongside each one
def all_emails():
    for i, mail in enumerate(inbox):
        print(f"{i+1}: {mail.from_address}, {mail.email_contents}")

# marking each email requested under this function as read
def get_email(i):
    if 0 <= (i) < len(inbox):
        email = inbox[i]
        print(f"{i+1}: {email.from_address}, {email.email_contents}")
        email.mark_as_read()
    else:
        print(f"{i} is an invalid index.")

def get_unread_emails():
    print(f"\nUnread emails:\n")
    for i, mail in enumerate(inbox):
        if not mail.has_been_read:
            print(f"{i+1}: {mail.from_address}, {mail.email_contents}")

def get_spam_emails():
    print(f"\nSpam emails:\n")
    for i, mail in enumerate(inbox):
        if mail.is_spam:
            print(f"{i+1}: {mail.from_address}, {mail.email_contents}")


def delete(i):
    inbox.pop(i-1)
    print(f"Email {i} has been deleted.")

user_choice = ""

while user_choice != "quit":
    user_choice = input("\nWhat would you like to do - read/mark spam/send/quit?: ").lower()
    
    if user_choice == "read":
        print(f'''
        Which email(s) would you like to read:
        1 - all emails
        2 - all unread emails
        3 - spam
        4 - specific email
        ''')
        read_choice = input(f"\nChoice: ")
        if read_choice == '1':
            all_emails()
        elif read_choice == '2':
            get_unread_emails()
        elif read_choice == '3':
            get_spam_emails()
        elif read_choice == '4':
            # using try-except block here to handle ValueErrors if user doesn't input an integer
            while True:
                try:
                    i = int(input("Enter the index of the email you wish to access: "))
                    break
                except ValueError:
                    print(f"Invalid response. Please enter a valid number.")
            get_email(i-1)
            # included the option to delete here and utilised the delete() function
            # used a while loop to continuosly check for correct input
            del_choice = input("Would you like to delete this email? (Y / N): ").upper()
            while True:
                if del_choice == "Y":
                    delete(i)
                    break
                elif del_choice == "N":
                    break
                else:
                    print("Invalid response. Please enter 'Y' or 'N'.")
                    del_choice = input("Would you like to delete this email?: ").upper()
                    continue
        else:
            print("Invalid response.")
    
    # using another try-excpet block for value error handling
    elif user_choice == "mark spam":
        while True:
            try:
                spam_index = int(input("Enter the index of the email you wish to mark as spam: "))
                break
            except ValueError:
                print(f"Invalid response. Please enter a valid number.")
        inbox[spam_index-1].mark_as_spam()
    
    # taking user inputs here then creating the object within the called function/method
    elif user_choice == "send":
        email_from = input("Enter your email address: ")
        contents = input("Enter the contents of your email here: ")
        add_email(email_from, contents)
    
    elif user_choice == "quit":
        print("Goodbye")
        break
    
    else:
        print("Oops - incorrect input")
import re

# function to help make sure that phone number user input is valid

def get_phone(edit):
        while True:
            match = False
            with open('contact_file.txt', 'r') as file:
                phone = input("Please enter 10-digit phone number: ")
                if len(phone) != 10:
                        print(f"Invalid entry. Phone number must be exactly 10 digits. Try again.")
                else:
                    try:
                        int(phone) > -1
                    except ValueError as ve:
                        print(f"Invalid entry. Phone number must contain numeric characters only. Try again.")
                    except Exception as e:
                        print(f"Exception: {e}")
                    else:
                        file_content = file.readlines()
                        for line in file_content:
                            if re.match(f"Phone: {phone}", line):
                                if edit == True:
                                    print(f"phone number {phone} found.")
                                    return phone
                                match = True
                        if edit == True:
                                print(f"Phone number {phone} not found.")
                        elif match != True:
                            return phone
                        else:
                            print(f"Phone number {phone} already in contacts.\nTry again.")
                        
# function to help make sure that email user input is valid

def get_email():
    while True:
        email = input("Please enter Email address: ")
        if re.match(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,24}\b", email):
            return email
        else:
            print(f"Invalid entry. Email must be in following example format: address@site.com\nTry again.")

# function to help make sure that name user input is valid

def get_name():
    while True:
        name = input("Please enter name: ")
        if re.match(r"\b[A-Za-z -.']{1,747}\b", name):
            return name
        else:
            print(f"Invalid entry. That was not a name and you know it bucko.")

def replace_number():
    edit = True
    old_phone = get_phone(edit)
    print(f"What 10-digit number would you like to replace {old_phone} with?\n")
    edit = False
    new_phone = get_phone(edit)
    with open("contact_file.txt", 'r+') as file:
        file_contents = file.read()
        updated_file_contents = re.sub(f"Phone: {old_phone}",f"Phone: {new_phone}", file_contents)
        file.seek(0)
        file.write(updated_file_contents)
        file.truncate()
        return print(f"{old_phone} successfully replaced with {new_phone}")

def replace_email(contact_dict):
    while True:
        old_email = get_email()
        for phone_number in contact_dict:
            for key, value in contact_dict[phone_number].items():
                if key == "Email" and value == old_email:
                    print(f"Email address {old_email} found.")
                    found = True
                    while found == True:
                        new_email = input("Please enter new Email address: ")
                        if re.match(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,24}\b", new_email):
                            with open("contact_file.txt", 'r+') as file:
                                file_contents = file.read()
                                updated_file_contents = re.sub(f"Email: {old_email}",f"Email: {new_email}", file_contents)
                                file.seek(0)
                                file.write(updated_file_contents)
                                file.truncate()
                                return print(f"{old_email} successfully replaced with {new_email}")
                        else:
                            print(f"Invalid entry. Email must be in following example format: address@site.com\nTry again.")            
        print("Email not located.")

def replace_name(contact_dict):
    while True:
        old_name = get_name()
        for phone_number in contact_dict:
            for key, value in contact_dict[phone_number].items():
                if key == "Name" and value == old_name:
                    print(f"Name {old_name} found.")
                    found = True
                    while found == True:
                        new_name = input("Please enter name: ")
                        if re.match(r"\b[A-Za-z -.']{1,747}\b", new_name):
                            with open("contact_file.txt", 'r+') as file:
                                file_contents = file.read()
                                updated_file_contents = re.sub(f"Name: {old_name}",f"Name: {new_name}", file_contents)
                                file.seek(0)
                                file.write(updated_file_contents)
                                file.truncate()
                                return print(f"{old_name} successfully replaced with {new_name}")
                        else:
                            print(f"Invalid entry. That was not a name and you know it bucko.\nTry again.")
        print("Name not located.")


def add_note():
    edit = True
    phone = get_phone(edit)
    edit = False
    new_notes = input("Please enter new notes for this contact (e.g. address, notes): ")
    with open("contact_file.txt", 'r+') as file:
        file_contents = file.read()
        pattern_of_line = (rf"Phone: {phone}.*\n")
        line_to_replace = re.search(pattern_of_line, file_contents).group(0)
        updated_line = line_to_replace.strip() + f" + NEW NOTE: {new_notes}\n"
        updated_file_contents = file_contents.replace(line_to_replace, updated_line)
        file.seek(0)
        file.write(updated_file_contents)
        return print(f"Contact {phone} successfully added note: {new_notes}")

def init_contact_dict():
    contact_dict = {}
    with open("contact_file.txt", 'r') as file:
        file_contents = file.readlines()
        for line in file_contents:
            line_groups = re.search(r"Phone: ([0-9]{10}), Name: ([A-Za-z -.']{1,747}), Email: ([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,24}), Notes: (.*\n)", line)
            if line_groups:
                contact_dict[line_groups.group(1)] = {'Name': line_groups.group(2), 'Email': line_groups.group(3), 'Notes': line_groups.group(4).strip()}
        return contact_dict
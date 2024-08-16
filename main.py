from helpers import *

# the menu as a function. Calls all of the other functions based on user input

def menu():
    while True:
        selection = input("Welcome to the Contact Management System!\nMenu:\n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Import contacts from a text file\n8. Quit\n\nPlease make selection (1-8): ")
        if selection == '1':
            add_contacts(init_contact_dict())
        elif selection == '2':
            edit_contact()
        elif selection == '3':
            delete_contact()
        elif selection == '4':
            find_contact(init_contact_dict())
        elif selection == '5':
            display_contacts()
        elif selection == '6':
            export_contacts(init_contact_dict())
        elif selection == '7':
            import_contacts(init_contact_dict())
        elif selection == '8':
            print("Thank you for using the Contact Management System! Goodbye.")
            break 
        else:
            print("Not a valid option. Must be 1-8.")

# adding contacts to the file as function. Calls asome more input based functions
def add_contacts(contact_dict):
    while True:
            edit = False
            phone = get_phone(edit)
            name = get_name()
            email = get_email()
            notes = input("Please enter any additional information for this contact (e.g. address, notes): ")
            contact_dict[phone] = {'Name' : name, 'Email' : email, 'Notes' : notes}
            with open("contact_file.txt", 'w') as file:  
                        for key, value in contact_dict.items():  
                            file.write(f"Phone: {key}, Name: {value['Name']}, Email: {value['Email']}, Notes: {value['Notes']}\n")
            print(f"Contact information for phone number {phone} recorded")
            choice = '?'
            while choice != 'y':
                choice = input("\nContinue adding contacts (y/n)? ").lower()
                if choice == 'n':
                    return
                elif choice != 'y':
                    print("Invalid choice. Choice must be either 'y' or 'n'.")

def edit_contact():
    while True:
        selection = input("Which would you like to edit from below:\n1. Phone number\n2. Email address \n3. Name\n4. Notes\n5. Return to menu\n")
        if selection == '1':
            replace_number()
        elif selection == '2':
            replace_email(init_contact_dict())
        elif selection == '3':
            replace_name(init_contact_dict())
        elif selection == '4':
            add_note()
        elif selection == "5":
            return
        else:
            print("Not a valid option. Must be 1-5.")

def delete_contact():
    while True:
        edit = True
        phone = get_phone(edit)
        with open("contact_file.txt", 'r+') as file:
            file_contents = file.read()
            pattern_of_line = (rf"Phone: {phone}.*\n")
            line_to_replace = re.search(pattern_of_line, file_contents).group(0)
            updated_file_contents = file_contents.replace(line_to_replace, "")
            file.seek(0)
            file.write(updated_file_contents)
            file.truncate()
            print(f"Contact {phone} removed.")
            choice = '?'
            while choice != 'y':
                choice = input("\nContinue removing contacts (y/n)? ").lower()
                if choice == 'n':
                    return
                elif choice != 'y':
                    print("Invalid choice. Choice must be either 'y' or 'n'.")

def find_contact(contact_dict):
    while True:
        edit = True
        found = False
        selection = input("Search by:\n1. Phone number\n2. Email address \n3. Name\n4. Return to menu\n")
        if selection == '1':
            phone = get_phone(edit)
            print(f"\nPhone: {phone}")
            for key, value in contact_dict[phone].items():
                print(f"       {key}: {value}")
            print("")
        elif selection == '2':
            email = get_email()
            with open("contact_file.txt", 'r+') as file:
                file_content = file.readlines()
                for line in file_content:
                    if re.match(rf".*Email: {email},", line):
                        found = True
                        print(f"Email address {email} found.")
                        line_groups = re.search(r"Phone: ([0-9]{10}), Name: ([A-Za-z -.']{1,747}), Email: ([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,24}), Notes: (.*\n)", line)
                        print(f"\nEmail: {line_groups.group(3)}\nPhone: {line_groups.group(1)}\nName: {line_groups.group(2)}\nNotes: {line_groups.group(4)}")
                if found == False:
                    print(f"Email address {email} not found in contacts.")
        elif selection == '3':
            name = get_name()
            with open("contact_file.txt", 'r+') as file:
                file_content = file.readlines()
                for line in file_content:
                    if re.match(rf".*Name: {name},", line):
                        found = True
                        print(f"Name {name} found.")
                        line_groups = re.search(r"Phone: ([0-9]{10}), Name: ([A-Za-z -.']{1,747}), Email: ([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,24}), Notes: (.*\n)", line)
                        print(f"\nName: {line_groups.group(2)}\nPhone: {line_groups.group(1)}\nEmail: {line_groups.group(3)}\nNotes: {line_groups.group(4)}")
                if found == False:
                    print(f"Name {name} not found in contacts.") 
        elif selection == '4':
            edit = False
            return
        else:
            print("Not a valid option. Must be 1-4.")

def display_contacts():
    contact_dict = init_contact_dict()
    print("\nContacts:\n")
    for phone_number in contact_dict:
        print(f"Phone: {phone_number}")
        for key, value in contact_dict[phone_number].items():
            print(f"       {key}: {value}")
        print("")

def export_contacts(contact_dict):
    while True:
        new_file_name = f"{input('Please name a text file to export contacts to (can be new), do NOT include the file extension. For instance .txt): ')}.txt"
        with open(new_file_name, 'a') as file:
            for phone_number in contact_dict:
                file.write(f"Phone: {phone_number}, ")
                for key, value in contact_dict[phone_number].items():
                    if key != "Notes":
                        file.write(f"{key}: {value}, ")
                    else:
                        file.write(f"{key}: {value}\n")
            print(f"\nFile {new_file_name} successfully appended.")
            choice = '?'
            while choice != 'y':
                choice = input("\nContinue adding contacts (y/n)? ").lower()
                if choice == 'n':
                    return
                elif choice != 'y':
                    print("Invalid choice. Choice must be either 'y' or 'n'.")



            
            print(f"Contacts exported to {new_file_name}.")
            choice = '?'
            while choice != 'y':
                choice = input("\nContinue adding contacts (y/n)? ").lower()
                if choice == 'n':
                    return
                elif choice != 'y':
                    print("Invalid choice. Choice must be either 'y' or 'n'.")

def import_contacts(contact_dict):
    while True:
        new_file_name = f"{input('Please name a file to import contacts from (do NOT include the file extension. For instance .txt): ')}.txt"
        with open(new_file_name, 'r') as file, open('contact_file.txt', 'w') as home_file:
            file_contents = file.readlines()
            for line in file_contents:
                line_groups = re.search(r"Phone: ([0-9]{10}), Name: ([A-Za-z -.']{1,747}), Email: ([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,24}), Notes: (.*)", line)
                if line_groups:
                    file_imported = True
                    contact_dict[line_groups.group(1)] = {'Name': line_groups.group(2), 'Email': line_groups.group(3), 'Notes': line_groups.group(4).strip()}
            if file_imported:
                for phone_number in contact_dict:
                    home_file.write(f"Phone: {phone_number}, ")
                    for key, value in contact_dict[phone_number].items():
                        if key != "Notes":
                            home_file.write(f"{key}: {value}, ")
                        else:
                            home_file.write(f"{key}: {value}\n")
                print(f"\nFile {new_file_name} successfully imported.")
            else:
                print("File not formatted properly for import. Each line must look like sample line below:\n\nPhone: 1234567890, Name: Example-First-Name O'Last-Name Jr., Email: example@email.ex, Notes: example notes")
            choice = '?'
            while choice != 'y':
                choice = input("\nContinue adding contacts (y/n)? ").lower()
                if choice == 'n':
                    return
                elif choice != 'y':
                    print("Invalid choice. Choice must be either 'y' or 'n'.")
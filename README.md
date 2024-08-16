This Repository is a mini-project for Coding Temple. 

TABLE OF CONTENTS:
1. app.py
2. main.py
3. helpers.py
4. contact_file.txt
5. example_export.txt
6. project_outline.txt
7. conclusion


1. app.py

  The application runs through the app.py file. It does so by:
  1st: importing all custom functions from main.py.
  2nd: assigning variable 'contact_dict' a value of calling the custom function init_contact_dict() without any arguments.
  3rd calling custom function menu() without any arguments.

2. main.py

  The application's primary functions are defined in this file. In addition, the file imports all custom functions from helpers.py.
  
  Functions defined here:
  
      1. menu()
    
        This function prints a formatted selection menu in the CLI and conditionally calls all other primary functions depending on user input.
        It takes zero arguments and returns nothing (I used a **break** instead).
    
        The sub-functions (all of which will be defined later) that this function calls are as follows:
    
        1. add_contacts()
        2. init_contact_dict()
        3. edit_contacts()
        4. delete_contacts()
        5. find_contact()
        6. display_contacts()
        7. export_contacts()
        8. import_contacts()
        
      2. add_contacts(contact_dict)
      
        This function allows users to add new contacts to their contact dictionary and file.
        This function takes one argument. This argument is intended to be a dictionary collection.
        It collects three variables using helper functions:
          1. phone
          2. name
          3. email
        and collects a fourth using a standard input function:
          4. notes
        
        With these four variables, the function updates the dictionary (provided in the argument) with the phone variable as a key and the other three as values for that key.
        The function then writes the full dictionary to our permanent contact storage file contact_file.txt
    
        The sub-functions (all of which will be defined later) that this function calls are as follows:
    
        1. get_phone()
        2. get_name()
        3. get_email()
    
      3. edit_contacts()
    
        This function allows users to change details about the contacts in their contact dictionary and permanent file.
        This function takes no arguments. Instead, it functions like menu(), providing users with a CLI-based interactive selection space. 
    
        The sub-functions (all of which will be defined later) that this function calls are as follows:
    
        1. replace_number()
        2. replace_email()
        3. replace_name()
        4. add_note()
    
      4. delete_contacts()
    
        This function deletes contacts from the dictionary of contacts and the permanent file.
        This function takes no arguments. Once called, it calls a sub-function (get_phone()) to return a value to assign to a variable called phone.
    
        The function then:
        1. opens contact_file.txt in the r+ mode (allowing it to change the file).
        2. reads the file into a variable called file_contents
        3. searches file_contents for a pattern containing the variable phone
        4. in a new variable, copies file_contents and replaces the line where that pattern is found with ""; in other words - deleting that line.
        5. overwrites the actual file with the variable copy that is an exact duplicate except with the patterned line removed.
    
      5. find_contact()
    
        This function takes a query from the user  and searches through the contact list and prints additional information about the queried contact. 
        This function takes one argument. The argument is intended to be a dictionary collection.
        This function takes no arguments.
    
        This function provides the user with three options by which to query
          1. phone number, using the get_phone() helper function.
          2. email, using the get_email() helper function and methods from the re module.
          3. name, using the get_name() helper function and methods from the re module.
          
     6. display_contacts()
    
            This function prints a formatted display of the items in the contact dictionary and uses sub-function init_contact_dict() to ensure the collection is synced before doing so.
    
    7. export_contacts()
    
           This function exports a text file (either by appending or creating a new file) containing a copy of the contact collection's contents. The file is formatted to match the primary text file and the CLI display of contact information, allowing it to be searched using the same regex patterns.
           This function takes one argument; it is intended that this argument be the primary dictionary storing the contact information.
    
    9. import_contacts()
    
           This function imports the information in a text file into the primary dictionary if the file is formatted properly.

3. helpers.py

   This file defines the application's secondary/helper functions and imports the re module.

   Functions defined here:

       1. get_phone()

          The purpose of this function is to allow the user to input a valid phone number. This function takes one argument, a boolean variable, to contextually determine whether it accepts values found in the collection it compares against or does not accept. 

       2. get_email()

           The purpose of this function is to allow the user to input a valid email address.
   
       3. get_name()
   
            The purpose of this function is to allow the user to input a valid name.
   
       4. replace_number()

            This function allows the user to change a contact's key (phone number) moniker while retaining the original key's associated values.
   
       5. replace_email()

            This function allows the user to change the value of the key that holds a particular contact's email address.

       6. replace_name()

            This function allows the user to change the value of the key that holds a particular contact's name.

       7. add_note()

             This function allows the user to append the key value that holds a particular contact's note section.

       8. init_contact_dictionary()

             This function initializes the primary collection for contacts (the variable contact_dict) by syncing it with the permanent file.

   
4. contact_file.txt

   This file contains a permanent collection of contacts formatted to be accessed when performing the application by running app.py 

5. example_export.txt

   This is an example text file that I encourage users to utilize when first trying out the import_contacts() function. It has no purpose in the actual application. And it can be deleted - no one will shed a tear.

   
6. project_outline.txt

   This file contains the prompts for the assignment.



7. Conclusion

   Looking back, I could have made this much more efficient by utilizing the dictionaries more and sanctioning off any file handling to the import and export functions.
   That being said, I think that functionally, the fact that the file updates as you go is more user-friendly than that more code-efficient solution, so it's a double-edged sword.

   Additionally, quite a bit of code is repeated in this project. I think there's much room for more efficiency in the future. I will need to take more time to consider modularity more thoroughly.
























    
      
      



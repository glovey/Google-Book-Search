""" This file contains system Logic - enabling a user to search Google Books, add books to a reading list and manage
that reading list. """

from google_search import do_search
from print_library import print_library
from add_to_reading_list import add_to_reading_list
from manage_saved_list import save_list
from manage_saved_list import load_list
from manage_saved_list import delete_list


''' Ask user what they would like to do on the system: search / check reading list / delete saved reading list / 
save list and shut down '''
system_on = True
reading_list = []

while system_on:
    choice = None
    while choice not in ["1", "2", "3", "4", "5"]:
        print("\nWhat would you like to do?\n")
        print("1. Search Google Books")
        print("2. Check your reading list")
        print("3. Load your saved reading list.")
        print("4. Delete your saved reading list")
        print("5. Save your reading list and shut down")
        choice = input("choose 1, 2, 3, 4 or 5\n")
        if choice not in ["1", "2", "3", "4", "5"]:
            print("That's not a valid choice, please try again.")

    ''' Perform actions dependant on user input, based on option above '''
    if choice == "1":
        add_to_reading_list(do_search(), reading_list)
        choice = None

    elif choice == "2":
        if len(reading_list) != 0:
            print("\nHere is your reading list:\n")
            print_library(reading_list)
            print("\n")
        else:
            print("Your reading list is empty\n")
            choice = None

    elif choice == "3":
        reading_list = load_list(reading_list)

    elif choice == "4":
        delete_list()

    else:
        keep_list = None
        while keep_list not in ["yes", "no"]:
            keep_list = input(
                "Would you like to save your reading list before you go? Answer yes or no.\nPlease note this will "
                "overwrite any previously saved reading list.\n ").lower()
            if keep_list not in ["yes", "no"]:
                print("That's not a valid option, please try again\n")
        if keep_list == "yes":
            save_list(reading_list)
            print("Your list has been saved for next time\n")
            keep_list = None
        else:
            print("Your reading list has not been saved\n")
            keep_list = None
        print("Thank you for using Joe books. Goodbye. ")
        system_on = False

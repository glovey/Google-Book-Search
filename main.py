""" This file contains system Logic - enabling a user to search Google Books and add books to a reading list """

from google_search import do_search
from print_library import print_library
from add_to_reading_list import add_to_reading_list
from save_load_list import save_list
from save_load_list import load_list
import os

''' Ask user what they would like to do on the system: search / check reading list / shut down '''
system_on = True
reading_list = []

while system_on:
    choice = None
    while choice not in ["1", "2", "3","4","5"]:
        print("\nWhat would you like to do?\n")
        print("1. Search Google Books")
        print("2. Check your reading list")
        print("3. Load previous reading list. Please note this will overwrite your current reading list.")
        print("4. Delete your reading list")
        print("5. Save your reading list and shut down")
        choice = input("choose 1, 2, 3, 4 or 5\n")
        if choice not in ["1", "2", "3","4", "5"]:
            print("That's not a valid choice, please try again.")

    ''' Depending on user input: '''

    ''' Perform book search and ask if they want to add books to reading list, check the reading list, or close down 
    the system '''
    if choice == "1":
        add_to_reading_list(do_search(), reading_list)
        choice = None
    elif choice == "2":
        if len(reading_list) != 0:
          print("\nHere is your reading list:\n")
          print_library(reading_list)
          print ("\n")  
          
        else:
          print("Your reading list is empty\n")
          choice = None
    elif choice == "3":
      reading_list = load_list(reading_list)
    elif choice == "4":
      try:
        os.remove("saved_reading_list.pickle")
        print ("\nYour reading list has been deleted.")
      except:
        print ("You haven't saved any books to a reading list")
    else:
        keep_list = None
        while keep_list not in ["yes", "no"]:
          keep_list = input("Would you like to save your reading list before you go? Answer yes or no.\n Please note this will overwrite any previously saved reading list\n. ").lower()
          if keep_list not in ["yes", "no"]:
            print("That's not a valid option, please try again\n")
        if keep_list == "yes":
          save_list(reading_list)
          print ("Your list has been saved for next time\n")
          keep_list = None
        else:
          print ("Your reading list has not been saved\n")
          keep_list = None
        print("Thank you for using Joe books. Goodbye. ")
        system_on = False

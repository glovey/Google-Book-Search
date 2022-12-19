#files
from create_book import Book
from google_search import do_search
from print_library import print_library
from add_to_reading_list import add_to_reading_list

#Variables
system_on = True
search = True
reading_list = []
add_book = None
book_choice = None
choice = None

#System Logic

#Ask user what they would like to do on the system: search / check reading list / shut down
while system_on:
  while choice not in ["1","2","3"]:
    print ("What would you like to do?\n")
    print ("1. Search Google Books") 
    print ("2. Check your reading list")
    print ("3. Shut down")
    choice = input("choose 1, 2 or 3\n")
    if choice not in ["1","2","3"]:
      print ("That's not a valid choice, please try again.")
  
  # If user wants to search, perform search and ask if they want to add books to reading list
  if choice == "1":
    add_to_reading_list(do_search(), reading_list)
    choice = None
  elif choice == "2":
    if len(reading_list) == 0:
      print ("Your reading list is empty\n")
      choice = None
    else:
      print ("Here is your reading list:\n")  
      print_library(reading_list)  
      choice = None
  else:
    print ("Thank you for using Joe books. Goodbye. ")
    system_on = False


    
  
  # Ask user if they would like to add a book to their Reading List
  
  
  
  
  
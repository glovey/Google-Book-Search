from print_library import print_library

def add_to_reading_list(query_results, reading_list):
  add_book = None
  while add_book not in ["yes", "no"]:
    add_book = input("Would you like to add a book to you reading list? Answer yes or no.\n").lower()
    if add_book not in ["yes", "no"]:
      print ("that's not a valid option, please try again\n")

  
  while add_book == "yes":
    book_choice = int(input(f"which book would you like to add? Give a number between 1 and {len(query_results)}.\n"))-1
    if query_results[book_choice] not in reading_list:
      reading_list.append(query_results[book_choice])
      print ( f"{query_results[book_choice].title} has been added to you reading list.\n")
    else:
      print ( f"{query_results[book_choice].title} is already in your reading list.\n")
    
    another_book = None
    while another_book not in ["yes", "no"]:
      another_book = input  ("Would you like to add another book? Answer yes or no\n").lower()
      if another_book not in ["yes", "no"]:
        print ("that's not a valid option, please try again\n")
      if another_book == "yes":
        print_library(query_results)
      elif another_book == "no":
        add_book = None
        
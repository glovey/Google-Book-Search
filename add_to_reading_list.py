from print_library import print_library


def add_to_reading_list(query_results, reading_list):
    """ Ask user if they want to add book a book to reading list. Continue to ask and add until user stops process.

        Parameters:
            query_results: array (array of books from search, stored as Book objects
            reading_list: array (from main) (array of books added by user to 'reading list', stored as Book objects)
        Updates:
            reading list: array (array of books added by user to 'reading list', stored as Book objects
    """

    ''' Skip this step if query returned no results '''
    if len(query_results) == 0:
        pass
    else:
        ''' Ask user if they want to add a book to their reading list '''
        add_book = None
        while add_book not in ["yes", "no"]:
            add_book = input("Would you like to add a book to you reading list? Answer yes or no.\n").lower()
            if add_book not in ["yes", "no"]:
                print("that's not a valid option, please try again\n")

        ''' Ask user which book they would like to add. Add if not already in list '''
        while add_book == "yes":
            book_choice = None
            while book_choice not in range(0, len(query_results)):
                try:
                    book_choice = int(input(f"which book would you like to add? Give a number between 1 and"
                                            f" {len(query_results)}.\n")) - 1
                    if book_choice not in range(0, len(query_results)):
                        print("that's not a valid option, please try again\n")
                except ValueError:
                    print("that's not a valid option, please try again\n")

            '''Add book if not already in reading list'''
            if query_results[book_choice] not in reading_list:
                reading_list.append(query_results[book_choice])
                print(f"{query_results[book_choice].title} has been added to you reading list.\n")
            else:
                print(f"{query_results[book_choice].title} is already in your reading list.\n")

            ''' Ask user if they want to add another book, repeat process until user states 'no' '''
            another_book = None
            while another_book not in ["yes", "no"]:
                another_book = input("Would you like to add another book? Answer yes or no\n").lower()
                if another_book not in ["yes", "no"]:
                    print("That's not a valid option, please try again\n")
                if another_book == "yes":
                    print_library(query_results)
                elif another_book == "no":
                    add_book = None

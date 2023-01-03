import os
import pickle
from print_library import print_library


def load_list(reading_list):
    """
    Load previously saved (pickled) data within the file "saved_reading_list.pickle". Data will be an array as per
    "save_list()". Advise user if this file does not exist.

        Parameters:
            reading_list: array (from main) (array of books added by user to 'reading list', stored as Book objects)

        Input:
            saved_reading_list.pickle: file (containing saved library in binary)

        Returns:
            library: array (of Book objects or empty if no save file exists)
    """
    current_reading_list = reading_list
    if len(current_reading_list) > 0 and os.path.exists("saved_reading_list.pickle"):

        merge_list = None
        while merge_list not in ["yes", "no"]:
            merge_list = input(
                "You currently have books in your reading list. Do you want to merge this list with your "
                "saved list? Otherwise the Loaded list will replace your current list. Enter yes or "
                "no\n").lower()
            if merge_list not in ["yes", "no"]:
                print("that's not a valid option, please try again\n")
        if merge_list == "yes":
            with open("saved_reading_list.pickle", "rb") as f:
                loaded_list = pickle.load(f)
                print("your previous reading list has been loaded\n")
            for x in loaded_list:
                for y in current_reading_list:
                    if x.title == y.title and x.authors == y.authors and x.publisher == y.publisher:
                        pass
                    else:
                        current_reading_list.append(x)
            return current_reading_list
        else:
            try:
                with open("saved_reading_list.pickle", "rb") as f:
                    loaded_list = pickle.load(f)
                    print("your previous reading list has been loaded\n")
                    return loaded_list
            except FileNotFoundError:
                if len(reading_list) > 0:
                    print("You haven't saved any books to a reading list")
                    return reading_list
                else:
                    print("You haven't saved any books to a reading list")
                    return []

    else:
        try:
            with open("saved_reading_list.pickle", "rb") as f:
                loaded_list = pickle.load(f)
                print("your previous reading list has been loaded\n")
                return loaded_list
        except FileNotFoundError:
            if len(reading_list) > 0:
                print("You haven't saved any books to a reading list")
                print_library(reading_list)
                return reading_list
            else:
                print("You haven't saved any books to a reading list")
                print_library(reading_list)
                return []

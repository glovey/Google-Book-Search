import pickle
import os


def save_list(library):
    """
    Pickle library argument provided to give a file of the pickled data in binary.

        Parameters:
            library: array

        Output:
            saved_reading_list.pickle: file (containing saved library in binary)
    """
    with open("saved_reading_list.pickle", "wb") as f:
        pickle.dump(library, f, pickle.HIGHEST_PROTOCOL)


def load_list(reading_list):
    """
    Load previously saved (pickled) data within the file "saved_reading_list.pickle". Data will be an array as per
    "save_list()". if current reading list and saved reading list contain books, offer to merge lists,
    otherwise overwrite current reading list with saved reading list. Advise if no saved list exists.

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
                count = 0
                for y in current_reading_list:
                    if x.title == y.title and x.authors == y.authors and x.publisher == y.publisher:
                        count += 1
                    else:
                        pass
                if count > 0:
                    pass
                else:
                    reading_list.append(x)

            return reading_list
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
                return reading_list
            else:
                print("You haven't saved any books to a reading list")
                return []


def delete_list():
    """
    Delete the file "saved_reading_list.pickle". Advise user if this file does not exist.

    """

    try:
        os.remove("saved_reading_list.pickle")
        print("\nYour reading list has been deleted.")
    except FileNotFoundError:
        print("You haven't saved any books to a reading list")

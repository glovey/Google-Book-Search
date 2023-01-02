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


def load_list():
    """
    Load previously saved (pickled) data within the file "saved_reading_list.pickle". Data will be an array as per
    "save_list()". Advise user if this file does not exist.

        Input:
            saved_reading_list.pickle: file (containing saved library in binary)

        Returns:
            library: array
    """

    try:
        with open("saved_reading_list.pickle", "rb") as f:
            loaded_list = pickle.load(f)
            print("your previous reading list has been loaded\n")
            return loaded_list
    except FileNotFoundError:
        print("You haven't saved any books to a reading list")


def delete_list():
    """
    Delete the file "saved_reading_list.pickle". Advise user if this file does not exist.

    """

    try:
        os.remove("saved_reading_list.pickle")
        print("\nYour reading list has been deleted.")
    except FileNotFoundError:
        print("You haven't saved any books to a reading list")

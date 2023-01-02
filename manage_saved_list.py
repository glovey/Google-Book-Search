import pickle
import os
from create_book import Book


def save_list(library):
    with open("saved_reading_list.pickle", "wb") as f:
        pickle.dump(library, f, pickle.HIGHEST_PROTOCOL)


def load_list():
    try:
        with open("saved_reading_list.pickle", "rb") as f:
            library = pickle.load(f)
            print("your previous reading list has been loaded\n")
            return library
    except FileNotFoundError:
        print("You haven't saved any books to a reading list")


def delete_list():
    try:
        os.remove("saved_reading_list.pickle")
        print("\nYour reading list has been deleted.")
    except FileNotFoundError:
        print("You haven't saved any books to a reading list")

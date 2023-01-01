import pickle
from create_book import Book


def save_list(library):
    with open("saved_reading_list.pickle", "wb") as f:
        pickle.dump(library, f, pickle.HIGHEST_PROTOCOL)


def load_list(library):
    try:
        with open("saved_reading_list.pickle", "rb") as f:
            library = pickle.load(f)
            print("your previous reading list has been loaded\n")
            return library
    except NameError:
        print("You haven't saved any books to a reading list")

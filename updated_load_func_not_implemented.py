def load_list(reading_list):
    """
    Load previously saved (pickled) data within the file "saved_reading_list.pickle". Data will be an array as per
    "save_list()". Advise user if this file does not exist.

        Input:
            saved_reading_list.pickle: file (containing saved library in binary)

        Returns:
            library: array
    """
    if len(reading_list) > 0 and :
        merge_list = input("You currently have books in your reading list. Do you want to merge this list with your "
                          "saved list? Otherwise the Loaded list will replace your current list. Enter yes or no ")
    try:
        with open("saved_reading_list.pickle", "rb") as f:
            loaded_list = pickle.load(f)
            print("your previous reading list has been loaded\n")
            return loaded_list
    except FileNotFoundError:
        print("You haven't saved any books to a reading list")

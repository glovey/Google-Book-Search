def print_library(library):
    """ Print the key attributes of Book objects contained in Library arrays provided.

      Parameters:
          library: array (array of Book objects)
    """

    '''Take library array and print attributes of each contained object in the proper format '''
    for count, book in enumerate(library):
        print(f"{count + 1}. {book.title}")
        print(f"Written by: {book.authors_str}")
        print(f"Published by: {book.publisher}\n")

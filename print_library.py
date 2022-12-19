def print_library(library):
  for count, book in enumerate(library):
    print (f"{count+1}. {book.title}")
    print (f"Written by: {book.authors_str}")
    print ( f"Published by: {book.publisher}\n")
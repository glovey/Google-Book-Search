#
import requests  # external library
from create_book import Book
from print_library import print_library


def do_search():
    """ Create Google Books API call using API key and users search request. Present results to user and return
    query results array containing search results Book objects.

        Returns:
            query_results: array (array of books from search, stored as Book objects
    """

    ''' API key to allow access to Google Books API '''
    api_key = "AIzaSyBFVYm6UHh50nFU9FvbUL6qqnKxfcGMpLQ"

    ''' Gather input from user - their search query for Google books '''
    user_input = input("what would you like to search Google Books for?\n")

    ''' Use user input and API key to create the API request and receive response data '''
    api_call = f"https://www.googleapis.com/books/v1/volumes?q={user_input}&key={api_key}"

    response = requests.get(url=api_call)
    response.raise_for_status()
    data = response.json()

    try:
        ''' Create objects of each book, containing key details '''
        query_results = []
        for x in range(min(len(data["items"]), 5)):
            book = Book()

            ''' Use try/except to avoid errors where entries are missing title/author/publisher fields '''
            try:
                book.title = data["items"][x]["volumeInfo"]["title"]
            except KeyError:
                book.title = "None"

            try:
                book.authors = data["items"][x]["volumeInfo"]["authors"]
            except KeyError:
                book.authors = "None"

            try:
                book.publisher = data["items"][x]["volumeInfo"]["publisher"]
            except KeyError:
                book.publisher = "None"

            ''' convert author arrays to strings (allowing for multiple authors)'''
            book.list_authors()
            ''' add '''
            query_results.append(book)

    except KeyError:
        print("Your search returned no results, check you have entered your query correctly.")

    ''' Present user with search results '''
    print("here are your search results\n")
    print_library(query_results)

    ''' Return query results for use in add_to_reading_list func'''
    return query_results

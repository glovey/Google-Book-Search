#Libraries
import requests

#Files
from create_book import Book
from print_library import print_library

#Variables

add_book = None

def do_search():
  #API key to allow acces to Google Books API
  api_key = "AIzaSyBFVYm6UHh50nFU9FvbUL6qqnKxfcGMpLQ"
  
  #Gather input from user - their search query for Google books
  user_input = input("what would you like to search Google Books for?\n")
  
  #Use user input and API key to create the API request and receive response data
  api_call = f"https://www.googleapis.com/books/v1/volumes?q={user_input}&key={api_key}"
  
  response = requests.get(url = api_call)
  response.raise_for_status()
  data = response.json()

  try:
      
    #Create objects of each book, containing key details
    query_results = []
    for x in range(min(len(data["items"]),5)):
      book = Book()
    
      #Use try/except to avoid errors where entries are missing title/author/publisher fields
      try:
        book.title = data["items"][x]["volumeInfo"]["title"]
      except:
        book.title =  "None"
    
      try:
        book.authors = data["items"][x]["volumeInfo"]["authors"]
      except:
        book.authors =  "None"
      
      try:
        book.publisher = data["items"][x]["volumeInfo"]["publisher"]
      except:
        book.publisher =  "None"
      
      book.list_authors()
      
      query_results.append(book)

  except:
    print ("Your search returned no results, check you have entered your query correctly.")
  
  #Present user with search restults
  
   
  print ("here are your search results\n")
  print_library(query_results)

  return query_results

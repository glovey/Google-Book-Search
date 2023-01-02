# Google Book Searcher

### by Joe Filby

## Summary

This programme allows the user to search google books for any word or words they like. The programme makes an API 
call to the Google Books API and returns up to 5 search results, giving key details for each book.

The user can then select books from the search results to add to their reading list and then view that reading list.

The programme also gives the user the option to save their reading list when exiting the programme, and gives the 
option to load a reading list saved in a previous session. 

Unit tests are provided to test functionality and facilitate future development.

## Installation

### Main programme

To run this programme using the command prompt (using Windows):

- Install **Python** on your computer:
  - Check out www.python.org to get started (or https://www.anaconda.com/products/distribution for Anaconda, a great 
   **Python** distribution platform.
  

- Open command prompt on your computer


- Check you have the necessary Requests module by pip installing it:
  - At the command prompt enter:

    `pip install requests`
  

- Within the command prompt, navigate to the file directory where you have save the Google Book Searcher files by entering:

    `<current directory> cd [<directory containing programfile>]`

- And Finally, to run the programme enter:

    `python main.py`


- Enjoy!

### Unit tests

- To run the unit tests you will need to have Pytest installed:
  - At the command prompt enter: 

    `pip install requests`
  

- To run the unit tests enter the following at the command prompt:

  `pytest` or `pytest -Wi` (see **Issues** for further commentary on this)


## How to use the programme

Once the programme is running, follow the on-screen instructions which should guide you through the user journey. 

From the main menu, there are 4 options:

- Search Google Books
- See your reading list
- Load previously save reading list
- Delete previously saved reading
- Save reading list and shut down

And after selecting any of these options, you will be instructed how to proceed through each.

## Unit tests

This version of this programme passes all unit tests. 

Pytest does however raise a Deprecation Warning but this does not impact on functionality.

## Issues

The programme passes all unit tests but a Deprecation warning is raised. While this does not affect functionality 
this should be resolved in future development. 

For now, Pytest reports this warning in addition to the unit tests, as it should, when pytest is called with:

`pytest` 

To remove the warning from the report, run pytest by entering

`pytest -Wi`

into the command prompt instead.

## Future development

- Resolve Issues
- Improve save/load functionality
  - Currently loading a saved reading list will overwrite any reading list created in the current session. A useful 
    function would be to merge current and saved reading lists. 
- Develop search function to allow result filtering by author / publisher etc. 

## Credits

Written by Joe Filby

Inspired by 8L


class Book:
    """  Create Book objects from Google Book Search results, capturing key info. To be stored in query and reading
    list arrays

        Attributes:
            title: int (book title)
            authors: array (book author(s))
            authors_str: str (updated in methods) (authors converted to formatted str)
            publisher: str (book publisher)

        Methods:
            list_authors: take authors and converts to authors_str
    """

    def __init__(self):
        self.title = None
        self.authors = None
        self.authors_str = "None"
        self.publisher = None

    def list_authors(self):
        """ Convert 'authors' array to str of given authors, or 'None' when no authors present.

            Parameters:
                self.authors: array (book author(s))

            Updates:
                self.authors_str: str (authors converted to formatted str)
        """

        ''' State if no author is given, print authors from authors array and format where multiple authors given '''
        if self.authors == "None":
            pass
        elif len(self.authors) == 1:
            self.authors_str = self.authors[0]
        else:
            self.authors_str = self.authors[0]
            for x in range(1, len(self.authors)):
                self.authors_str += f", {self.authors[x]}"

class Book:
  def __init__(self):
    self.title = None
    self.authors = None
    self.authors_str = "None"
    self.publisher = None

  def list_authors(self):
    if len(self.authors) == 1:
      self.authors_str = self.authors[0]
    elif self.authors == "None":
      pass
    else:
      self.authors_str = self.authors[0]
      for x in range(1,len(self.authors)):
        self.authors_str += f", {self.authors[x]}"

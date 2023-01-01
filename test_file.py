from google_search import do_search
from create_book import Book
from add_to_reading_list import add_to_reading_list

'''Test Search function'''


def test_search_returns_results(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Great project")
    query_results = do_search()
    assert len(query_results) > 0


def test_search_returns_book_objects(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Amazing work")
    query_results = do_search()
    for x in query_results:
        assert isinstance(x, Book)


'''Test add to reading list function'''


def test_search_results_added_to_reading_list(monkeypatch):
    query_results = ["test"]
    reading_list = []
    inputs = iter(["yes", "1", "no"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    add_to_reading_list(query_results, reading_list)
    assert query_results[0] == "test"

import os

from google_search import do_search
from create_book import Book
from add_to_reading_list import add_to_reading_list
from manage_saved_list import save_list
from manage_saved_list import load_list

'''Test Search function'''


def test_search_returns_results(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Great project")
    query_results = do_search()
    assert len(query_results) > 0


def test_search_returns_book_objects(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Amazing work")
    query_results = do_search()
    for x in query_results:
        assert isinstance(x, Book)


'''Test add to reading list function'''


def test_search_results_added_to_reading_list(monkeypatch):
    query_results = ["test"]
    reading_list = []
    inputs = iter(["yes", "1", "no"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    add_to_reading_list(query_results, reading_list)
    assert reading_list[0] == "test"


'''Test Save and load functionality'''

test_lib = [1, 2, 3, 4]


def test_save_creates_pickle_file():
    save_list(test_lib)
    assert os.path.exists("saved_reading_list.pickle")
    os.remove("saved_reading_list.pickle")


def test_load_restores_saved_list():
    save_list(test_lib)
    loaded_list = load_list()
    assert loaded_list == test_lib
    os.remove("saved_reading_list.pickle")
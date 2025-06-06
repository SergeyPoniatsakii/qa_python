import pytest

from main import BooksCollector

@pytest.fixture
def books_collector():
    return BooksCollector()

@pytest.fixture
def books_dict_without_genres():
    collector = BooksCollector()
    collector.add_new_book("Книга1")
    collector.add_new_book("Книга2")
    collector.add_new_book("Книга3")
    collector.add_new_book("Книга4")
    return collector
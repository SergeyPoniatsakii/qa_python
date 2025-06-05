import pytest

from main import BooksCollector

@pytest.fixture
def books_collector():
    return BooksCollector()

@pytest.fixture
def books_without_genres():
    collector = BooksCollector()
    collector.add_new_book("Книга1")
    # collector.add_new_book("Книга2")
    # collector.add_new_book("Книга3")
    return collector

@pytest.fixture
def initialized_books_collector():
    collector = BooksCollector()
    collector.add_new_book("Книга1")
    collector.set_book_genre("Книга1", "Фантастика")
    collector.add_new_book("Книга2")
    collector.set_book_genre("Книга2", "Ужасы")
    collector.add_new_book("Книга3")
    collector.set_book_genre("Книга3", "Детективы")
    collector.add_new_book("Книга4")
    collector.set_book_genre("Книга4", "Детективы")
    return collector

@pytest.fixture
def books_in_favorites():
    collector = BooksCollector()
    collector.add_new_book("Книга1")
    collector.add_new_book("Книга2")
    collector.add_new_book("Книга3")
    collector.add_book_in_favorites("Книга1")
    collector.add_book_in_favorites("Книга3")
    return collector
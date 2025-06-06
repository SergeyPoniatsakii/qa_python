
class TestBooksCollector:
    import pytest

    def test_add_new_book_with_empty_name_no_add(self, books_collector):
        books_collector.add_new_book("")
        assert not books_collector.books_genre

    @pytest.mark.parametrize("book_name, expected_result", [
        ("a", True),
        ("a" * 40, True),
        ("a" * 41, False),
        ("", False),
        ("a" * 39, True)
    ])
    def test_add_new_book_with_name_in_border_lengths(self, books_collector, book_name, expected_result):
        books_collector.add_new_book(book_name)
        assert (book_name in books_collector.books_genre) == expected_result

    def test_set_book_genre_existing_genre_add(self, books_dict_without_genres):
        books_dict_without_genres.set_book_genre("Книга1", "Фантастика")
        assert books_dict_without_genres.books_genre["Книга1"] == "Фантастика"

    def test_set_book_genre_non_existing_genre_not_add(self, books_dict_without_genres):
        books_dict_without_genres.set_book_genre("Книга1", "Фэнтези")
        assert books_dict_without_genres.books_genre["Книга1"] == ""

    def test_get_book_genre_existing_book_genre_got(self, books_dict_without_genres):
        books_dict_without_genres.set_book_genre("Книга1", "Фантастика")
        assert books_dict_without_genres.books_genre["Книга1"] == "Фантастика"

    def test_get_genre_of_non_existing_book_genre_none(self, books_collector):
        assert books_collector.get_book_genre("Неизвестная книга") is None

    def test_get_books_with_specific_genre_existing_genre_book_got(self, books_dict_without_genres):
        books_dict_without_genres.set_book_genre("Книга3", "Фантастика")
        books_dict_without_genres.set_book_genre("Книга4", "Фантастика")
        assert books_dict_without_genres.get_books_with_specific_genre("Фантастика") == ["Книга3", "Книга4"]

    def test_get_books_with_specific_genre_non_existing_genre_book_none(self, books_dict_without_genres):
        books_dict_without_genres.set_book_genre("Книга1", "Фэнтези")
        assert books_dict_without_genres.get_books_with_specific_genre("Фэнтези") == []

    def test_get_books_genre_with_different_genres_dictionary_got(self, books_dict_without_genres):
        books_dict_without_genres.set_book_genre("Книга1", "Фантастика")
        books_dict_without_genres.set_book_genre("Книга2", "Ужасы")
        books_dict_without_genres.set_book_genre("Книга3", "Детективы")
        books_dict_without_genres.set_book_genre("Книга4", "Детективы")
        assert books_dict_without_genres.get_books_genre() == {"Книга1": "Фантастика", "Книга2": "Ужасы",
                                                                 "Книга3": "Детективы", "Книга4": "Детективы"}

    def test_get_books_genre_with_empty_genres_dictionary_empty(self, books_collector):
        books_collector.add_new_book("Книга1")
        assert books_collector.get_books_genre() == {"Книга1": ""}

    def test_get_books_for_children_mixed_genre_books_got_no_rate(self, books_dict_without_genres):
        books_dict_without_genres.set_book_genre("Книга1", "Фантастика")
        assert books_dict_without_genres.get_books_for_children() == ["Книга1"]

    def test_add_book_in_favorites_existing_book_add(self, books_dict_without_genres):
        books_dict_without_genres.add_book_in_favorites("Книга3")
        assert "Книга3" in books_dict_without_genres.favorites

    def test_add_book_in_favorites_duplicate_book_not_add(self, books_dict_without_genres):
        books_dict_without_genres.add_book_in_favorites("Книга1")
        books_dict_without_genres.add_book_in_favorites("Книга1")
        assert books_dict_without_genres.favorites.count("Книга1") == 1

    def test_delete_book_from_favorites_existing_book_del(self, books_dict_without_genres):
        books_dict_without_genres.add_book_in_favorites("Книга1")
        books_dict_without_genres.delete_book_from_favorites("Книга1")
        assert "Книга1" not in books_dict_without_genres.favorites

    def test_get_list_of_favorites_books_with_multiple_books_list_got(self, books_dict_without_genres):
        books_dict_without_genres.add_book_in_favorites("Книга1")
        books_dict_without_genres.add_book_in_favorites("Книга3")
        assert books_dict_without_genres.get_list_of_favorites_books() == ["Книга1", "Книга3"]

    def test_get_list_of_favorites_books_with_duplicates_no_duplicates_in_list(self, books_dict_without_genres):
        books_dict_without_genres.add_book_in_favorites("Книга1")
        books_dict_without_genres.add_book_in_favorites("Книга1")
        books_dict_without_genres.add_book_in_favorites("Книга3")
        assert books_dict_without_genres.get_list_of_favorites_books() == ["Книга1", "Книга3"]
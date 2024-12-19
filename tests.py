from main import BooksCollector
import pytest


class TestBookCollector:

    @pytest.fixture(autouse=True)
    def setup_collector(self):
        self.collector = BooksCollector()

    @pytest.mark.parametrize('book_name', [
        'A',  # минимально допустимая длина
        'A' * 40,  # максимально допустимая длина
        'Brave New World',  # пробелы в названии книги
        '1984'  # цифры в названии книги
    ])
    def test_add_new_book_valid_name_and_empty_values(self, book_name):
        self.collector.add_new_book(book_name)
        assert book_name in self.collector.get_books_genre()
        assert self.collector.get_book_genre(book_name) == ''

    @pytest.mark.parametrize('book_name', [
        '',  # пустое название
        'A' * 41  # слишком длинное название
    ])
    def test_add_new_book_invalid_length(self, book_name):
        self.collector.add_new_book(book_name)
        assert book_name not in self.collector.get_books_genre()

    def test_add_new_book_duplicate_name_book_not_added(self):
        book_name = 'Invincible'
        self.collector.add_new_book(book_name)
        self.collector.add_new_book(book_name)
        assert len(self.collector.get_books_genre()) == 1

    @pytest.mark.parametrize('book_name, genre', [
        ['Invincible', 'Фантастика'],
        ['Pet Sematary', 'Ужасы'],
        ['Murder on the Orient Express', 'Детективы'],
        ['Shrek', 'Мультфильмы'],
        ['The Twelve Chairs', 'Комедии']
    ])
    def test_set_book_genre_valid_book_and_genre(self, book_name, genre):
        self.collector.add_new_book(book_name)
        self.collector.set_book_genre(book_name, genre)
        assert self.collector.get_book_genre(book_name) == genre

    def test_set_book_genre_invalid_genre(self):
        new_book = 'The Lord of the Rings'
        self.collector.add_new_book(new_book)
        self.collector.set_book_genre(new_book, 'Фэнтези')
        assert self.collector.get_book_genre(new_book) == ''

    def test_set_book_genre_invalid_book(self):
        non_existent_book = "Несуществующая книга"
        genre = "Фантастика"
        original_state = self.collector.get_books_genre().copy()
        self.collector.set_book_genre(non_existent_book, genre)
        assert self.collector.get_books_genre() == original_state

    def test_get_book_genre_when_book_has_genre(self):
        book_name = 'Invincible'
        genre = 'Фантастика'
        self.collector.add_new_book(book_name)
        self.collector.set_book_genre(book_name, genre)
        assert self.collector.get_book_genre(book_name) == genre

    def test_get_book_genre_when_book_without_genre(self):
        book_name = 'The Lord of the Rings'
        self.collector.add_new_book(book_name)
        assert self.collector.get_book_genre(book_name) == ''

    def test_get_books_with_specific_genre(self):
        self.collector.add_new_book('Pet Sematary')
        self.collector.add_new_book('Invincible')
        self.collector.set_book_genre('Pet Sematary', 'Ужасы')
        self.collector.set_book_genre('Invincible', 'Фантастика')
        books = self.collector.get_books_with_specific_genre('Ужасы')
        assert books == ['Pet Sematary']

    @pytest.mark.parametrize('initial_books_genre, expected_genre_dict', [
        [
            {"Invincible": "Фантастика", "Pet Sematary": "Ужасы"},
            {"Invincible": "Фантастика", "Pet Sematary": "Ужасы"}
        ]
    ])
    def test_get_books_genre(self, initial_books_genre, expected_genre_dict):
        self.collector.books_genre = initial_books_genre
        assert self.collector.get_books_genre() == expected_genre_dict

    def test_get_books_for_children(self):
        self.collector.add_new_book('Pet Sematary')
        self.collector.add_new_book('Invincible')
        self.collector.set_book_genre('Pet Sematary', 'Ужасы')
        self.collector.set_book_genre('Invincible', 'Фантастика')
        books_for_children = self.collector.get_books_for_children()
        assert books_for_children == ["Invincible"]

    @pytest.mark.parametrize("book_name", ["Pet Sematary", "Invincible"])
    def test_add_book_in_favorites(self, book_name):
        self.collector.add_new_book(book_name)
        self.collector.add_book_in_favorites(book_name)
        assert book_name in self.collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_exist(self):
        non_existent_book = "Несуществующая книга"
        original_favorites = self.collector.get_list_of_favorites_books().copy()
        self.collector.add_book_in_favorites(non_existent_book)
        assert self.collector.get_list_of_favorites_books() == original_favorites

    def test_delete_book_from_favorites(self):
        self.collector.add_new_book("Invincible")
        self.collector.add_book_in_favorites("Invincible")
        self.collector.delete_book_from_favorites("Invincible")
        assert "Invincible" not in self.collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        self.collector.add_new_book("Invincible")
        self.collector.add_new_book("Pet Sematary")
        self.collector.add_book_in_favorites("Invincible")
        self.collector.add_book_in_favorites("Pet Sematary")
        assert set(self.collector.get_list_of_favorites_books()) == {"Invincible", "Pet Sematary"}

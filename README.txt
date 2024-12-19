1. setup_collector: создаёт новый экземпляр BooksCollector перед каждым тестом.
2. test_add_new_book_valid_name_and_empty_values: проверяет добавление новой книги с валидным названием и пустым значением
3. test_add_new_book_invalid_length: проверяет, что книги не добавляются, если имя пустое или превышает 40 символов.
4. test_add_new_book_duplicate_name_book_not_added: проверяет, что дубликат книги не добавляется в словарь
5. test_set_book_genre_valid_book_and_genre: проверяет корректную установку жанра книги.
6. test_set_book_genre_invalid_genre - проверяет, что нельзя установить несуществующий жанр.
7. test_set_book_genre_invalid_book: проверяет, что нельзя установить жанр несуществующим книгам.
8. test_get_book_genre_when_book_has_genre -  проверяет, что правильно возвращается жанр для указанной книги.
9. test_get_book_genre_when_book_without_genre - проверяет, что возвращает пустой жанр для книги без жанра
10. test_get_books_with_specific_genre - проверяет, что возвращается список книг с определенным жанром
11. test_get_books_genre: проверяет возврат всего словаря книг.
12. test_get_books_for_children: проверяет, что возвращаются только доступные детям книги.
13. test_add_book_in_favorites: проверяет добавление книги в избранное.
14. test_add_book_in_favorites_not_exist: проверяет, что нельзя добавить несуществующую книгу в избранное.
15. test_delete_book_from_favorites: проверяет возможность удаления книги из избранного.
16. test_get_list_of_favorites_books: проверяет, что возвращается список избранных книг
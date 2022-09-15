from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_add_two_same_books_without_error(self):
        collector = BooksCollector()

        same_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(same_name)
        collector.add_new_book(same_name)

        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating(self):
        name = 'Гордость и предубеждение и зомби'
        rating = 5

        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_rating(name, rating)

        assert collector.get_book_rating(name) == rating

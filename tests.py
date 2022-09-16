class TestBooksCollector:
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_add_two_same_books_without_error(self, collector):
        same_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(same_name)
        collector.add_new_book(same_name)

        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating(self, collector):
        name = 'Гордость и предубеждение и зомби'
        rating = 5

        collector.add_new_book(name)
        collector.set_book_rating(name, rating)

        assert collector.get_book_rating(name) == rating

    def test_set_book_rating_nonexistent_book_return_none(self, collector):
        name = 'Гордость и предубеждение и зомби'
        rating = 5

        collector.set_book_rating(name, rating)

        assert collector.get_book_rating(name) is None

    def test_set_book_rating_wrong_rating_return_one(self, collector):
        name = 'Гордость и предубеждение и зомби'
        rating = 55

        collector.add_new_book(name)
        collector.set_book_rating(name, rating)

        assert collector.get_book_rating(name) == 1

    def test_get_book_rating(self, collector):
        """
        this method is tested in other tests (f.e. test_set_book_rating), but I have to follow the rules of the task
        """
        name = 'Гордость и предубеждение и зомби'
        rating = 5

        collector.add_new_book(name)
        collector.set_book_rating(name, rating)

        assert collector.get_book_rating(name) == rating

import unittest
from unittest.mock import Mock
from library import library
import json
from library.patron import Patron

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.lib = library.Library()
        # self.books_data = [{'title': 'Learning Python', 'ebook_count': 3, 'author': jones}, {'title': 'Learning Python (Learning)', 'ebook_count': 1}, {'title': 'Learning Python', 'ebook_count': 1}, {'title': 'Learn to Program Using Python', 'ebook_count': 1}, {'title': 'Aprendendo Python', 'ebook_count': 1}, {'title': 'Python Basics', 'ebook_count': 1}]
        with open('tests_data/ebooks.txt', 'r') as f:
            self.books_data = json.loads(f.read())
        with open('tests_data/json_Sayan_Mukhopadhyay.txt', 'r') as f:
            self.Mukhopadhyay_data = json.loads(f.read())

    def test_is_ebook_true(self):
        self.lib.api.get_ebooks = Mock(return_value=self.books_data)
        self.assertTrue(self.lib.is_ebook('Learn to Program Using Python'))

    def test_is_ebook_false(self):
        self.lib.api.get_ebooks = Mock(return_value=self.books_data)
        self.assertFalse(self.lib.is_ebook('Learn to Prodram Using Python'))

    def test_get_ebooks_count(self):
        self.lib.api.get_ebooks = Mock(return_value=self.books_data)
        self.assertEqual(self.lib.get_ebooks_count("learning python"), 8)

    def test_is_book_by_author(self):
        self.lib.api.books_by_author = Mock(return_value=["Advanced Data Analytics Using Python: With Machine Learning, Deep Learning and NLP Examples"])
        self.assertEqual(self.lib.is_book_by_author("Sayan Mukhopadhyay","Advanced Data Analytics Using Python: With Machine Learning, Deep Learning and NLP Examples"), True)

    def test_is_book_by_author_false(self):
        self.lib.api.books_by_author = Mock(return_value=["Advanced Data Analytics Using Python: With Machine Learning, Deep Learning and NLP Examples"])
        self.assertEqual(self.lib.is_book_by_author("Sayan Mukhopadhyay","Learning Python"), False)

    def test_get_languages_for_book(self):
        self.lib.api.get_book_info = Mock(return_value=[{'title': 'Advanced Data Analytics Using Python: With Machine Learning, Deep Learning and NLP Examples', 'publisher': ['Apress'], 'publish_year': [2018], 'language': 'English'}])
        self.assertEqual(self.lib.get_languages_for_book("Advanced Data Analytics Using Python: With Machine Learning, Deep Learning and NLP Examples"),{'E', 'l', 'h', 'n', 'g', 's', 'i'})

    # def test_register_patron(self):
    #     patron = Patron("Bob", "Jones", 30, 1)
    #     def check(patron):
    #         if patron is not None:
    #             return 1
    #         else:
    #             None
    #     self.lib.db.insert_patron = Mock(side_effect=check)
    #     self.assertEqual(self.lib.register_patron("Bob", "Jones", 30, 1), 1)

    def test_register_patron_false(self):
        self.patron = Mock(return_value=None)
        false_patron = self.lib.register_patron("fname","lname",0,0)
        self.assertEqual(false_patron, None)

    def test_is_patron_registered_true(self):
            patron_mock = Mock()
            self.lib.db.retrieve_patron = Mock(return_value=1)
            self.assertTrue(self.lib.is_patron_registered(patron_mock))

    def test_is_patron_registered_false(self):
        patron_mock = Mock()
        self.lib.db.retrieve_patron = Mock(return_value=None)
        self.assertFalse(self.lib.is_patron_registered(patron_mock))

    def test_borrow_book(self):
        book_mock = Mock()
        patron_mock = Mock()
        method_mock = Mock()
        self.lib.db.update_patron = method_mock
        self.lib.borrow_book(book_mock,patron_mock)
        method_mock.assert_called()

    def test_return_book(self):
        book_mock = Mock()
        patron_mock = Mock()
        method_mock = Mock()
        self.lib.db.update_patron = method_mock
        self.lib.return_borrowed_book(book_mock,patron_mock)
        method_mock.assert_called()

    # def test_is_book_borrowed(self):
    #     book_mock = Mock()
    #     patron_mock = Mock()
    #     self.lib.is_book_borrowed(book_mock, patron_mock)

import unittest
from unittest import mock
from library import patron


class TestPatron(unittest.TestCase):
    def setUp(self):
        self.pat = patron.Patron('fname', 'lname', '20', '1234')

    def test_valid_name(self):
        pat = patron.Patron('fname', 'lname', '20', '1234')
        self.assertTrue(isinstance(pat, patron.Patron))

    def test_invalid_name(self):
        self.assertRaises(patron.InvalidNameException, patron.Patron, '1fname', '1lname', '20', '1234')

    def test_add_borrowed_book(self):
        self.pat.add_borrowed_book('Book1')
        self.assertEqual(self.pat.get_borrowed_books(), ['book1'])
    
    def test_add_existing_borrowed_book(self):
        self.pat.add_borrowed_book('Book1')
        self.pat.add_borrowed_book('Book1')
        self.assertEqual(self.pat.get_borrowed_books(), ['book1'])

    def test_get_borrowed_books(self):
        with mock.patch.object(self.pat, 'get_borrowed_books', return_value=['book1', 'book2']):
            self.assertEqual(self.pat.get_borrowed_books(), ['book1', 'book2'])

    def test_return_borrowed_book(self):
        self.pat.add_borrowed_book('Book1')
        self.pat.return_borrowed_book('Book1')
        self.assertEqual(self.pat.get_borrowed_books(), [])

    def test_get_fname(self):
        self.assertEqual(self.pat.get_fname(), 'fname')

    def test_get_lname(self):
        self.assertEqual(self.pat.get_lname(), 'lname')

    def test_get_age(self):
        self.assertEqual(self.pat.get_age(), '20')

    def test_get_memberID(self):
        self.assertEqual(self.pat.get_memberID(), '1234')

    def test_eq(self):
        pat1 = patron.Patron('fname', 'lname', '20', '1234')
        pat2 = patron.Patron('fname', 'lname', '20', '1234')
        pat3 = patron.Patron('fname', 'lname', '21', '1234')
        self.assertTrue(pat1 == pat2)
        self.assertFalse(pat1 == pat3)

    def test_ne(self):
        pat1 = patron.Patron('fname', 'lname', '20', '1234')
        pat2 = patron.Patron('fname', 'lname', '20', '1234')
        pat3 = patron.Patron('fname', 'lname', '21', '1234')
        self.assertFalse(pat1 != pat2)
        self.assertTrue(pat1 != pat3)

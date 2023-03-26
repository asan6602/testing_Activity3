import os
import unittest
from unittest.mock import Mock, call
from library import library_db_interface
from library.patron import Patron

class TestLibbraryDBInterface(unittest.TestCase):

    def setUp(self):
        self.db_interface = library_db_interface.Library_DB()

    def test_insert_patron_not_in_db(self):
        patron_mock = Mock()
        self.db_interface.retrieve_patron = Mock(return_value=None)
        data = {'fname': 'name', 'lname': 'name', 'age': 'age', 'memberID': 'memberID',
                'borrowed_books': []}
        self.db_interface.convert_patron_to_db_format = Mock(return_value=data)
        self.assertGreater(self.db_interface.insert_patron(patron_mock), 1)
        
    def test_insert_not_patron(self):
        false_partion = None #No mock because I want false patron
        return_value = self.db_interface.insert_patron(false_partion);
        self.assertIsNone(return_value);
        
    def test_insert_parton_in_db(self):
        patron_mock = Mock()
        self.db_interface.retrieve_patron = Mock(return_value=None)
        data = {'fname': 'name', 'lname': 'name', 'age': 'age', 'memberID': 'memberID',
                'borrowed_books': []}
        self.db_interface.convert_patron_to_db_format = Mock(return_value=data)
        self.db_interface.retrieve_patron = Mock(return_value=1)
        self.db_interface.insert_patron(patron_mock) 
        self.assertIsNone(self.db_interface.insert_patron(patron_mock))
        
    def test_patron_count(self): 
        patron_mock = Mock()
        self.db_interface.retrieve_patron = Mock(return_value=None)
        data = {'fname': 'name', 'lname': 'name', 'age': 'age', 'memberID': 'memberID',
                'borrowed_books': []}
        self.db_interface.convert_patron_to_db_format = Mock(return_value=data)
        self.db_interface.insert_patron(patron_mock)
        self.assertGreater(self.db_interface.get_patron_count(), 1)
        
    def test_get_all_patrons(self):
        patron_mock = Mock()
        self.db_interface.retrieve_patron = Mock(return_value=None)
        data = {'fname': 'name', 'lname': 'name', 'age': 'age', 'memberID': 'memberID',
                'borrowed_books': []}
        self.db_interface.convert_patron_to_db_format = Mock(return_value=data)
        self.db_interface.insert_patron(patron_mock)
        self.assertGreater(len(self.db_interface.get_all_patrons()),1) 
        
    def test_retrieve_patron_bad_id(self):
        self.assertIsNone(self.db_interface.retrieve_patron(None))

    def test_update_patron(self):
        data = {'fname': 'name', 'lname': 'name', 'age': 'age', 'memberID': 'memberID',
                'borrowed_books': []}
        def check(data):
            if data is not None:
                return data
            else:
                None
        self.db_interface.convert_patron_to_db_format = Mock(return_value=check(data))
        db_update_mock = Mock(return_value=check(data))
        self.db_interface.db.update = db_update_mock
        self.db_interface.update_patron(Mock())
        db_update_mock.assert_called()
        
    def test_bad_update_patron(self):
        bad_patron = None
        self.assertIsNone(self.db_interface.update_patron(bad_patron))

    def test_convert_patron_to_db_format(self):
        patron_mock = Mock()

        patron_mock.get_fname = Mock(return_value=1)
        patron_mock.get_lname = Mock(return_value=2)
        patron_mock.get_age = Mock(return_value=3)
        patron_mock.get_memberID = Mock(return_value=4)
        patron_mock.get_borrowed_books = Mock(return_value=5)
        self.assertEqual(self.db_interface.convert_patron_to_db_format(patron_mock),
                         {'fname': 1, 'lname': 2, 'age': 3, 'memberID': 4,
                          'borrowed_books': 5})

    def test_close_db(self):
        db_close_mock = Mock()
        self.db_interface.db.close = db_close_mock
        self.db_interface.close_db()
        db_close_mock.assert_called()

#remove file each runthrough 
    # def tearDown(self) -> None:
    #     os.remove("db.json")
    #     return super().tearDown()
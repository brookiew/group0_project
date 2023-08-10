import unittest
from core.utils import dict_factory, calculate_cost, calculate_total_cost, generate_unique_id
from session import UserSession, Sessions
from database.db import Database

class TestUserSession(unittest.TestCase):

    def setUp(self):
        # Set up a mock database for testing
        self.mock_db = type('MockDatabase', (), {'get_full_inventory': lambda: [
            {'id': 'item1', 'item_name': 'Item 1', 'price': 100},
            {'id': 'item2', 'item_name': 'Item 2', 'price': 50},
        ]})()

    def test_empty_cart(self):
        user_session = UserSession('test_user', self.mock_db)
        result = user_session.empty_cart()
        expected_result = {
            'item1': {'name': 'Item 1', 'price': 100, 'quantity': 0, 'discount': 0, 'tax_rate': 0},
            'item2': {'name': 'Item 2', 'price': 50, 'quantity': 0, 'discount': 0, 'tax_rate': 0},
        }
        self.assertEqual(result, expected_result)

    # Add more test cases for the UserSession class methods

class TestSessions(unittest.TestCase):

    def setUp(self):
        # Set up a mock database for testing
        self.mock_db = type('MockDatabase', (), {})()

    def test_add_and_get_session(self):
        sessions = Sessions()
        sessions.add_new_session('test_user', self.mock_db)
        result = sessions.get_session('test_user')
        self.assertIsInstance(result, UserSession)
        self.assertEqual(result.username, 'test_user')

    # Add more test cases for the Sessions class methods

if __name__ == '__main__':
    unittest.main()

class TestUtils(unittest.TestCase):

    def test_dict_factory(self):
        # Mock cursor description
        cursor_description = [('id', None, None, None, None, None, None)]
        mock_cursor = type('MockCursor', (), {'description': cursor_description})
        row = (1,)
        
        # Call the function
        result = dict_factory(mock_cursor, row)
        
        # Check the result
        expected_result = {'id': 1}
        self.assertEqual(result, expected_result)

    def test_calculate_cost(self):
        # Test with default discount and tax rate
        result = calculate_cost(100, 5)
        self.assertEqual(result, 525.0)

        # Test with custom discount and tax rate
        result = calculate_cost(100, 5, discount=0.1, tax_rate=0.08)
        self.assertEqual(result, 472.5)

    def test_calculate_total_cost(self):
        items = {
            'item1': {'price': 100, 'quantity': 2, 'discount': 0.1, 'tax_rate': 0.05},
            'item2': {'price': 50, 'quantity': 3, 'discount': 0.0, 'tax_rate': 0.1}
        }

        result = calculate_total_cost(items)
        self.assertEqual(result, 274.5)

    def test_generate_unique_id(self):
        result1 = generate_unique_id()
        result2 = generate_unique_id()
        self.assertNotEqual(result1, result2)

if __name__ == '__main__':
    unittest.main()

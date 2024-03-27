import unittest

from classes import Client
from utils import CLIENT_NAME_VALIDATION_MSG


class TestClient(unittest.TestCase):
    """
    The TestClient class represents a set of unit tests for the Client class.

    Methods:
        setUp: Sets up the test environment for each test method.
        test_init: Tests the initialization of the Client class.
        test_init_with_short_name: Tests the initialization of the Client class with a short name.
    """

    def setUp(self):
        """
        The method to set up the test environment for each test method.
        """
        # Initialize a client with a name
        self.client = Client("John Doe")

    def test_init(self):
        """
        The method to test the initialization of the Client class.
        """
        # Assert that the client's name is as expected
        self.assertEqual(self.client.name, "John Doe")

    def test_init_with_short_name(self):
        """
        The method to test the initialization of the Client class with a short name.
        """
        # Assert that initializing a client with a short name raises a ValueError
        with self.assertRaises(ValueError) as context:
            Client("Jo")
        self.assertTrue(CLIENT_NAME_VALIDATION_MSG in str(context.exception))


if __name__ == "__main__":
    unittest.main()

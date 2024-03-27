import unittest
from datetime import datetime

from classes import Client, Package
from utils import PACKAGE_ORIGIN_VALIDATION_MSG, PACKAGE_DESTINATION_VALIDATION_MSG, \
    PACKAGE_ORIGIN_DESTINATION_SAME_VALIDATION_MSG, PACKAGE_CLIENT_VALIDATION_MSG


class TestPackage(unittest.TestCase):
    """
    The TestPackage class represents a set of unit tests for the Package class.

    Methods:
        setUp: Sets up the test environment for each test method.
        test_init: Tests the initialization of the Package class.
        test_init_with_short_origin: Tests the initialization of the Package class with a short origin.
        test_init_with_short_destination: Tests the initialization of the Package class with a short destination.
        test_init_with_same_origin_and_destination: Tests the initialization of the Package class with the same origin and destination.
        test_init_with_invalid_client: Tests the initialization of the Package class with an invalid client.
    """

    def setUp(self):
        """
        The method to set up the test environment for each test method.
        """
        # Initialize a client and a package with the client as the owner
        self.client = Client("John Doe")
        self.package = Package("New York", "Los Angeles", self.client, datetime.now().strftime("%d/%m/%Y"))

    def test_init(self):
        """
        The method to test the initialization of the Package class.
        """
        # Assert that the package's origin, destination, and client are as expected
        self.assertEqual(self.package.origin, "New York")
        self.assertEqual(self.package.destination, "Los Angeles")
        self.assertEqual(self.package.client, self.client)

    def test_init_with_short_origin(self):
        """
        The method to test the initialization of the Package class with a short origin.
        """
        # Assert that initializing a package with a short origin raises a ValueError
        with self.assertRaises(ValueError) as context:
            Package("NY", "Los Angeles", self.client, datetime.now().strftime("%d/%m/%Y"))
        self.assertTrue(PACKAGE_ORIGIN_VALIDATION_MSG in str(context.exception))

    def test_init_with_short_destination(self):
        """
        The method to test the initialization of the Package class with a short destination.
        """
        # Assert that initializing a package with a short destination raises a ValueError
        with self.assertRaises(ValueError) as context:
            Package("New York", "LA", self.client, datetime.now().strftime("%d/%m/%Y"))
        self.assertTrue(PACKAGE_DESTINATION_VALIDATION_MSG in str(context.exception))

    def test_init_with_same_origin_and_destination(self):
        """
        The method to test the initialization of the Package class with the same origin and destination.
        """
        # Assert that initializing a package with the same origin and destination raises a ValueError
        with self.assertRaises(ValueError) as context:
            Package("New York", "New York", self.client, datetime.now().strftime("%d/%m/%Y"))
        self.assertTrue(PACKAGE_ORIGIN_DESTINATION_SAME_VALIDATION_MSG in str(context.exception))

    def test_init_with_invalid_client(self):
        """
        The method to test the initialization of the Package class with an invalid client.
        """
        # Assert that initializing a package with an invalid client raises a ValueError
        with self.assertRaises(ValueError) as context:
            Package("New York", "Los Angeles", "John Doe", datetime.now().strftime("%d/%m/%Y"))
        self.assertTrue(PACKAGE_CLIENT_VALIDATION_MSG in str(context.exception))


if __name__ == "__main__":
    unittest.main()

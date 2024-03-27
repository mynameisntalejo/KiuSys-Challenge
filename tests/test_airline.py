import json
import unittest
from datetime import datetime

from classes import Airline
from utils import AIRLINE_NAME_VALIDATION_MSG, DATE_FORMAT, PACKAGE_CLIENT_VALIDATION_MSG


class TestAirline(unittest.TestCase):
    """
    The TestAirline class represents a set of unit tests for the Airline class.

    Methods:
        setUp: Sets up the test environment for each test method.
        test_init: Tests the initialization of the Airline class.
        test_init_with_short_name: Tests the initialization of the Airline class with a short name.
        test_add_client: Tests the addition of a client to the Airline class.
        test_add_package: Tests the addition of a package to the Airline class.
        test_add_get_transportation_fee: Tests the addition and retrieval of a transportation fee in the Airline class.
        test_get_total_transportation_report: Tests the retrieval of the total transportation report in the Airline class.
        test_add_package_with_invalid_client: Tests the addition of a package with an invalid client to the Airline class.
    """

    def setUp(self):
        """
        The method to set up the test environment for each test method.
        """
        # Initialize an airline and add packages from a fixtures file
        self.airline = Airline("Airline Name")

        with open("tests/fixtures/packages.json", "r") as f:
            packages_data = json.load(f)[0]["tests_packages"]

        for package_data in packages_data:
            client = self.airline.add_client(package_data["client_str"])
            self.airline.add_package(package_data["origin"], package_data["destination"], client,
                                     datetime.now().strftime(DATE_FORMAT))

    def test_init(self):
        """
        The method to test the initialization of the Airline class.
        """
        # Assert that the airline's name and the lengths of its packages and clients lists are as expected
        self.assertEqual(self.airline.name, "Airline Name")
        self.assertEqual(len(self.airline.packages), 3)
        self.assertEqual(len(self.airline.clients), 3)

    def test_init_with_short_name(self):
        """
        The method to test the initialization of the Airline class with a short name.
        """
        # Assert that initializing an airline with a short name raises a ValueError
        with self.assertRaises(ValueError) as context:
            Airline("AN")
        self.assertTrue(AIRLINE_NAME_VALIDATION_MSG in str(context.exception))

    def test_add_client(self):
        """
        The method to test the addition of a client to the Airline class.
        """
        # Add a client and assert that the client's name is as expected and that the client is in the airline's clients list
        client_name = "New Client"
        client = self.airline.add_client(client_name)
        self.assertEqual(client.name, client_name)
        self.assertIn(client, self.airline.clients)

    def test_add_package(self):
        """
        The method to test the addition of a package to the Airline class.
        """
        # Add a package and assert that the package's details are as expected and that the package is in the airline's packages list
        origin = "Origin"
        destination = "Destination"
        client = self.airline.clients[0]
        package = self.airline.add_package(origin, destination, client, datetime.now().strftime(DATE_FORMAT))
        self.assertEqual(package.origin, origin)
        self.assertEqual(package.destination, destination)
        self.assertEqual(package.client, client)
        self.assertIn(package, self.airline.packages)

    def test_add_get_transportation_fee(self):
        """
        The method to test the addition and retrieval of a transportation fee in the Airline class.
        """
        # Add a transportation fee and assert that the retrieved fee is as expected
        date = "31/12/2023"
        fee = 20
        self.airline.add_transportation_fee(date, fee)
        returned_fee = self.airline.get_transportation_fee(date)
        self.assertEqual(returned_fee, fee)

    def test_get_total_transportation_report(self):
        """
        The method to test the retrieval of the total transportation report in the Airline class.
        """
        # Get the total transportation report and assert that the report is as expected
        date = "31/12/2023"
        report = self.airline.get_total_transportation_report(date)
        expected_report = f"[DATE: {date} | FEE: 10]\nTotal packages transported: 0\nTotal transportation fee charged: 0"
        self.assertEqual(report, expected_report)
        default_date = datetime.now().strftime("%d/%m/%Y")
        self.airline.add_transportation_fee(default_date, 20)
        report = self.airline.get_total_transportation_report(default_date)
        expected_report = f"[DATE: {default_date} | FEE: 20]\nTotal packages transported: 3\nTotal transportation fee charged: 60"
        self.assertEqual(report, expected_report)

    def test_add_package_with_invalid_client(self):
        """
        The method to test the addition of a package with an invalid client to the Airline class.
        """
        # Assert that adding a package with an invalid client raises a ValueError
        with self.assertRaises(ValueError) as context:
            self.airline.add_package("Origin", "Destination", "Invalid Client", datetime.now().strftime(DATE_FORMAT))
        self.assertTrue(PACKAGE_CLIENT_VALIDATION_MSG in str(context.exception))


if __name__ == "__main__":
    unittest.main()

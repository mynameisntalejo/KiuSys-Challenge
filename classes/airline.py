from classes.client import Client
from classes.package import Package
from utils import date_min_validation, date_format_validation, date_range_validation, DATE_MIN, \
    AIRLINE_NAME_VALIDATION_MSG, int_fee_validation, CLIENT_NOT_EXIST_VALIDATION_MSG


class Airline:
    """
    The Airline class represents an airline with its name, clients, packages, and transportation fees.

    Attributes:
        name (str): The name of the airline.
        clients (list): A list of clients of the airline.
        packages (list): A list of packages handled by the airline.
        transportation_fee (dict): A dictionary mapping dates to transportation fees.
    """

    def __init__(self, name):
        """
        The constructor for the Airline class.

        Parameters:
            name (str): The name of the airline.
        """
        # Validate that the airline name is at least 3 characters long
        if len(name) < 3:
            raise ValueError(AIRLINE_NAME_VALIDATION_MSG)
        self.name = name
        # Initialize empty lists for the clients and packages
        self.clients = []
        self.packages = []
        # Initialize the transportation fee dictionary with a default fee
        self.transportation_fee = {
            DATE_MIN: 10,
        }

    def __str__(self):
        """
        The method to get the string representation of the airline.

        Returns:
            str: The string representation of the airline.
        """
        # Return the name of the airline
        return f"{self.name}"

    def __repr__(self):
        """
        The method to get the string representation of the airline for debugging.

        Returns:
            str: The string representation of the airline for debugging.
        """
        # Return the name of the airline
        return f"{self.name}"

    def get_client(self, name):
        """
        The method to get a client by name.

        Parameters:
            name (str): The name of the client.

        Returns:
            Client: The client with the given name.

        Raises:
            ValueError: If no client with the given name exists.
        """
        # Iterate over the clients
        for client in self.clients:
            # If the client's name matches the given name, return the client
            if client.name == name:
                return client
        # If no client with the given name was found, raise a ValueError
        raise ValueError(CLIENT_NOT_EXIST_VALIDATION_MSG)

    def add_client(self, name):
        """
        The method to add a client.

        Parameters:
            name (str): The name of the client.

        Returns:
            Client: The added client.
        """
        # Try to get the client with the given name
        try:
            client = self.get_client(name)
        # If no client with the given name exists, create a new client and add it to the clients list
        except ValueError as e:
            client = Client(name)
            self.clients.append(client)
        # Return the client
        return client

    def add_package(self, origin, destination, client, date):
        """
        The method to add a package.

        Parameters:
            origin (str): The origin of the package.
            destination (str): The destination of the package.
            client (Client): The client who owns the package.
            date (str): The date when the package is added.

        Returns:
            Package: The added package.
        """
        # Create a new package and add it to the packages list
        package = Package(origin, destination, client, date)
        self.packages.append(package)
        # Return the package
        return package

    def add_transportation_fee(self, date, fee):
        """
        The method to add a transportation fee.

        Parameters:
            date (str): The date when the fee is added.
            fee (int): The fee to be added.
        """
        # Validate the date and the fee
        date_format_validation(date)
        date_min_validation(date)
        int_fee_validation(fee)
        # Add the fee to the transportation fee dictionary
        self.transportation_fee[date] = int(fee)

    def get_transportation_fee(self, date):
        """
        The method to get the transportation fee for a given date.

        Parameters:
            date (str): The date for which to get the fee.

        Returns:
            int: The fee for the given date.
        """
        # Validate the date
        date_format_validation(date)
        date_range_validation(date)
        # Return the fee for the latest date that is not later than the given date
        return self.transportation_fee[max([key for key in self.transportation_fee if key <= date])]

    def get_total_transportation_report(self, date):
        """
        The method to get the total transportation report for a given date.

        Parameters:
            date (str): The date for which to get the report.

        Returns:
            str: The report for the given date.
        """
        # Initialize the total number of transported packages
        total = 0
        # Iterate over the packages
        for packages in self.packages:
            # If the package's date matches the given date, increment the total
            total += packages.date == date if 1 else 0
        # Get the transportation fee for the given date
        transportation_fee = self.get_transportation_fee(date)
        # Return the report
        return f"[DATE: {date} | FEE: {transportation_fee}]\nTotal packages transported: {total}\nTotal transportation fee charged: {total * transportation_fee}"

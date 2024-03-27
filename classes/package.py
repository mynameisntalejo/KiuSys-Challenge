from datetime import datetime

from classes.client import Client
from utils import PACKAGE_ORIGIN_VALIDATION_MSG, PACKAGE_DESTINATION_VALIDATION_MSG, \
    PACKAGE_ORIGIN_DESTINATION_SAME_VALIDATION_MSG, PACKAGE_CLIENT_VALIDATION_MSG, DATE_FORMAT


class Package:
    """
    The Package class represents a package with its origin, destination, client, and date.

    Attributes:
        origin (str): The origin of the package.
        destination (str): The destination of the package.
        client (Client): The client who owns the package.
        date (str): The date when the package is added.
    """

    def __init__(self, origin, destination, client, date=None):
        """
                The constructor for the Package class.

                Parameters:
                    origin (str): The origin of the package.
                    destination (str): The destination of the package.
                    client (Client): The client who owns the package.
                    date (str): The date when the package is added.
                """
        # Assign the origin, destination, client, and date to the package
        if len(origin) < 3:
            raise ValueError(PACKAGE_ORIGIN_VALIDATION_MSG)
        if len(destination) < 3:
            raise ValueError(PACKAGE_DESTINATION_VALIDATION_MSG)
        if origin == destination:
            raise ValueError(PACKAGE_ORIGIN_DESTINATION_SAME_VALIDATION_MSG)
        if not isinstance(client, Client):
            raise ValueError(PACKAGE_CLIENT_VALIDATION_MSG)
        self.origin = origin
        self.destination = destination
        self.client = client
        self.date = date if date else datetime.now().strftime(DATE_FORMAT)

    def __str__(self):
        """
        The method to get the string representation of the package.

        Returns:
            str: The string representation of the package.
        """
        # Return the details of the package
        return f"{self.origin} -> {self.destination} (from {self.client})"

    def __repr__(self):
        """
        The method to get the string representation of the package for debugging.

        Returns:
            str: The string representation of the package for debugging.
        """
        # Return the details of the package
        return f"{self.origin} -> {self.destination} (from {self.client})"

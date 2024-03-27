from utils import CLIENT_NAME_VALIDATION_MSG


class Client:
    """
    The Client class represents a client with its name.

    Attributes:
        name (str): The name of the client.
    """

    def __init__(self, name):
        """
        The constructor for the Client class.

        Parameters:
            name (str): The name of the client.
        """
        # Validate that the client name is at least 3 characters long
        if len(name) < 3:
            raise ValueError(CLIENT_NAME_VALIDATION_MSG)
        self.name = name

    def __str__(self):
        """
        The method to get the string representation of the client.

        Returns:
            str: The string representation of the client.
        """
        # Return the name of the client
        return f"{self.name}"

    def __repr__(self):
        """
        The method to get the string representation of the client for debugging.

        Returns:
            str: The string representation of the client for debugging.
        """
        # Return the name of the client
        return f"{self.name}"

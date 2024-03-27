import json
import unittest

from classes import Airline


def populate_system(airline):
    """
    Populate the airline system with data from a JSON file.

    Parameters:
        airline (Airline): The airline system to populate.
    """
    # Open and read the JSON file
    with open("tests/fixtures/packages.json", "r") as f:
        packages_data = json.load(f)[0]["demo_packages"]

    # Loop through the data and add each package to the system
    for package_data in packages_data:
        client = airline.add_client(package_data["client_str"])
        airline.add_package(package_data["origin"], package_data["destination"], client,
                            package_data["date"] if "date" in package_data else None)


def add_transportation_fee(airline):
    """
    Add a transportation fee to the airline system.

    Parameters:
        airline (Airline): The airline system to add the fee to.
    """
    date = input("\nPlease enter a date (dd/mm/yyyy): ")
    fee = input("Please enter the transportation fee: ")
    airline.add_transportation_fee(date, fee)
    print(f"Transportation fee for {date} set to {fee}.")


def add_client(airline):
    """
    Add a client to the airline system.

    Parameters:
        airline (Airline): The airline system to add the client to.
    """
    name = input("\nPlease enter the client's name: ")
    client = airline.add_client(name)
    print(f"Client {client.name} added.")


def add_package(airline):
    """
    Add a package to the airline system.

    Parameters:
        airline (Airline): The airline system to add the package to.
    """
    origin = input("Please enter the package's origin: ")
    destination = input("Please enter the package's destination: ")
    client_name = input("Please enter the client's name: ")
    date = input("Please enter the date (dd/mm/yyyy): ")
    client = airline.get_client(client_name)
    package = airline.add_package(origin, destination, client, date)
    print(
        f"Package from {package.origin} to {package.destination} for client {package.client.name} on date {package.date} added.")


def main():
    """
    Main function to run the airline system.
    """
    airline = Airline("Airline KiuSys-Challenge")

    # Loop to keep the system running until the user chooses to exit
    while True:
        print("\nWelcome to the System!")
        print("1. Populate system with default data")
        print("2. Add transportation fee")
        print("3. Add client")
        print("4. Add package")
        print("5. Execute main application")
        print("6. Run tests (and exit the program)")
        print("0. Exit the program")
        option = input("Please select an option (1, 2, 3, 4, 5, 6 or 0): ")

        # Handle the user's choice
        if option == "0":
            print("Thank you for using our system! Bye.")
            break
        elif option == "1":
            populate_system(airline)
            print("System populated with default data.")
        elif option == "2":
            try:
                add_transportation_fee(airline)
            except ValueError as e:
                print(e)
        elif option == "3":
            try:
                add_client(airline)
            except ValueError as e:
                print(e)
        elif option == "4":
            try:
                add_package(airline)
            except ValueError as e:
                print(e)
        elif option == "5":
            while True:
                date = input("\nPlease enter a date (dd/mm/yyyy): ")
                try:
                    report = airline.get_total_transportation_report(date)
                    print(report)
                except ValueError as e:
                    print(e)

                continue_prompt = input("\nDo you want to continue? (Yes/No): ")
                try:
                    if continue_prompt[0].lower() != "y":
                        print("Thank you for using our system! Bye.")
                        break
                except (ValueError, IndexError) as e:
                    print("Invalid input. Exiting system.")
                    break
        elif option == "6":
            # Discover and run the tests
            loader = unittest.TestLoader()
            start_dir = 'tests'
            suite = loader.discover(start_dir)
            runner = unittest.TextTestRunner()
            runner.run(suite)
            break
        else:
            print("Invalid option. Please select 1, 2, 3, 4, 5, 6 or 0 .")


if __name__ == "__main__":
    main()

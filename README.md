# Airline KiuSys-Challenge

This project is a simple airline system written in Python. It allows you to manage clients, packages, and transportation
fees.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing
purposes.

### Prerequisites

You need to have Python installed on your machine. You can download it from the official
website: https://www.python.org/downloads/

### Installing

Clone the repository to your local machine:

```bash
git clone https://github.com/mynameisntalejo/KiuSys-Challenge.git
```

Navigate to the project directory:

```bash
cd KiuSys-Challenge
```

### Using Fixtures

Fixtures are a way of loading data into the system for testing purposes. In this project, fixtures are stored in
the `tests/fixtures` directory as JSON files.

The `main.py` script includes a function `populate_system(airline)` that reads data from
the `tests/fixtures/packages.json` file and populates the system with this data. This function is used when you select
option 1 from the main menu ("Populate system with default data").

The `packages.json` file contains an array of package data. Each package data object includes the following fields:

- `client_str`: The name of the client.
- `origin`: The origin of the package.
- `destination`: The destination of the package.
- `date` (optional): The date of the package.

To use the fixtures, simply run the application and select option 1 from the main menu. The system will be populated
with the data from the `packages.json` file.

### Running the Application

To run the application, execute the `main.py` script:

```bash
python main.py
```

The system will present you with a menu of options:

1. Populate system with default data
2. Add transportation fee
3. Add client
4. Add package
5. Execute main application
6. Run tests (and exit the program)

Follow the prompts to interact with the system.

### Running the Tests

To run the tests, choose option 6 from the main menu. The tests are located in the `tests` directory and are structured
as unit tests.

## Built With

* [Python](https://www.python.org/)

## Authors

* **mynameisntalejo** - *Initial work* - [mynameisntalejo](https://github.com/mynameisntalejo)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
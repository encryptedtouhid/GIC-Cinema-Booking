# GIC Cinemas Booking System

## Project Overview

The GIC Cinemas Booking System is a command-line application that simulates a cinema ticket booking system. The system allows users to:

- Define a movie with a customizable seating layout
- Book multiple tickets with automatic or manual seat selection
- Check booking details using a unique booking ID
- Visualize the seating map with available, booked, and currently selected seats

The application follows SOLID principles and implements a clean, modular architecture to ensure maintainability and extensibility.

## Technologies Used

- **Python 3.9**: Core programming language
- **Built-in Libraries**:
  - `unittest`: For testing
  - `io`: For testing output
  - `sys`: For system-level operations
  - No external dependencies are required

## Project Structure

```
cinema_booking_system/
│
├── core/                      # Core application components
│   ├── __init__.py
│   ├── application.py         # Main application logic
│   └── menu.py                # Menu rendering
│
├── models/                    # Data models
│   ├── __init__.py
│   ├── movie.py               # Movie representation
│   ├── seat.py                # Seat representation
│   └── booking.py             # Booking representation
│
├── services/                  # Business logic services
│   ├── __init__.py
│   ├── booking_service.py     # Booking management
│   ├── display_service.py     # UI display logic
│   ├── input_service.py       # User input handling
│   └── seat_allocation_service.py  # Seat allocation strategies
│
├── utils/                     # Utility functions
│   ├── __init__.py
│   └── validator.py           # Input validation
│   └── strings_manager.py     # String constants management
│
├── tests/                     # Test suite
│   ├── test_models/           # Model tests
│   ├── test_services/         # Service tests 
│   └── __init__.py
│
├
└── main.py                    # Application entry point
```

## Design Patterns and Principles

### SOLID Principles Implementation

1. **Single Responsibility Principle**:
   - Each class has one specific responsibility
   - For example: `BookingService` handles bookings, `DisplayService` handles UI display

2. **Open/Closed Principle**:
   - Components are designed for extension without modification
   - New seating strategies could be added by extending the `SeatAllocationService`

3. **Liskov Substitution Principle**:
   - Classes are designed so subtypes can be used in place of parent types

4. **Interface Segregation Principle**:
   - Services have focused interfaces with specific purposes
   - No class implements methods it doesn't use

5. **Dependency Inversion Principle**:
   - High-level modules depend on abstractions
   - Dependencies are injected rather than created internally

### Design Patterns

- **Service Layer Pattern**: Separates business logic into dedicated service classes
- **Repository Pattern**: Used in `BookingService` for managing bookings
- **Strategy Pattern**: Implemented in seat allocation for different selection strategies
- **Dependency Injection**: Components receive their dependencies rather than creating them

## Setup Instructions

### Prerequisites

- Python 3.9 or higher

### Installation

1. Clone the repository or download the source code:

```bash
git clone https://github.com/encryptedtouhid/GIC-Cinema-Booking.git
cd GIC-Cinema-Booking
```

2. Install the package in development mode:

```bash
pip install -e .
```

Alternatively, you can add the project root to your Python path:

```bash
export PYTHONPATH=$PYTHONPATH:/path/to/GIC-Cinema-Booking
# On Windows:
# set PYTHONPATH=%PYTHONPATH%;C:\path\to\GIC-Cinema-Booking
```


2. No additional package installation is required as the project uses only built-in libraries.

## Running the Application

Execute the main script to start the application:

```bash
python main.py
```

3. Follow the prompts to book tickets or check existing bookings.

## Running Tests

The application includes a comprehensive test suite covering all components.

### Running All Tests

To run the entire test suite:

### Running Specific Tests

To run tests for a specific module:

```bash
python -m unittest tests/test_models/test_movie.py
```


### Test Coverage

The test suite includes:
- Unit tests for all models, services



## Package Setup (For Development)

If you want to develop this package, you should create a `setup.py` file in the root directory:

```python
from setuptools import setup, find_packages

setup(
    name="giccinema",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.9",
)
```
This will allow you to install the package in development mode using `pip install -e .`

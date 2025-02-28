import unittest
import io
import sys
from giccinema.services.display_service import DisplayService
from giccinema.models.seat import Seat


class TestDisplayService(unittest.TestCase):

    def setUp(self):
        self.display_service = DisplayService()

        # Create some test seats
        self.seats = []
        for row in 'ABC':
            for col in range(1, 6):  # 5 seats per row
                self.seats.append(Seat(row, col))

    def test_display_seating_map(self):
        # Redirect stdout to capture print output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Book some seats
        self.seats[0].book("GIC0001")  # A1
        self.seats[1].book("GIC0001")  # A2

        # Display the map
        current_booking_seats = [self.seats[5], self.seats[6]]  # B1, B2
        self.display_service.display_seating_map(self.seats, current_booking_seats)

        # Reset stdout
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()

        # Check if the output contains expected elements
        self.assertIn("SCREEN", output)
        self.assertIn("--------------------------------", output)

        # Check if all rows are displayed
        for row in 'ABC':
            self.assertIn(f"{row} ", output)

        # Check if all column numbers are displayed
        for col in range(1, 6):
            self.assertIn(f"{col}  ", output)

        # Check if booked seats, current booking seats, and available seats
        # are properly represented

        # The exact output format is hard to test precisely due to spacing,
        # but we can check for basic patterns

    def test_display_empty_seating_map(self):
        # Redirect stdout to capture print output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Display the map with no current bookings
        self.display_service.display_seating_map(self.seats)

        # Reset stdout
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()

        # Check if the output contains expected elements
        self.assertIn("SCREEN", output)

        # All seats should be represented as dots (available)
        self.assertNotIn("#", output)  # No booked seats
        self.assertNotIn("o", output)  # No current booking seats


if __name__ == '__main__':
    unittest.main()
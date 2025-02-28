import unittest
from giccinema.services.seat_allocation_service import SeatAllocationService


class TestSeatAllocationService(unittest.TestCase):
    def setUp(self):
        self.rows = 5
        self.seats_per_row = 10
        self.service = SeatAllocationService(self.rows, self.seats_per_row)

    def test_initialization(self):
        seats = self.service.seats

        # Check we have the correct number of seats
        self.assertEqual(len(seats), self.rows * self.seats_per_row)

        # Check rows are A-E
        rows = set(seat.row for seat in seats)
        self.assertEqual(rows, {'A', 'B', 'C', 'D', 'E'})

        # Check columns are 1-10
        for row in rows:
            cols = sorted(seat.col for seat in seats if seat.row == row)
            self.assertEqual(cols, list(range(1, self.seats_per_row + 1)))

    def test_get_available_seats(self):
        # Initially all seats are available
        available = self.service.get_available_seats()
        self.assertEqual(len(available), self.rows * self.seats_per_row)

        # Book a seat
        seat_to_book = available[0]
        seat_to_book.book("GIC0001")

        # Get available seats again
        available = self.service.get_available_seats()
        self.assertEqual(len(available), self.rows * self.seats_per_row - 1)
        self.assertNotIn(seat_to_book, available)

    def test_book_seats(self):
        seats = self.service.seats[:5]  # First 5 seats

        self.service.book_seats(seats, "GIC0001")

        # Check all seats are booked with the correct booking ID
        for seat in seats:
            self.assertTrue(seat.is_booked)
            self.assertEqual(seat.booking_id, "GIC0001")

    def test_get_default_allocation(self):
        # Request 4 seats
        allocation = self.service.get_default_allocation(4)

        # Should allocate 4 seats in row A (furthest from screen)
        # starting from middle position
        self.assertEqual(len(allocation), 4)
        self.assertTrue(all(seat.row == 'A' for seat in allocation))

        # Middle positions for 4 seats in a 10-seat row would be positions 4, 5, 6, 7
        cols = sorted(seat.col for seat in allocation)
        self.assertEqual(cols, [4, 5, 6, 7])

    def test_get_custom_allocation(self):
        # Request 3 seats starting from B5
        allocation = self.service.get_custom_allocation(3, "B5")

        # Should allocate 3 seats in row B starting from position 5
        self.assertEqual(len(allocation), 3)
        self.assertTrue(all(seat.row == 'B' for seat in allocation))

        cols = sorted(seat.col for seat in allocation)
        self.assertEqual(cols, [5, 6, 7])

    def test_custom_allocation_with_overflow(self):
        # Book some seats to force overflow
        seats_to_book = [s for s in self.service.seats if s.row == 'B' and s.col > 7]
        self.service.book_seats(seats_to_book, "GIC0001")

        # Request 5 seats starting from B5
        # Only 3 seats available in row B (5, 6, 7), so 2 should overflow to row C
        allocation = self.service.get_custom_allocation(5, "B5")

        self.assertEqual(len(allocation), 5)

        # Check row B has positions 5, 6, 7
        b_seats = [s for s in allocation if s.row == 'B']
        b_cols = sorted(s.col for s in b_seats)
        self.assertEqual(b_cols, [5, 6, 7])

        # Check row C has 2 seats from the middle
        c_seats = [s for s in allocation if s.row == 'C']
        self.assertEqual(len(c_seats), 2)

    def test_get_seat_by_position(self):
        seat = self.service.get_seat_by_position("C7")

        self.assertIsNotNone(seat)
        self.assertEqual(seat.row, 'C')
        self.assertEqual(seat.col, 7)

        # Try a non-existent position
        non_existent = self.service.get_seat_by_position("Z99")
        self.assertIsNone(non_existent)

    def test_get_seats_for_booking(self):
        # Book some seats with different booking IDs
        seats1 = self.service.seats[:3]  # First 3 seats
        seats2 = self.service.seats[10:14]  # 4 seats

        self.service.book_seats(seats1, "GIC0001")
        self.service.book_seats(seats2, "GIC0002")

        # Get seats for booking GIC0001
        booking_seats = self.service.get_seats_for_booking("GIC0001")

        self.assertEqual(len(booking_seats), 3)
        self.assertEqual(set(booking_seats), set(seats1))

        # Get seats for booking GIC0002
        booking_seats = self.service.get_seats_for_booking("GIC0002")

        self.assertEqual(len(booking_seats), 4)
        self.assertEqual(set(booking_seats), set(seats2))

        # Try a non-existent booking ID
        non_existent = self.service.get_seats_for_booking("NONEXISTENT")
        self.assertEqual(len(non_existent), 0)


if __name__ == '__main__':
    unittest.main()
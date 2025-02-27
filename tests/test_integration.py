import unittest
from giccinema.core.cinema import CinemaHall
from giccinema.services.booking_service import BookingService
from giccinema.core.seat_allocator import SeatAllocator

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.cinema = CinemaHall("Inception", 8, 10)
        self.booking_service = BookingService(self.cinema)
        self.allocator = SeatAllocator()

    def test_full_booking_flow(self):
        # Step 1: Book 4 seats
        booking_id1, seats1 = self.booking_service.book_tickets(4)
        self.assertIsNotNone(booking_id1)

        # Step 2: Book 6 seats
        booking_id2, seats2 = self.booking_service.book_tickets(6)
        self.assertIsNotNone(booking_id2)

        # Step 3: Check bookings
        self.assertEqual(self.booking_service.check_booking(booking_id1), seats1)
        self.assertEqual(self.booking_service.check_booking(booking_id2), seats2)

        # Step 4: Ensure remaining seats updated
        self.assertEqual(self.cinema.available_seats, 70)

    def test_overbooking(self):
        # Try to book more seats than available
        booking_id, seats = self.booking_service.book_tickets(100)
        self.assertIsNone(booking_id)

    def test_seat_persistence(self):
        # Step 1: Book 4 seats
        booking_id, seats = self.booking_service.book_tickets(4)
        self.assertIsNotNone(booking_id)

        # Step 2: Verify seats are not overwritten by another booking
        second_booking_id, second_seats = self.booking_service.book_tickets(3)
        self.assertIsNotNone(second_booking_id)
        self.assertNotEqual(seats, second_seats)

if __name__ == "__main__":
    unittest.main()

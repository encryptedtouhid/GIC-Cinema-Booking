import unittest
from giccinema.core.cinema import CinemaHall
from giccinema.services.booking_service import BookingService
from giccinema.core.seat_allocator import SeatAllocator

class TestBookingService(unittest.TestCase):
    def setUp(self):
        self.cinema = CinemaHall("Inception", 8, 10)
        self.booking_service = BookingService(self.cinema)
        self.allocator = SeatAllocator()

    def test_successful_booking(self):
        booking_id, seats = self.booking_service.book_tickets(5)
        self.assertIsNotNone(booking_id)
        self.assertEqual(len(seats), 5)

    def test_booking_not_exceeding_capacity(self):
        booking_id, seats = self.booking_service.book_tickets(100)
        self.assertIsNone(booking_id)

    def test_check_booking_exists(self):
        booking_id, seats = self.booking_service.book_tickets(3)
        self.assertEqual(self.booking_service.check_booking(booking_id), seats)

    def test_check_invalid_booking(self):
        self.assertIsNone(self.booking_service.check_booking("GIC9999"))

if __name__ == "__main__":
    unittest.main()

import unittest
from giccinema.core.cinema import CinemaHall
from giccinema.core.seat_allocator import SeatAllocator

class TestCinemaHall(unittest.TestCase):
    def setUp(self):
        self.cinema = CinemaHall("Inception", 8, 10)
        self.seat_allocator = SeatAllocator()

    def test_successful_booking(self):
        booking_id, seats = self.cinema.book_tickets(4, self.seat_allocator)
        self.assertIsNotNone(booking_id)
        self.assertEqual(len(seats), 4)

    def test_booking_exceeds_capacity(self):
        booking_id, seats = self.cinema.book_tickets(100, self.seat_allocator)
        self.assertIsNone(booking_id)

    def test_check_booking_exists(self):
        booking_id, seats = self.cinema.book_tickets(2, self.seat_allocator)
        self.assertEqual(self.cinema.check_booking(booking_id), seats)

    def test_check_invalid_booking(self):
        self.assertIsNone(self.cinema.check_booking("GIC9999"))

if __name__ == "__main__":
    unittest.main()

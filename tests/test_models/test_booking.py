import unittest
from giccinema.models.booking import Booking
from giccinema.models.seat import Seat


class TestBooking(unittest.TestCase):

    def test_initialization(self):

        # Create some seats
        seat1 = Seat("A", 3)
        seat2 = Seat("A", 4)
        seat3 = Seat("A", 5)
        seats = [seat1, seat2, seat3]

        booking = Booking("GIC0001", "Inception", seats)

        self.assertEqual(booking.booking_id, "GIC0001")
        self.assertEqual(booking.movie_title, "Inception")
        self.assertEqual(booking.seats, seats)

    def test_get_seat_count(self):

        # Create some seats
        seats = [Seat("B", i) for i in range(1, 6)]  # 5 seats

        booking = Booking("GIC0002", "Avatar", seats)

        self.assertEqual(booking.get_seat_count(), 5)

        # Add more seats
        seats.append(Seat("C", 1))

        self.assertEqual(booking.get_seat_count(), 6)


if __name__ == '__main__':
    unittest.main()
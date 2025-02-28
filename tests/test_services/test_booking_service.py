import unittest
from giccinema.services.booking_service import BookingService
from giccinema.models.seat import Seat


class TestBookingService(unittest.TestCase):

    def setUp(self):
        self.booking_service = BookingService()

    def test_generate_booking_id(self):
        id1 = self.booking_service.generate_booking_id()
        id2 = self.booking_service.generate_booking_id()
        id3 = self.booking_service.generate_booking_id()

        # Check format
        self.assertTrue(id1.startswith("GIC"))
        self.assertTrue(id2.startswith("GIC"))
        self.assertTrue(id3.startswith("GIC"))

        # Check sequential numbering
        self.assertEqual(id1, "GIC0001")
        self.assertEqual(id2, "GIC0002")
        self.assertEqual(id3, "GIC0003")

    def test_create_booking(self):
        # Create some seats
        seats = [Seat("A", i) for i in range(1, 4)]  # 3 seats

        booking_id = "GIC0001"
        booking = self.booking_service.create_booking(booking_id, "Inception", seats)

        # Check booking details
        self.assertEqual(booking.booking_id, booking_id)
        self.assertEqual(booking.movie_title, "Inception")
        self.assertEqual(booking.seats, seats)

        # Check it was added to the bookings dict
        self.assertIn(booking_id, self.booking_service.bookings)
        self.assertEqual(self.booking_service.bookings[booking_id], booking)

    def test_get_booking(self):
        # Create a booking
        seats = [Seat("B", i) for i in range(1, 3)]  # 2 seats

        booking_id = "GIC0001"
        booking = self.booking_service.create_booking(booking_id, "Matrix", seats)

        # Get the booking
        retrieved_booking = self.booking_service.get_booking(booking_id)

        # Check it's the same booking
        self.assertEqual(retrieved_booking, booking)

        # Try a non-existent booking
        non_existent = self.booking_service.get_booking("NONEXISTENT")
        self.assertIsNone(non_existent)


if __name__ == '__main__':
    unittest.main()
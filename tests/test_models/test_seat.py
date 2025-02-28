import unittest
from giccinema.models.seat import Seat


class TestSeat(unittest.TestCase):

    def test_initialization(self):
        seat = Seat("A", 5)

        self.assertEqual(seat.row, "A")
        self.assertEqual(seat.col, 5)
        self.assertFalse(seat.is_booked)
        self.assertIsNone(seat.booking_id)

    def test_book_seat(self):

        seat = Seat("B", 3)

        seat.book("GIC0001")

        self.assertTrue(seat.is_booked)
        self.assertEqual(seat.booking_id, "GIC0001")

    def test_unbook_seat(self):

        seat = Seat("C", 7)

        # First book the seat
        seat.book("GIC0002")
        self.assertTrue(seat.is_booked)

        # Then unbook it
        seat.unbook()

        self.assertFalse(seat.is_booked)
        self.assertIsNone(seat.booking_id)

    def test_string_representation(self):
        seat1 = Seat("A", 1)
        seat2 = Seat("B", 10)
        seat3 = Seat("H", 5)

        self.assertEqual(str(seat1), "A01")
        self.assertEqual(str(seat2), "B10")
        self.assertEqual(str(seat3), "H05")


if __name__ == '__main__':
    unittest.main()
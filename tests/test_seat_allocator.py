import unittest
from giccinema.core.seat_allocator import SeatAllocator

class TestSeatAllocator(unittest.TestCase):
    def setUp(self):
        self.rows = 8
        self.seats_per_row = 10
        self.seating_chart = [['.' for _ in range(self.seats_per_row)] for _ in range(self.rows)]
        self.allocator = SeatAllocator()

    def test_allocate_single_seat(self):
        seats = self.allocator.allocate_seats(self.seating_chart, 1)
        self.assertEqual(len(seats), 1)

    def test_allocate_multiple_seats(self):
        seats = self.allocator.allocate_seats(self.seating_chart, 3)
        self.assertEqual(len(seats), 3)

    def test_allocate_too_many_seats(self):
        seats = self.allocator.allocate_seats(self.seating_chart, 100)
        self.assertEqual(seats, [])

    def test_allocate_seats_in_full_row(self):
        for i in range(self.seats_per_row):
            self.seating_chart[7][i] = 'o'  # Mark the last row as fully booked
        seats = self.allocator.allocate_seats(self.seating_chart, 2)
        self.assertTrue(all(row != 7 for row, col in seats))  # Ensure no seats are allocated in row 7

if __name__ == "__main__":
    unittest.main()

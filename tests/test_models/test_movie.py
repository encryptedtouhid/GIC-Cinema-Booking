import unittest
from giccinema.models.movie import Movie


class TestMovie(unittest.TestCase):

    def test_initialization(self):
        movie = Movie("Inception", 8, 10)

        self.assertEqual(movie.title, "Inception")
        self.assertEqual(movie.rows, 8)
        self.assertEqual(movie.seats_per_row, 10)
        self.assertEqual(movie.total_seats, 80)
        self.assertEqual(movie.available_seats, 80)

    def test_total_seats_calculation(self):
        movie = Movie("Tenet", 5, 12)
        self.assertEqual(movie.total_seats, 60)

    def test_available_seats_update(self):
        movie = Movie("Dune", 10, 10)
        self.assertEqual(movie.available_seats, 100)

        # Simulate booking 5 seats
        movie.available_seats -= 5
        self.assertEqual(movie.available_seats, 95)

        # Simulate booking 10 more seats
        movie.available_seats -= 10
        self.assertEqual(movie.available_seats, 85)


if __name__ == '__main__':
    unittest.main()
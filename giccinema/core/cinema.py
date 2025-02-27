import itertools
import string


class CinemaHall:
    def __init__(self, movie_title, rows, seats_per_row):
        self.movie_title = movie_title
        self.rows = min(rows, 26)
        self.seats_per_row = min(seats_per_row, 50)
        self.total_seats = self.rows * self.seats_per_row
        self.available_seats = self.total_seats
        self.bookings = {}
        self.seating_chart = [['.' for _ in range(self.seats_per_row)] for _ in range(self.rows)]
        self.booking_counter = itertools.count(1)  # Unique booking ID generator

    def book_tickets(self, num_tickets, seat_allocator, custom_position=None):
        if num_tickets > self.available_seats:
            return None, None

        seats = seat_allocator.allocate_seats(self.seating_chart, num_tickets, custom_position)
        if not seats:
            return None, None

        booking_id = f"GIC{next(self.booking_counter):04d}"
        for row, col in seats:
            self.seating_chart[row][col] = 'o'
        self.bookings[booking_id] = seats
        self.available_seats -= num_tickets
        return booking_id, seats

    def check_booking(self, booking_id):
        return self.bookings.get(booking_id, None)


import string
from giccinema.services.booking_factory import BookingFactory


class CinemaService:
    def __init__(self, movie_title, rows, seats_per_row):
        self.movie_title = movie_title
        self.rows = min(rows, 26)
        self.seats_per_row = min(seats_per_row, 50)
        self.seating_chart = [['.' for _ in range(self.seats_per_row)] for _ in range(self.rows)]
        self.bookings = {}
        self.available_seats = self.rows * self.seats_per_row
        self.booking_counter = 1

    def allocate_seats(self, num_tickets):
        seats = []
        row_idx = 0  # Allocate seats in the first row (A) first
        mid = self.seats_per_row // 2
        seat_indices = sorted(range(self.seats_per_row), key=lambda x: abs(mid - x))
        for col in seat_indices:
            if self.seating_chart[row_idx][col] == '.' and len(seats) < num_tickets:
                seats.append((row_idx, col))
            if len(seats) == num_tickets:
                for row, col in seats:
                    self.seating_chart[row][col] = 'o'
                self.available_seats -= num_tickets
                return seats
        return []

    def make_booking(self, tickets):
        booking = BookingFactory.create_booking(self, tickets)
        if booking:
            self.bookings[booking.id] = booking.seats
        return booking

    def check_booking(self, booking_id):
        return self.bookings.get(booking_id, None)

    def get_seating_display(self, highlight_seats=None):
        display = "\n          S C R E E N\n" + "-" * 32 + "\n"
        for row_idx, row in enumerate(self.seating_chart[::-1]):
            row_label = string.ascii_uppercase[len(self.seating_chart) - row_idx - 1]
            row_display = ['o' if (len(self.seating_chart) - row_idx - 1, col) in highlight_seats else (
                '#' if cell == 'o' else '.') for col, cell in enumerate(row)]
            display += f"{row_label} {'  '.join(row_display)}\n"
        display += "  " + "  ".join(str(i + 1) for i in range(self.seats_per_row))
        return display
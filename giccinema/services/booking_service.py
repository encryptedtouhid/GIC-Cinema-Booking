import string
from giccinema.services.booking_factory import BookingFactory
from giccinema.common.strings_manager import StringManager

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

    def try_rebook_seats(self, booking, seat_input):
        if not seat_input:
            return True

        if len(seat_input) < 2 or not seat_input[0].isalpha() or not seat_input[1:].isdigit():
            return False

        row_idx = ord(seat_input[0].upper()) - ord('A')
        col_idx = int(seat_input[1:]) - 1

        if row_idx >= self.rows or col_idx >= self.seats_per_row or self.seating_chart[row_idx][col_idx] != '.':
            return False

        # Clear previous seats
        for row, col in self.bookings[booking.id]:
            self.seating_chart[row][col] = '.'

        # Assign new seats
        new_seats = [(row_idx, col_idx)]
        self.seating_chart[row_idx][col_idx] = 'o'
        self.bookings[booking.id] = new_seats

        return True

    def get_seating_display(self, highlight_seats=None):
        display = f"\n          {StringManager.SCREEN}\n" + "-" * 32 + "\n"
        for row_idx, row in enumerate(self.seating_chart[::-1]):
            row_label = string.ascii_uppercase[len(self.seating_chart) - row_idx - 1]
            row_display = ['o' if (len(self.seating_chart) - row_idx - 1, col) in highlight_seats else (
                '#' if cell == 'o' else '.') for col, cell in enumerate(row)]
            display += f"{row_label} {'  '.join(row_display)}\n"
        display += "  " + "  ".join(str(i + 1) for i in range(self.seats_per_row))
        return display

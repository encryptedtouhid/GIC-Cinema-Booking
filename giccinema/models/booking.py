class Booking:

    def __init__(self, booking_id, movie_title, seats):

        self.booking_id = booking_id
        self.movie_title = movie_title
        self.seats = seats  # List of Seat objects

    def get_seat_count(self):
        """Get the number of seats in this booking."""
        return len(self.seats)
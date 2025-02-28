from giccinema.models.booking import Booking

class BookingService:
    def __init__(self):
        self.bookings = {}
        self.booking_counter = 0

    def generate_booking_id(self):
        self.booking_counter += 1
        return f"GIC{self.booking_counter:04d}"

    def create_booking(self, booking_id, movie_title, seats):
        booking = Booking(booking_id, movie_title, seats)
        self.bookings[booking_id] = booking
        return booking

    def get_booking(self, booking_id):
        return self.bookings.get(booking_id)
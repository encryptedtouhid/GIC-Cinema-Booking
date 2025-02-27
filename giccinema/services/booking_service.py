from giccinema.core.cinema import CinemaHall
from giccinema.core.seat_allocator import SeatAllocator

class BookingService:
    def __init__(self, cinema: CinemaHall):
        self.cinema = cinema
        self.seat_allocator = SeatAllocator()

    def book_tickets(self, num_tickets, custom_position=None):
        return self.cinema.book_tickets(num_tickets, self.seat_allocator, custom_position)

    def check_booking(self, booking_id):
        return self.cinema.check_booking(booking_id)

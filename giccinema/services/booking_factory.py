from giccinema.models.booking import Booking


class BookingFactory:
    @staticmethod
    def create_booking(cinema, tickets):
        allocated_seats = cinema.allocate_seats(tickets)
        if not allocated_seats:
            return None

        booking_id = f"GIC{cinema.booking_counter:04d}"
        cinema.booking_counter += 1

        return Booking(booking_id, tickets, allocated_seats)

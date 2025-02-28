from giccinema.core.menu import Menu
from giccinema.models.movie import Movie
from giccinema.services.booking_service import BookingService
from giccinema.services.display_service import DisplayService
from giccinema.services.input_service import InputService
from giccinema.services.seat_allocation_service import SeatAllocationService
from giccinema.utils.strings_manager import StringManager
from giccinema.utils.validator import Validator


class Application:

    def __init__(self):
        self.string_manager = StringManager()
        self.input_service = InputService()
        self.display_service = DisplayService()
        self.booking_service = BookingService()

        # Initialize movie and seats
        title, rows, seats_per_row = self.input_service.get_movie_input()
        self.movie = Movie(title, rows, seats_per_row)
        self.seat_allocation_service = SeatAllocationService(rows, seats_per_row)

        # Create menu
        self.menu = Menu(self.movie)

    def run(self):

        while True:
            self.menu.display()
            selection = self.input_service.get_menu_selection()

            if selection == 1:
                self.book_tickets()
            elif selection == 2:
                self.check_bookings()
            elif selection == 3:
                print(self.string_manager.MSG_THANK_YOU)
                break
            else:
                print(self.string_manager.MSG_RETRY)

    def book_tickets(self):
        print()
        print(self.string_manager.TICKET_INPUT)

        while True:
            num_tickets = self.input_service.get_number_of_tickets()
            if num_tickets is None:
                print(self.string_manager.RETURN_TO_MENU)
                return

            available_seats = self.seat_allocation_service.get_available_seats()
            if len(available_seats) < num_tickets:
                print(self.string_manager.MSG_AVAILABLE_SEAT.format(len(available_seats)))
                print()
                print(self.string_manager.TICKET_INPUT)
                continue

            # Get default seat allocation
            allocated_seats = self.seat_allocation_service.get_default_allocation(num_tickets)
            if not allocated_seats:
                print(self.string_manager.MSG_BOOKING_FAILED)
                print()
                print(self.string_manager.TICKET_INPUT)
                continue

            # If we reach here, we have a valid number of tickets and allocation
            break

        # Generate booking ID
        booking_id = self.booking_service.generate_booking_id()

        print()
        print(self.string_manager.MSG_RESERVED.format(num_tickets, self.movie.title))
        print(self.string_manager.BOOKING_ID.format(booking_id))
        print(self.string_manager.MSG_SELECTED_SEAT)

        self.display_service.display_seating_map(self.seat_allocation_service.seats, allocated_seats)

        while True:
            print(self.string_manager.MSG_ACCEPT_OR_BLANK)
            seat_selection = self.input_service.get_seat_selection()

            if seat_selection is None:
                # User accepted default allocation
                break

            # Validate seat position
            if not Validator.is_valid_seat_position(seat_selection, self.movie.rows, self.movie.seats_per_row):
                print(self.string_manager.MSG_INVALID_SEAT)
                continue

            # Try custom allocation
            custom_allocated_seats = self.seat_allocation_service.get_custom_allocation(num_tickets, seat_selection)
            if not custom_allocated_seats:
                print(self.string_manager.MSG_BOOKING_FAILED)
                continue

            allocated_seats = custom_allocated_seats

            print()
            print(self.string_manager.BOOKING_ID.format(booking_id))
            print(self.string_manager.MSG_SELECTED_SEAT)
            self.display_service.display_seating_map(self.seat_allocation_service.seats, allocated_seats)

        # Confirm booking
        self.seat_allocation_service.book_seats(allocated_seats, booking_id)
        booking = self.booking_service.create_booking(booking_id, self.movie.title, allocated_seats)

        self.movie.available_seats -= num_tickets

        print()
        print(f"{self.string_manager.BOOKING_ID.format(booking_id)} {self.string_manager.CONFIRMED_TEXT}")

    def check_bookings(self):

        print()
        print(self.string_manager.BOOKING_ID_INPUT)

        while True:
            booking_id = self.input_service.get_booking_id()
            if booking_id is None:
                break

            booking = self.booking_service.get_booking(booking_id)
            if not booking:
                print(self.string_manager.MSG_INVALID_BOOKING)
                print()
                print(self.string_manager.BOOKING_ID_INPUT)
                continue

            print()
            print(self.string_manager.BOOKING_ID.format(booking_id))
            print(self.string_manager.MSG_SELECTED_SEAT)

            booked_seats = self.seat_allocation_service.get_seats_for_booking(booking_id)
            self.display_service.display_seating_map(self.seat_allocation_service.seats, booked_seats)

            print()
            print(self.string_manager.BOOKING_ID_INPUT)
from giccinema.common.strings_manager import StringManager
from giccinema.services.booking_service import CinemaService
from giccinema.views.console_view import ConsoleView
from giccinema.common.message_provider import show_message


class CinemaController:
    def __init__(self):
        self.cinema = None

    def start(self):
        movie_info = input(f"{StringManager.MSG_INITIATE}\n> ")
        title, rows, seats = movie_info.rsplit(" ", 2)
        self.cinema = CinemaService(title, int(rows), int(seats))

        while True:
            print(f"\n{StringManager.MSG_WELCOME}")
            print(f"{StringManager.OPTION_ONE.format(self.cinema.movie_title, self.cinema.available_seats)}")
            print(f"{StringManager.OPTION_TWO}")
            print(f"{StringManager.OPTION_THREE}")

            choice = input(f"{StringManager.REQUEST_INPUT}").strip()
            if choice == "1":
                self.handle_booking()
            elif choice == "2":
                self.handle_check_booking()
            elif choice == "3":
                print(f"{StringManager.MSG_THANK_YOU}")
                break
            else:
                show_message(StringManager.MSG_RETRY, "err")

    def handle_booking(self):
        while True:
            num_tickets = input(f"{StringManager.TICKET_INPUT}\n> ")
            if not num_tickets:
                return

            try:
                num_tickets = int(num_tickets)
            except ValueError:
                show_message(f"{StringManager.MSG_INVALID_NUMBER}", "err")
                continue

            if num_tickets > self.cinema.available_seats:
                show_message(f"{StringManager.MSG_AVAILABLE_SEAT.format(self.cinema.available_seats)}", "err")
                continue

            booking = self.cinema.make_booking(num_tickets)
            if not booking:
                show_message(f"{StringManager.MSG_BOOKING_FAILED}", "err")
                continue

            print(f"{StringManager.MSG_RESERVED.format(num_tickets, self.cinema.movie_title)}")
            print(f"{StringManager.BOOKING_ID.format(booking.id)}")
            print(self.cinema.get_seating_display(highlight_seats=booking.seats))

            while True:
                new_choice = input(f"\n{StringManager.MSG_ACCEPT_OR_BLANK}").strip()
                if not new_choice:
                    print(f"\nBooking id: {booking.id} confirmed.")
                    return

                rebooked = self.cinema.try_rebook_seats(booking, new_choice)
                if rebooked:
                    print(f"\nBooking id: {booking.id}")
                    print(self.cinema.get_seating_display(highlight_seats=booking.seats))
                else:
                    show_message(StringManager.MSG_INVALID_SEAT, "err")


from giccinema.services.booking_service import BookingService
from giccinema.views.console_view import ConsoleView

class CinemaController:
    def __init__(self):
        self.cinema = None

    def start(self):
        movie_info = input("Please define movie title and seating map in [Title] [Row] [SeatsPerRow] format:\n> ")
        title, rows, seats = movie_info.rsplit(" ", 2)
        self.cinema = BookingService(title, int(rows), int(seats))

        while True:
            choice = ConsoleView.display_menu(self.cinema.movie_title, self.cinema.available_seats)
            if choice == "1":
                self.handle_booking()
            elif choice == "2":
                self.handle_check_booking()
            elif choice == "3":
                print("Thank you for using GIC Cinemas system. Bye!")
                break
            else:
                print("\nInvalid selection, please try again.")

    def handle_booking(self):
        num_tickets = ConsoleView.get_number_of_tickets()
        if not num_tickets:
            return
        booking = self.cinema.make_booking(num_tickets)
        if not booking:
            print("Not enough seats available. Try again.")
            return
        ConsoleView.display_booking(booking, self.cinema)

        while True:
            new_seat_input = ConsoleView.get_new_seat_input()
            if not new_seat_input:
                print(f"\nBooking id: {booking.id} confirmed.")
                return
            rebooked = self.cinema.try_rebook_seats(booking, new_seat_input)
            if rebooked:
                ConsoleView.display_booking(booking, self.cinema)
            else:
                print("\nInvalid seat selection. Try again.")

    def handle_check_booking(self):
        while True:
            booking_id = ConsoleView.get_booking_id()
            if not booking_id:
                return
            seats = self.cinema.check_booking(booking_id)
            if seats:
                ConsoleView.display_booking_details(booking_id, seats, self.cinema)
                break
            print("\nInvalid booking ID. Try again.")

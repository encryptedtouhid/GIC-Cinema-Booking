from giccinema.services.booking_service import CinemaService
from giccinema.views.console_view import ConsoleView


class CinemaController:
    def __init__(self):
        self.cinema = None

    def start(self):
        movie_info = input("Please define movie title and seating map in [Title] [Row] [SeatsPerRow] format:\n> ")
        title, rows, seats = movie_info.rsplit(" ", 2)
        self.cinema = CinemaService(title, int(rows), int(seats))

        while True:
            print(f"\nWelcome to GIC Cinemas")
            print(f"[1] Book tickets for {self.cinema.movie_title} ({self.cinema.available_seats} seats available)")
            print("[2] Check bookings")
            print("[3] Exit")
            choice = input("Please enter your selection: ").strip()
            if choice == "1":
                self.handle_booking()
            elif choice == "2":
                self.handle_check_booking()
            elif choice == "3":
                print("Thank you for using GIC Cinemas system. Bye!")
                break

    def handle_booking(self):
        while True:
            num_tickets = input("Enter number of tickets to book, or enter blank to go back to main menu:\n> ")
            if not num_tickets:
                return

            try:
                num_tickets = int(num_tickets)
            except ValueError as e:
                print(f"\nInvalid input. Please enter a valid number.")
                return

            if num_tickets > self.cinema.available_seats:
                print(f"\nSorry, there are only {self.cinema.available_seats} seats available.")
                continue
            booking = self.cinema.make_booking(num_tickets)
            if not booking:
                print("Not enough seats available. Try again.")
                continue
            print(f"Successfully reserved {num_tickets} {self.cinema.movie_title} tickets. Booking id: {booking.id}")
            print(self.cinema.get_seating_display(highlight_seats=booking.seats))

    def handle_check_booking(self):
        while True:
            booking_id = input("Enter booking ID, or enter blank to go back to main menu:\n> ")
            if not booking_id:
                return
            seats = self.cinema.check_booking(booking_id)
            if not seats:
                print("Booking ID not found.")
            else:
                print(f"Booking id: {booking_id}")
                print(self.cinema.get_seating_display(highlight_seats=seats))

from giccinema.core.cinema import CinemaHall
from giccinema.services.booking_service import BookingService
from giccinema.views.console_view import ConsoleView
import string

class CinemaController:
    def __init__(self):
        self.cinema = None

    def start(self):
        movie_info = input("Please define movie title and seating map in [Title] [Row] [SeatsPerRow] format:\n> ")
        title, rows, seats = movie_info.rsplit(" ", 2)
        self.cinema = CinemaHall(title, int(rows), int(seats))
        self.booking_service = BookingService(self.cinema)

        while True:
            choice = ConsoleView.display_menu(self.cinema.movie_title, self.cinema.available_seats)
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
            num_tickets = int(num_tickets)
            booking_id, seats = self.booking_service.book_tickets(num_tickets)

            if not booking_id:
                print("Not enough seats available. Try again.")
                continue

            print(f"Successfully reserved {num_tickets} {self.cinema.movie_title} tickets.")
            print(f"Booking id: {booking_id}")
            ConsoleView.display_seating_chart(self.cinema, highlight_seats=seats)

            while True:
                custom_seat_input = input("Enter blank to accept seat selection, or enter new seating position (e.g., B03):\n> ")
                if not custom_seat_input:
                    break
                row_letter, col_number = custom_seat_input[0], int(custom_seat_input[1:]) - 1
                row_idx = string.ascii_uppercase.index(row_letter)
                custom_seats = self.booking_service.book_tickets(num_tickets, (row_idx, col_number))
                if custom_seats:
                    print(f"Booking id: {booking_id}")
                    ConsoleView.display_seating_chart(self.cinema, highlight_seats=custom_seats)
                    break
                print("Invalid seating position. Try again.")
            print(f"Booking id: {booking_id} confirmed.")

    def handle_check_booking(self):
        while True:
            booking_id = input("Enter booking ID, or enter blank to go back to main menu:\n> ")
            if not booking_id:
                return
            seats = self.booking_service.check_booking(booking_id)
            if not seats:
                print("Booking ID not found.")
            else:
                print(f"Booking id: {booking_id}")
                ConsoleView.display_seating_chart(self.cinema, highlight_seats=seats)

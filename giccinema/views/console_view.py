import string

class ConsoleView:
    @staticmethod
    def display_menu(movie_title, available_seats):
        print(f"\n[1] Book tickets for {movie_title} ({available_seats} seats available)")
        print("[2] Check bookings")
        print("[3] Exit")
        return input("Please enter your selection: ").strip()

    @staticmethod
    def get_number_of_tickets():
        while True:
            num_tickets = input("Enter number of tickets to book, or enter blank to go back to main menu:\n> ")
            if not num_tickets:
                return None
            try:
                return int(num_tickets)
            except ValueError:
                print("Invalid number. Please try again.")

    @staticmethod
    def get_booking_id():
        return input("Enter booking ID, or enter blank to go back to main menu:\n> ")

    @staticmethod
    def get_new_seat_input():
        return input("Enter blank to accept seat selection, or enter new seating position (e.g., B03):\n> ")

    @staticmethod
    def display_booking(booking, cinema):
        print(f"Successfully reserved {booking.tickets} {cinema.movie_title} tickets. Booking id: {booking.id}")
        print(cinema.get_seating_display(highlight_seats=booking.seats))

    @staticmethod
    def display_booking_details(booking_id, seats, cinema):
        print(f"Booking id: {booking_id}")
        print(cinema.get_seating_display(highlight_seats=seats))

import string

class ConsoleView:
    @staticmethod
    def display_menu(movie_title, available_seats):
        print("\nWelcome to GIC Cinemas")
        print(f"[1] Book tickets for {movie_title} ({available_seats} seats available)")
        print("[2] Check bookings")
        print("[3] Exit")
        return input("Please enter your selection: ").strip()

    @staticmethod
    def display_seating_chart(cinema, highlight_seats=None):
        print("\n          S C R E E N")
        print("--------------------------------")
        for row_idx, row in enumerate(cinema.seating_chart):
            row_label = string.ascii_uppercase[row_idx]
            row_display = [
                'o' if (row_idx, col) in highlight_seats else ('#' if cell == 'o' else '.')
                for col, cell in enumerate(row)
            ]
            print(f"{row_label} {'  '.join(row_display)}")
        print("   " + "  ".join(str(i + 1) for i in range(cinema.seats_per_row)))

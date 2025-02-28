from giccinema.utils.strings_manager import StringManager


class DisplayService:

    def __init__(self):
        self.string_manager = StringManager()

    def display_seating_map(self, seats, current_booking_seats=None):
        if current_booking_seats is None:
            current_booking_seats = []

        # Determine dimensions
        max_row = max(seat.row for seat in seats)
        max_col = max(seat.col for seat in seats)

        # Create header
        print()
        print(f"          {self.string_manager.SCREEN}")
        print("--------------------------------")

        # Create rows from furthest to closest to screen
        for row in range(ord(max_row), ord('A') - 1, -1):
            row_char = chr(row)
            print(f"{row_char} ", end="")

            for col in range(1, max_col + 1):
                seat = next((s for s in seats if s.row == row_char and s.col == col), None)

                if seat in current_booking_seats:
                    print("o  ", end="")
                elif seat and seat.is_booked:
                    print("#  ", end="")
                else:
                    print(".  ", end="")

            print()

        # Create column numbers
        print("  ", end="")
        for col in range(1, max_col + 1):
            print(f"{col:<3}", end="")
        print("\n")
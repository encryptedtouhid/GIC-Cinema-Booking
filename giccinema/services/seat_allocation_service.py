from giccinema.models.seat import Seat


class SeatAllocationService:
    def __init__(self, rows, seats_per_row):

        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats = self._initialize_seats()

    def _initialize_seats(self):

        seats = []
        for r in range(self.rows):
            row_char = chr(ord('A') + r)
            for c in range(1, self.seats_per_row + 1):
                seats.append(Seat(row_char, c))
        return seats

    def get_available_seats(self):

        return [seat for seat in self.seats if not seat.is_booked]

    def book_seats(self, seats, booking_id):

        for seat in seats:
            seat.book(booking_id)

    def get_default_allocation(self, num_tickets):

        available_seats = self.get_available_seats()
        if len(available_seats) < num_tickets:
            return None

        # Group seats by row
        seats_by_row = {}
        for seat in available_seats:
            if seat.row not in seats_by_row:
                seats_by_row[seat.row] = []
            seats_by_row[seat.row].append(seat)

        # Sort rows from A to Z (A is furthest from screen in the visualization)
        rows = sorted(seats_by_row.keys())

        allocated_seats = []
        tickets_left = num_tickets

        for row in rows:
            row_seats = sorted(seats_by_row[row], key=lambda s: s.col)

            if len(row_seats) >= tickets_left:
                # Find middle-most position
                middle_index = (self.seats_per_row - tickets_left) // 2
                allocated_seats.extend(row_seats[middle_index:middle_index + tickets_left])
                tickets_left = 0
                break
            else:
                # Take all available seats in this row
                allocated_seats.extend(row_seats)
                tickets_left -= len(row_seats)

        return allocated_seats if tickets_left == 0 else None

    def get_custom_allocation(self, num_tickets, start_position):
        row = start_position[0].upper()
        col = int(start_position[1:])

        available_seats = self.get_available_seats()
        if len(available_seats) < num_tickets:
            return None

        # Get seats starting from the given position
        row_seats = [s for s in available_seats if s.row == row and s.col >= col]
        row_seats = sorted(row_seats, key=lambda s: s.col)

        allocated_seats = []
        tickets_left = num_tickets

        # First, take seats in the given row
        if row_seats:
            if len(row_seats) >= tickets_left:
                allocated_seats.extend(row_seats[:tickets_left])
                tickets_left = 0
            else:
                allocated_seats.extend(row_seats)
                tickets_left -= len(row_seats)

        # If we need more seats, go to the rows closer to the screen (higher alphabetically)
        if tickets_left > 0:
            rows_closer = [chr(ord(row) + i) for i in range(1, ord('Z') - ord(row) + 1)]

            for closer_row in rows_closer:
                if tickets_left == 0:
                    break

                row_seats = [s for s in available_seats if s.row == closer_row]
                row_seats = sorted(row_seats, key=lambda s: s.col)

                if len(row_seats) >= tickets_left:
                    # Find middle-most position
                    middle_index = (self.seats_per_row - tickets_left) // 2
                    allocated_seats.extend(row_seats[middle_index:middle_index + tickets_left])
                    tickets_left = 0
                else:
                    # Take all available seats in this row
                    allocated_seats.extend(row_seats)
                    tickets_left -= len(row_seats)

        return allocated_seats if tickets_left == 0 else None

    def get_seat_by_position(self, position):
        row = position[0].upper()
        col = int(position[1:])

        for seat in self.seats:
            if seat.row == row and seat.col == col:
                return seat

        return None

    def get_seats_for_booking(self, booking_id):
         return [seat for seat in self.seats if seat.booking_id == booking_id]
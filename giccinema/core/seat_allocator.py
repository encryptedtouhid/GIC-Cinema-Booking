class SeatAllocator:
    @staticmethod
    def allocate_seats(seating_chart, num_tickets, custom_position=None):
        rows = len(seating_chart)
        seats_per_row = len(seating_chart[0])

        if custom_position:
            row_idx, col_idx = custom_position
            seats = []
            for c in range(col_idx, min(col_idx + num_tickets, seats_per_row)):
                if seating_chart[row_idx][c] != '.':
                    return []
                seats.append((row_idx, c))
            return seats

        for row_idx in range(rows - 1, -1, -1):  # Start from last row
            for col_idx in range(seats_per_row // 2 - num_tickets // 2, seats_per_row):
                if col_idx + num_tickets <= seats_per_row and all(
                        seating_chart[row_idx][c] == '.' for c in range(col_idx, col_idx + num_tickets)):
                    return [(row_idx, c) for c in range(col_idx, col_idx + num_tickets)]
        return []
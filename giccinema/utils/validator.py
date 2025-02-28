class Validator:

    @staticmethod
    def is_valid_seat_position(position, max_row, max_col):
        if len(position) < 2:
            return False

        row = position[0].upper()
        try:
            col = int(position[1:])
            return 'A' <= row <= chr(ord('A') + max_row - 1) and 1 <= col <= max_col
        except ValueError:
            return False
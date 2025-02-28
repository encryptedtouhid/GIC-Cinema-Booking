from giccinema.utils.strings_manager import StringManager


class InputService:

    def __init__(self):
        self.string_manager = StringManager()

    def get_movie_input(self):

        print(self.string_manager.MSG_INITIATE)
        while True:
            try:
                user_input = input(f"{self.string_manager.MSG_INPUT_ARROW} ")
                parts = user_input.split(maxsplit=2)

                if len(parts) != 3:
                    print(self.string_manager.MSG_INVALID_INPUT_FORMAT)
                    continue

                title = parts[0]
                rows = int(parts[1])
                seats_per_row = int(parts[2])

                if rows > 26 or rows <= 0 or seats_per_row > 50 or seats_per_row <= 0:
                    print(self.string_manager.MSG_INVALID_INPUT_FORMAT)
                    continue

                return title, rows, seats_per_row
            except ValueError:
                print(self.string_manager.MSG_INVALID_INPUT_FORMAT)

    def get_menu_selection(self):

        try:
            selection = input(f"{self.string_manager.MSG_INPUT_ARROW} ")
            return int(selection)
        except ValueError:
            return None

    def get_number_of_tickets(self):

        while True:
            user_input = input(f"{self.string_manager.MSG_INPUT_ARROW} ")
            if not user_input:
                return None

            try:
                tickets = int(user_input)
                if tickets <= 0:
                    print(self.string_manager.MSG_INVALID_NUMBER)
                    continue
                return tickets
            except ValueError:
                print(self.string_manager.MSG_INVALID_NUMBER)

    def get_seat_selection(self):

        user_input = input(f"{self.string_manager.MSG_INPUT_ARROW} ")
        if not user_input:
            return None

        return user_input.upper()

    def get_booking_id(self):

        user_input = input(f"{self.string_manager.MSG_INPUT_ARROW} ")
        if not user_input:
            return None

        return user_input.upper()
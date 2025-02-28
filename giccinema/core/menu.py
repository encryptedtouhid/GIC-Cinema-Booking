from giccinema.utils.strings_manager import StringManager


class Menu:

    def __init__(self, movie):

        self.string_manager = StringManager()
        self.movie = movie

    def display(self):

        print()
        print(self.string_manager.MSG_WELCOME)
        print(self.string_manager.OPTION_ONE.format(
            self.movie.title, self.movie.available_seats))
        print(self.string_manager.OPTION_TWO)
        print(self.string_manager.OPTION_THREE)
        print(self.string_manager.REQUEST_INPUT)
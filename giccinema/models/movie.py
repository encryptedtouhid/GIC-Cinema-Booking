class Movie:

    def __init__(self, title, rows, seats_per_row):

        self.title = title
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.total_seats = rows * seats_per_row
        self.available_seats = self.total_seats
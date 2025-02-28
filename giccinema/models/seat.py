class Seat:

    def __init__(self, row, col):
        self.row = row  # A, B, C...
        self.col = col  # 1, 2, 3...
        self.is_booked = False
        self.booking_id = None

    def book(self, booking_id):
        self.is_booked = True
        self.booking_id = booking_id

    def unbook(self):
        self.is_booked = False
        self.booking_id = None

    def __str__(self):
        return f"{self.row}{self.col:02d}"
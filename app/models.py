class Event:
    def __init__(self, id, name, date, venue, available_tickets):
        self.id = id
        self.name = name
        self.date = date
        self.venue = venue
        self.available_tickets = available_tickets

# Sample events data
events = [
    Event(1, "Rock Concert", "2024-02-15", "Main Arena", 100),
    Event(2, "Tech Conference", "2024-02-20", "Conference Hall", 150),
    Event(3, "Comedy Show", "2024-02-25", "Theater", 80),
    Event(4, "Art Exhibition", "2024-03-01", "Gallery Space", 200)
]

bookings = []
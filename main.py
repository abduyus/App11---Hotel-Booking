import pandas

df = pandas.read_csv("hotels.csv")

class Hotel:
    def __init__(self, id):
        pass

    def book(self):
        pass

    def available(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self):
        pass


print(df)
id = input("Enter the ID of the hotel: ")
hotel = Hotel(id)
if hotel.avaiable():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    reservation_ticket.generate()
else:
    print("Hotel is not free.")
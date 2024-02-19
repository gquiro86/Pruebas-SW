import unittest
from reservation import Reservation
from customer import Customer
from hotel import Hotel
#import HtmlTestRunner

class TestReservationMethods(unittest.TestCase):
    def test_create_reservation(self):
        customer = Customer("Gerardo Quiroga", "gerardo@hotmail.com.com")
        hotel = Hotel("Hotel Fiesta Inn", "Ciudad de Mexico", 100)
        reservation = Reservation(customer, hotel)
        self.assertEqual(reservation.create_reservation(), "Reservation created for Gerardo Quiroga at Hotel Fiesta Inn")

    def test_cancel_reservation(self):
        customer = Customer("Gerardo Quiroga", "gerardo@hotmail.com.com")
        hotel = Hotel("Hotel Fiesta Inn", "Ciudad de Mexico", 100)
        reservation = Reservation(customer, hotel)
        reservation.create_reservation()
        self.assertEqual(reservation.cancel_reservation(), "Reservation canceled for Gerardo Quiroga at Hotel Fiesta Inn")

if __name__ == '__main__':
    unittest.main()
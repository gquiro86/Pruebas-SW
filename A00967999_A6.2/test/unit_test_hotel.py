import unittest
from app_hotel import Hotel
import HtmlTestRunner

class TestHotelMethods(unittest.TestCase):
    def test_display_info(self):
        hotel = Hotel("Hotel Fiesta Inn", "Ciudad de Mexico", 100)
        self.assertEqual(hotel.display_info(), "Hotel: Hotel Fiesta Inn, Location: Ciudad de Mexico, Rooms: 100")

    def test_reserve_room(self):
        hotel = Hotel("Hotel Fiesta Inn", "Ciudad de Mexico", 100)
        hotel.reserve_room("Gerardo Quiroga")
        self.assertIn("Gerardo Quiroga", [customer.name for customer in hotel.reservations])

    def test_cancel_reservation(self):
        hotel = Hotel("Hotel Fiesta Inn", "Ciudad de Mexico", 100)
        hotel.reserve_room("Gerardo Quiroga")
        hotel.cancel_reservation("Gerardo Quiroga")
        self.assertNotIn("Gerardo Quiroga", [customer.name for customer in hotel.reservations])

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='hotel_reports'))

import unittest
from app.hotel import Hotel 
import HtmlTestRunner

class TestHotelMethods(unittest.TestCase):
    def test_display_info(self):
        hotel = Hotel("Hotel California", "California", 100)
        self.assertEqual(hotel.display_info(), "Hotel: Hotel California, Location: California, Rooms: 100")

    def test_reserve_room(self):
        hotel = Hotel("Hotel California", "California", 100)
        hotel.reserve_room("John Doe")
        self.assertIn("John Doe", [customer.name for customer in hotel.reservations])

    def test_cancel_reservation(self):
        hotel = Hotel("Hotel California", "California", 100)
        hotel.reserve_room("John Doe")
        hotel.cancel_reservation("John Doe")
        self.assertNotIn("John Doe", [customer.name for customer in hotel.reservations])

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='hotel_reports'))

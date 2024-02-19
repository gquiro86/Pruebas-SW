import unittest
from hotel import Hotel
from customer import Customer

class TestHotelMethods(unittest.TestCase):
    def test_display_info(self):
        hotel = Hotel("Hotel Fiesta Inn", "Ciudad de Mexico", 100)
        self.assertEqual(hotel.display_info(), "Hotel: Hotel Fiesta Inn, Location: Ciudad de Mexico, Rooms: 100")

    def test_reserve_room(self):
        hotel = Hotel("Hotel Fiesta Inn", "Ciudad de Mexico", 100)
        customer = Customer("Gerardo Quiroga", "gerardo@hotmail.com")
        hotel.reserve_room(customer)
        self.assertIn("Gerardo Quiroga", [customer.name for customer in hotel.reservations])

    def test_cancel_reservation(self):
        hotel = Hotel("Hotel Fiesta Inn Queretaro", "Queretaro", 100)
        customer = Customer("Dulce Chavez", "dulce@hotmail.com")
        hotel.reserve_room(customer)
        hotel.cancel_reservation(customer)
        self.assertNotIn("Dulce Chavez", [customer.name for customer in hotel.reservations])

    #Casos de pruebas Negativos
    def test_invalid_hotel_name(self):
        with self.assertRaises(ValueError):
            hotel = Hotel("", "Queretaro", 100)

    def test_invalid_location(self):
        with self.assertRaises(ValueError):
            hotel = Hotel("Hotel sin ubicación", "", 100)

    def test_invalid_room_number(self):
        with self.assertRaises(ValueError):
            hotel = Hotel("Hotel con valor negativo de habitaciones", "Guadalajara", -100)

    def test_invalid_reservation_cancellation(self):
        hotel = Hotel("Hotel Name", "Location", 100)
        customer = Customer("Gerardo Quiroga", "gerardo@hotmail.com")
        with self.assertRaises(ValueError):
            hotel.cancel_reservation(customer)

if __name__ == '__main__':
    unittest.main()

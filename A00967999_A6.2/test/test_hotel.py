import unittest
import os
import json
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

    #pruebas para manejo de archivos
    def setUp(self):
        self.test_filename = "test_customers.json"

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_save_customer_data(self):
        customer = Customer("John Doe", "john@example.com")
        customer.save_customer_data(self.test_filename)

        with open(self.test_filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 1)
            self.assertEqual(lines[0], "John Doe,john@example.com\n")

    def test_delete_customer_data(self):
        with open(self.test_filename, 'w', encoding='utf-8') as file:
            file.write("John Doe,john@example.com\n")
            file.write("Jane Smith,jane@example.com\n")

        customer = Customer(None, None)
        customer.delete_customer_data(self.test_filename, "John Doe")

        with open(self.test_filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 1)
            self.assertEqual(lines[0], "Jane Smith,jane@example.com\n")

    def test_load_customer_data(self):
        with open(self.test_filename, 'w', encoding='utf-8') as file:
            file.write("John Doe,john@example.com\n")
            file.write("Jane Smith,jane@example.com\n")

        customer = Customer(None, None)
        loaded_customers = customer.load_customer_data(self.test_filename)

        self.assertEqual(len(loaded_customers), 2)
        self.assertEqual(loaded_customers[0].name, "John Doe")
        self.assertEqual(loaded_customers[0].email, "john@example.com")
        self.assertEqual(loaded_customers[1].name, "Jane Smith")
        self.assertEqual(loaded_customers[1].email, "jane@example.com")

    def setUp(self):
        self.test_filename = "test_hotels.json"

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_create_hotel(self):
        hotel = Hotel("Hotel ABC", "New York", 100)
        result = hotel.create_hotel()

        self.assertEqual(result, "Hotel Hotel ABC created.")
        self.assertTrue(os.path.exists(self.test_filename))

        with open(self.test_filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["name"], "Hotel ABC")
            self.assertEqual(data[0]["location"], "New York")
            self.assertEqual(data[0]["rooms"], 100)

    def test_delete_hotel(self):
        with open(self.test_filename, 'w', encoding='utf-8') as file:
            json.dump([{"name": "Hotel ABC", "location": "New York", "rooms": 100}], file)

        hotel = Hotel("Hotel ABC", "New York", 100)
        result = hotel.delete_hotel()

        self.assertEqual(result, "Hotel Hotel ABC deleted.")

        with open(self.test_filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.assertEqual(len(data), 0)

if __name__ == '__main__':
    unittest.main()

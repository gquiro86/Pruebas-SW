import unittest
import os
from customer import Customer
#import HtmlTestRunner

class TestCustomerMethods(unittest.TestCase):
    def test_display_info(self):
        customer = Customer("Gerardo Quiroga", "gerardo@hotmail.com")
        self.assertEqual(customer.display_info(), "Customer: Gerardo Quiroga, Email: gerardo@hotmail.com")

    #Casos de pruebas Negativos
    def test_invalid_customer_name(self):
        with self.assertRaises(ValueError):
            customer = Customer("", "gerardo@hotmail.com")

    def test_invalid_email_address(self):
        with self.assertRaises(ValueError):
            customer = Customer("Gerardo Quiroga", "invalid_email")

    def test_invalid_customer_information_retrieval(self):
        customer = Customer("Gerardo Quiroga", "gerardo@hotmail.com")
        with self.assertRaises(AttributeError):
            customer.retrieve_info(None)

    def test_invalid_deletion(self):
        customer = Customer("Gerardo Quiroga", "gerardo@hotmail.com")
        with self.assertRaises(AttributeError):
            customer.delete(None)

    def test_invalid_new_name(self):
        with self.assertRaises(ValueError):
            customer = Customer("Dulce Chavez", "dulce@hotmail.com")
            customer.update_info("", "dulce@hotmail.com")

    def test_invalid_new_email(self):
        with self.assertRaises(ValueError):
            customer = Customer("Juan Perez", "juan@hotmail.com")
            customer.update_info("Juan Perez", "correonovalido")

    def test_invalid_new_name_type(self):
        with self.assertRaises(ValueError):
            customer = Customer("Tere Najera", "tere@hotmail.com")
            customer.update_info(123, "tere@hotmail.com")
    
    #Casos de Prueba para manejo de archivos:
    def setUp(self):
        self.filename = "test_customers.txt"
        # Create a test file with sample data
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write("Gerardo Quiroga,gerardo@hotmail.com\n")
            file.write("Dulce Chavez,dulce@hotmail.com\n")

    def tearDown(self):
        # Remove the test file after each test
        os.remove(self.filename)

    def test_save_customer_data(self):
        customer = Customer("Alicia Villareal", "alicia@hotmail.com")
        customer.save_customer_data(self.filename)

        # Check if the customer data is saved correctly
        with open(self.filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            self.assertIn("Alicia villareal,alicia@hotmail.com\n", lines)

    def test_delete_customer_data(self):
        customer = Customer("Gerardo Quiroga", "john@hotmail.com")
        customer.delete_customer_data(self.filename, "Gerardo Quiroga")

        # Check if the customer data is deleted correctly
        with open(self.filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            self.assertNotIn("Gerardo Quiroga,john@hotmail.com\n", lines)

    def test_load_customer_data(self):
        customer = Customer("Alicia villareal", "alicia@hotmail.com")
        customer.save_customer_data(self.filename)

        # Load customer data and check if it's loaded correctly
        loaded_customers = customer.load_customer_data(self.filename)
        self.assertIsInstance(loaded_customers, list)
        self.assertEqual(len(loaded_customers), 3)  # Including the initial 2 customers


if __name__ == '__main__':
    unittest.main()
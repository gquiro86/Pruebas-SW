import unittest
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
            customer = Customer("Dulce Chavez", "dulce@example.com")
            customer.update_info("", "dulce@example.com")

    def test_invalid_new_email(self):
        with self.assertRaises(ValueError):
            customer = Customer("Juan Perez", "juan@hotmail.com")
            customer.update_info("Juan Perez", "correonovalido")

    def test_invalid_new_name_type(self):
        with self.assertRaises(ValueError):
            customer = Customer("Tere Najera", "tere@hotmail.com")
            customer.update_info(123, "tere@hotmail.com.com")

if __name__ == '__main__':
    unittest.main()
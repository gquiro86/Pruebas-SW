import unittest
from customer import Customer
#import HtmlTestRunner

class TestCustomerMethods(unittest.TestCase):
    def test_display_info(self):
        customer = Customer("Gerardo Quiroga", "gerardo@hotmail.com")
        self.assertEqual(customer.display_info(), "Customer:Gerardo Quiroga, Email: gerardo@hotmail.com")

    def test_update_info(self):
        customer = Customer("Gerardo Quiroga", "gerardo@hotmail.com")
        customer.update_info(name="Dulce Chavez", email="dulce@hotmail.com")
        self.assertEqual(customer.name, "Dulce Chavez")
        self.assertEqual(customer.email, "dulce@hotmail.com")

if __name__ == '__main__':
    unittest.main()
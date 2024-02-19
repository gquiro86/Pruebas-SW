""" Programa para manejar clientes """


class Customer:
    """ Clase Customer """
    def __init__(self, name, email):
        if not name:
            raise ValueError("Customer name cannot be empty")
        if not isinstance(name, str):
            raise ValueError("Customer name must be a string")
        if not email or '@' not in email:
            raise ValueError("Invalid email address")
        self.name = name
        self.email = email

    def display_info(self):
        """ Mostar information """
        return f"Customer: {self.name}, Email: {self.email}"

    def update_info(self, new_name, new_email):
        """ función para actualizar información de cliente """
        if not new_name:
            raise ValueError("New name cannot be empty")
        if not isinstance(new_name, str):
            raise ValueError("New name must be a string")
        if not new_email or '@' not in new_email:
            raise ValueError("Invalid new email address")

        self.name = new_name
        self.email = new_email

    def save_customer_data(self, filename):
        """ función para guardar a un cliente """
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(f"{self.name},{self.email}\n")

    def delete_customer_data(self, filename, name):
        """ función para borrar a un cliente """
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        with open(filename, 'w', encoding='utf-8') as file:
            for line in lines:
                if line.split(',')[0] != name:
                    file.write(line)

    def load_customer_data(self, filename):
        """ función para cargar la info de los clientes """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = file.readlines()
                customers = []
                for line in data:
                    name, email = line.strip().split(',')
                    customer = Customer(name, email)
                    customers.append(customer)
                return customers
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return None

    def __str__(self):
        """ función estandar para mostrar info """
        return self.display_info()

    def __repr__(self):
        """ función estandar para regresar a cliente y su email """
        return f"Customer(name={self.name}, email={self.email})"

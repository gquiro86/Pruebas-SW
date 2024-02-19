"""Clase  Hotel"""
import json


class Hotel:
    """Clase Hotel"""
    def __init__(self, name, location, rooms):
        if not name:
            raise ValueError("Hotel name cannot be empty")
        if not location:
            raise ValueError("Location cannot be empty")
        if rooms <= 0:
            raise ValueError("Number of rooms must be positive")
        
        self.name = name
        self.location = location
        self.rooms = rooms
        self.reservations = []

    def display_info(self):
        """Clase Hotel"""
        return f"Hotel: {self.name}, Location: {self.location}, Rooms: {self.rooms}"

    def modify_info(self, name=None, location=None, rooms=None):
        """Clase Hotel"""
        if name:
            self.name = name
        if location:
            self.location = location
        if rooms:
            self.rooms = rooms

    def reserve_room(self, customer):
        """Funcion para crear una reservación"""
        if not hasattr(customer, 'name') or not isinstance(customer.name, str) or not customer.name.strip():
            raise ValueError("Customer object must have a non-empty 'name' attribute")
        self.reservations.append(customer)
        return f"Room reserved for {customer.name} at {self.name}"
    
    def cancel_reservation(self, customer):
        """Funcion para cancelar reservación"""
        if not customer:
            raise ValueError("Customer object cannot be None")
        if customer not in self.reservations:
            raise ValueError("Customer has no reservation to cancel")
        self.reservations.remove(customer)
        return f"Reservation canceled for {customer.name} at {self.name}"


    def create_hotel(self):
        """Clase Hotel"""
        try:
            with open("hotels.json", "r", encoding='utf-8') as file:
                hotels = json.load(file)
        except FileNotFoundError:
            hotels = []

        new_hotel = {"name": self.name,
                     "location": self.location,
                     "rooms": self.rooms}
        hotels.append(new_hotel)

        with open("hotels.json", "w", encoding='utf-8') as file:
            json.dump(hotels, file)

        return f"Hotel {self.name} created."

    def delete_hotel(self):
        """Clase Hotel"""
        try:
            with open("hotels.json", "r", encoding='utf-8') as file:
                hotels = json.load(file)
        except FileNotFoundError:
            return "No hotels found to delete."

        for hotel in hotels:
            if hotel["name"] == self.name:
                hotels.remove(hotel)
                with open("hotels.json", "w", encoding='utf-8') as file:
                    json.dump(hotels, file)
                return f"Hotel {self.name} deleted."

        return f"No hotel named {self.name} found."

    def __str__(self):
        """Clase Hotel"""
        return self.display_info()

    def __repr__(self):
        """Clase Hotel"""
        return f"Hotel(name={self.name}",
        f"location={self.location}, rooms={self.rooms})"

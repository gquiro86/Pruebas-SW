"""Clase  Hotel"""
import json


class Hotel:
    """Clase Hotel"""
    def __init__(self, name, location, rooms):
        self.name = name
        self.location = location
        self.rooms = rooms
        self.reservations = []

    def display_info(self):
        """Clase Hotel"""
        return f"Hotel: {self.name}",
        f"Location: {self.location}, Rooms: {self.rooms}"

    def modify_info(self, name=None, location=None, rooms=None):
        """Clase Hotel"""
        if name:
            self.name = name
        if location:
            self.location = location
        if rooms:
            self.rooms = rooms

    def reserve_room(self, customer):
        """Clase Hotel"""
        self.reservations.append(customer)
        return f"Room reserved for {customer.name} at {self.name}"

    def cancel_reservation(self, customer_name):
        """Clase Hotel"""
        for customer in self.reservations:
            if customer.name == customer_name:
                self.reservations.remove(customer)
                return f"Reservation canceled for {customer_name}",
                f"at {self.name}"
        return "Reservation not found"

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

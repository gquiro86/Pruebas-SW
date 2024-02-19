""" Programa para Manejar reservaciones """
import json


class Reservation:
    """ Clase Reservation """
    def __init__(self, customer, hotel):
        self.customer = customer
        self.hotel = hotel

    def create_reservation(self):
        """ función para crear una reservación """
        try:
            with open("reservation.json", "r", encoding='utf-8') as file:
                reservations = json.load(file)
        except FileNotFoundError:
            reservations = []

        new_reservation = {"customer": self.customer.name,
                           "hotel": self.hotel.name}
        reservations.append(new_reservation)

        with open("reservation.json", "w", encoding='utf-8') as file:
            json.dump(reservations, file)

        return f"Reservation created for {self.customer.name}, at {self.hotel.name}"

    def cancel_reservation(self):
        """ función para cancelar una reservación """
        try:
            with open("reservation.json", "r", encoding='utf-8') as file:
                reservations = json.load(file)
        except FileNotFoundError:
            return "No reservations found to cancel."

        for reservation in reservations:
            if reservation["customer"] == self.customer.name:
                if reservation["hotel"] == self.hotel.name:
                    reservations.remove(reservation)
                    with open("reservation.json", "w",
                              encoding='utf-8') as file:
                        json.dump(reservations, file)
                    return f"Reservation canceled for {self.customer.name}, at {self.hotel.name}"
        return "Reservation not found"

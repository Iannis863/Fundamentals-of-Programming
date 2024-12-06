import unittest
from Passenger import Passenger
from Plane import Plane
from Airport import Airport

class TestPassenger(unittest.TestCase):
    def test_passenger_initialization(self):
        passenger = Passenger(123456, "John", "Doe")
        self.assertEqual(passenger.get_passport_number(), 123456)
        self.assertEqual(passenger.get_first_name(), "John")
        self.assertEqual(passenger.get_last_name(), "Doe")

    def test_passenger_getters(self):
        passenger = Passenger(123456, "John", "Doe")
        self.assertEqual(passenger.get_passport_number(), 123456)
        self.assertEqual(passenger.get_first_name(), "John")
        self.assertEqual(passenger.get_last_name(), "Doe")

    def test_passenger_setters(self):
        passenger = Passenger(123456, "John", "Doe")
        passenger.set_first_name("Jane")
        passenger.set_last_name("Smith")
        passenger.set_passport_number(654321)
        self.assertEqual(passenger.get_first_name(), "Jane")
        self.assertEqual(passenger.get_last_name(), "Smith")
        self.assertEqual(passenger.get_passport_number(), 654321)

    def test_passenger_invalid_initialization(self):
        with self.assertRaises(ValueError):
            Passenger("invalid", "John", "Doe")
        with self.assertRaises(ValueError):
            Passenger(123456, 123, "Doe")
        with self.assertRaises(ValueError):
            Passenger(123456, "John", 123)

    def test_passenger_invalid_setters(self):
        passenger = Passenger(123456, "John", "Doe")
        with self.assertRaises(ValueError):
            passenger.set_first_name(123)
        with self.assertRaises(ValueError):
            passenger.set_last_name(123)
        with self.assertRaises(ValueError):
            passenger.set_passport_number("invalid")

    def test_passenger_str(self):
        passenger = Passenger(123456, "John", "Doe")
        self.assertEqual(str(passenger), "John Doe, Passport number: 123456")


class TestPlane(unittest.TestCase):
    def test_plane_initialization(self):
        plane = Plane("A123", "Airline", 100, "Destination")
        self.assertEqual(plane.get_name_or_number(), "A123")
        self.assertEqual(plane.get_airline_company(), "Airline")
        self.assertEqual(plane.get_number_of_seats(), 100)
        self.assertEqual(plane.get_destination(), "Destination")
        self.assertEqual(plane.get_passengers(), [])

    def test_plane_getters(self):
        plane = Plane("A123", "Airline", 100, "Destination")
        self.assertEqual(plane.get_name_or_number(), "A123")
        self.assertEqual(plane.get_airline_company(), "Airline")
        self.assertEqual(plane.get_number_of_seats(), 100)
        self.assertEqual(plane.get_destination(), "Destination")
        self.assertEqual(plane.get_passengers(), [])

    def test_plane_get_passengers(self):
        plane = Plane("A123", "Airline", 100, "Destination")
        passenger1 = Passenger(123456, "John", "Doe")
        passenger2 = Passenger(654321, "Jane", "Smith")
        plane.add_passenger(passenger1)
        plane.add_passenger(passenger2)
        self.assertEqual(plane.get_passengers(), [passenger1, passenger2])
        self.assertEqual(len(plane.get_passengers()), 2)
        self.assertIn(passenger1, plane.get_passengers())
        self.assertIn(passenger2, plane.get_passengers())

    def test_plane_setters(self):
        plane = Plane("A123", "Airline", 100, "Destination")
        plane.set_name_or_number("B456")
        plane.set_airline_company("New Airline")
        plane.set_number_of_seats(200)
        plane.set_destination("New Destination")
        self.assertEqual(plane.get_name_or_number(), "B456")
        self.assertEqual(plane.get_airline_company(), "New Airline")
        self.assertEqual(plane.get_number_of_seats(), 200)
        self.assertEqual(plane.get_destination(), "New Destination")

    def test_plane_invalid_initialization(self):
        with self.assertRaises(ValueError):
            Plane(1.0, "Airline", 100, "Destination")
        with self.assertRaises(ValueError):
            Plane("A123", 123, 100, "Destination")
        with self.assertRaises(ValueError):
            Plane("A123", "Airline", "invalid", "Destination")
        with self.assertRaises(ValueError):
            Plane("A123", "Airline", 100, 123)

    def test_plane_invalid_setters(self):
        plane = Plane("A123", "Airline", 100, "Destination")
        with self.assertRaises(ValueError):
            plane.set_name_or_number(123.0)
        with self.assertRaises(ValueError):
            plane.set_airline_company(123)
        with self.assertRaises(ValueError):
            plane.set_number_of_seats("invalid")
        with self.assertRaises(ValueError):
            plane.set_destination(123)

    def test_plane_add_passenger(self):
        plane = Plane("A123", "Airline", 2, "Destination")
        passenger = Passenger(123456, "John", "Doe")
        plane.add_passenger(passenger)
        self.assertEqual(len(plane.get_passengers()), 1)
        self.assertEqual(plane.get_passengers()[0].get_first_name(), "John")
        passenger = Passenger(654321, "Jane", "Smith")
        plane.add_passenger(passenger)
        self.assertEqual(len(plane.get_passengers()), 2)
        self.assertEqual(plane.get_passengers()[1].get_first_name(), "Jane")

    def test_plane_add_passenger_invalid_type(self):
        plane = Plane("A123", "Airline", 1, "Destination")
        with self.assertRaises(ValueError):
            plane.add_passenger("invalid")

    def test_plane_add_passenger_no_seats(self):
        plane = Plane("A123", "Airline", 1, "Destination")
        passenger1 = Passenger(123456, "John", "Doe")
        passenger2 = Passenger(654321, "Jane", "Smith")
        plane.add_passenger(passenger1)
        with self.assertRaises(Exception):
            plane.add_passenger(passenger2)
        self.assertEqual(len(plane.get_passengers()), 1)
        self.assertEqual(plane.get_passengers()[0].get_first_name(), "John")

    def test_plane_remove_passenger(self):
        plane = Plane("A123", "Airline", 1, "Destination")
        passenger = Passenger(123456, "John", "Doe")
        plane.add_passenger(passenger)
        plane.remove_passenger(123456)
        self.assertEqual(plane.get_passengers(), [])
        self.assertEqual(len(plane.get_passengers()), 0)
        self.assertNotIn(passenger, plane.get_passengers())

    def test_plane_remove_passenger_invalid_type(self):
        plane = Plane("A123", "Airline", 1, "Destination")
        with self.assertRaises(ValueError):
            plane.remove_passenger("invalid")

    def test_plane_update_passenger(self):
        plane = Plane("A123", "Airline", 1, "Destination")
        passenger = Passenger(123456, "John", "Doe")
        plane.add_passenger(passenger)
        plane.update_passenger(123456, "Jane", "Smith")
        self.assertEqual(passenger.get_first_name(), "Jane")
        self.assertEqual(passenger.get_last_name(), "Smith")
        self.assertEqual(passenger.get_passport_number(), 123456)

    def test_plane_update_passenger_invalid_type(self):
        plane = Plane("A123", "Airline", 1, "Destination")
        with self.assertRaises(ValueError):
            plane.update_passenger("invalid", "Jane", "Smith")
        with self.assertRaises(ValueError):
            plane.update_passenger(123456, 123, "Smith")
        with self.assertRaises(ValueError):
            plane.update_passenger(123456, "Jane", 123)

    def test_plane_sort_passengers(self):
        plane = Plane("A123", "Airline", 2, "Destination")
        passenger1 = Passenger(123456, "John", "Doe")
        passenger2 = Passenger(654321, "Jane", "Smith")
        plane.add_passenger(passenger2)
        plane.add_passenger(passenger1)
        plane.sort_passengers()
        self.assertEqual(plane.get_passengers(), [passenger1, passenger2])
        self.assertEqual(plane.get_passengers()[0].get_last_name(), "Doe")
        self.assertEqual(plane.get_passengers()[1].get_last_name(), "Smith")

    def test_plane_search_passengers_name_contains(self):
        plane = Plane("A123", "Airline", 2, "Destination")
        passenger1 = Passenger(123456, "John", "Doe")
        passenger2 = Passenger(654321, "Jane", "Smith")
        plane.add_passenger(passenger1)
        plane.add_passenger(passenger2)
        result = plane.search_passengers_name_contains("an")
        self.assertEqual(result, [passenger2])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_first_name(), "Jane")

    def test_plane_search_passengers_name(self):
        plane = Plane("A123", "Airline", 2, "Destination")
        passenger1 = Passenger(123456, "John", "Doe")
        passenger2 = Passenger(654321, "Jane", "Smith")
        plane.add_passenger(passenger1)
        plane.add_passenger(passenger2)
        self.assertTrue(plane.search_passengers_name("John", "Doe"))
        self.assertFalse(plane.search_passengers_name("Jane", "Doe"))
        self.assertTrue(plane.search_passengers_name("Jane", "Smith"))

    def test_plane_str(self):
        plane = Plane("A123", "Airline", 100, "Destination")
        self.assertEqual(str(plane), "A123 (Airline) - Destination (0/100)")

    def test_plane_update(self):
        plane = Plane("A123", "Airline", 100, "Destination")
        plane.update_plane("B456", "New Airline", 200, "New Destination")
        self.assertEqual(plane.get_name_or_number(), "B456")
        self.assertEqual(plane.get_airline_company(), "New Airline")
        self.assertEqual(plane.get_number_of_seats(), 200)
        self.assertEqual(plane.get_destination(), "New Destination")
        self.assertEqual(plane.get_passengers(), [])


class TestAirport(unittest.TestCase):
    def test_airport_initialization(self):
        airport = Airport()
        self.assertEqual(airport.get_planes(), [])
        self.assertEqual(len(airport.get_planes()), 0)
        self.assertIsInstance(airport.get_planes(), list)

    def test_airport_getter(self):
        airport = Airport()
        self.assertEqual(airport.get_planes(), [])

    def test_airport_add_plane(self):
        airport = Airport()
        plane = Plane("A123", "Airline", 100, "Destination")
        airport.add_plane(plane)
        self.assertEqual(airport.get_planes(), [plane])
        self.assertEqual(len(airport.get_planes()), 1)
        self.assertEqual(airport.get_planes()[0].get_name_or_number(), "A123")

    def test_airport_add_plane_invalid_type(self):
        airport = Airport()
        with self.assertRaises(ValueError):
            airport.add_plane("invalid")

    def test_airport_sort_passengers(self):
        airport = Airport()
        plane = Plane("A123", "Airline", 2, "Destination")
        passenger1 = Passenger(123456, "John", "Doe")
        passenger2 = Passenger(654321, "Jane", "Smith")
        plane.add_passenger(passenger2)
        plane.add_passenger(passenger1)
        airport.add_plane(plane)
        airport.sort_passengers("A123")
        self.assertEqual(plane.get_passengers(), [passenger1, passenger2])
        self.assertEqual(plane.get_passengers()[0].get_last_name(), "Doe")
        self.assertEqual(plane.get_passengers()[1].get_last_name(), "Smith")

    def test_airport_sort_passengers_invalid_type(self):
        airport = Airport()
        with self.assertRaises(ValueError):
            airport.sort_passengers(1.0)

    def test_airport_sort_passengers_plane_not_found(self):
        airport = Airport()
        with self.assertRaises(Exception):
            airport.sort_passengers("A123")

    def test_airport_sort_planes(self):
        airport = Airport()
        plane1 = Plane("A123", "Airline", 2, "Destination")
        plane2 = Plane("B456", "Airline", 2, "Destination")
        passenger1 = Passenger(123456, "John", "Doe")
        passenger2 = Passenger(654321, "Jane", "Smith")
        plane1.add_passenger(passenger1)
        plane2.add_passenger(passenger1)
        plane2.add_passenger(passenger2)
        airport.add_plane(plane2)
        airport.add_plane(plane1)
        airport.sort_planes()
        self.assertEqual(airport.get_planes(), [plane1, plane2])
        self.assertEqual(airport.get_planes()[0].get_name_or_number(), "A123")
        self.assertEqual(airport.get_planes()[1].get_name_or_number(), "B456")

    def test_airport_sort_planes_passengers_name_start(self):
        airport = Airport()
        plane1 = Plane("A123", "Airline", 2, "Destination")
        plane2 = Plane("B456", "Airline", 2, "Destination")
        passenger1 = Passenger(123456, "John", "Doe")
        passenger2 = Passenger(654321, "Jane", "Smith")
        plane1.add_passenger(passenger1)
        plane1.add_passenger(passenger2)
        plane2.add_passenger(passenger2)
        airport.add_plane(plane2)
        airport.add_plane(plane1)
        airport.sort_planes_passengers_name_start("J")
        self.assertEqual(airport.get_planes(), [plane2, plane1])
        self.assertEqual(airport.get_planes()[0].get_name_or_number(), "B456")
        self.assertEqual(airport.get_planes()[1].get_name_or_number(), "A123")

    def test_airport_sort_planes_nr_passengers_destination(self):
        airport = Airport()
        plane1 = Plane("A123", "Airline", 2, "DestinationA")
        plane2 = Plane("B456", "Airline", 2, "DestinationB")
        passenger1 = Passenger(123456, "John", "Doe")
        passenger2 = Passenger(654321, "Jane", "Smith")
        plane1.add_passenger(passenger1)
        plane2.add_passenger(passenger2)
        airport.add_plane(plane2)
        airport.add_plane(plane1)
        airport.sort_planes_nr_passengers_destination()
        self.assertEqual(airport.get_planes(), [plane1, plane2])
        self.assertEqual(airport.get_planes()[0].get_destination(), "DestinationA")
        self.assertEqual(airport.get_planes()[1].get_destination(), "DestinationB")

    def test_airport_search_plane_passenger_passport_nr_starts_with(self):
        airport = Airport()
        plane = Plane("A123", "Airline", 2, "Destination")
        passenger1 = Passenger(123456, "John", "Doe")
        passenger2 = Passenger(123789, "Jane", "Smith")
        plane.add_passenger(passenger1)
        plane.add_passenger(passenger2)
        airport.add_plane(plane)
        result = airport.search_plane_passenger_passport_nr_starts_with()
        self.assertEqual(result, [plane])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_name_or_number(), "A123")

    def test_airport_search_passenger_name_contains(self):
        airport = Airport()
        plane = Plane("A123", "Airline", 2, "Destination")
        passenger1 = Passenger(123456, "John", "Doe")
        passenger2 = Passenger(654321, "Jane", "Smith")
        plane.add_passenger(passenger1)
        plane.add_passenger(passenger2)
        airport.add_plane(plane)
        result = airport.search_passenger_name_contains("A123", "Jane")
        self.assertEqual(result, [passenger2])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_first_name(), "Jane")

    def test_airport_search_passenger_name(self):
        airport = Airport()
        plane1 = Plane("A123", "Airline", 2, "Destination")
        plane2 = Plane("B456", "Airline", 2, "Destination")
        passenger1 = Passenger(123456, "John", "Doe")
        passenger2 = Passenger(654321, "Jane", "Smith")
        plane1.add_passenger(passenger1)
        plane1.add_passenger(passenger2)
        plane2.add_passenger(passenger2)
        airport.add_plane(plane1)
        airport.add_plane(plane2)
        result = airport.search_passenger_name("John", "Doe")
        self.assertEqual(result, [plane1])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_name_or_number(), "A123")
        result = airport.search_passenger_name("Jane", "Smith")
        self.assertEqual(result, [plane1, plane2])
        self.assertEqual(len(result), 2)
        self.assertEqual(result[1].get_name_or_number(), "B456")
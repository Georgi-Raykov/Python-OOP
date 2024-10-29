from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    def __init__(self):

        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name, last_name, driving_license_number):

        for user in self.users:

            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type, brand, model, license_plate_number):

        valid_vehicles = {'PassengerCar': PassengerCar, 'CargoVan': CargoVan}

        if vehicle_type not in valid_vehicles:
            return f"Vehicle type {vehicle_type} is inaccessible."
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."
        self.vehicles.append(valid_vehicles[vehicle_type](brand, model, license_plate_number))
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point, end_point, length):

        idx = len(self.routes) + 1

        route = self.__find_route(start_point, end_point)
        if route:
            if route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            elif route.length > length:
                route.is_locked = True

        new_route = Route(start_point, end_point, length, route_id=idx)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number, license_plate_number, route_id, is_accident_happened):

        user = self.__find_user_by_license_number(driving_license_number)
        vehicle = self.__find_vehicle_by_plate_number(license_plate_number)
        route = self.__find_route_by_route_id(route_id)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed!"
        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()
        return str(vehicle)

    def repair_vehicles(self, count):

        damaged_vehicles = [damaged for damaged in self.vehicles if damaged.is_damaged]

        sorted_vehicles = sorted(damaged_vehicles, key=lambda vehicle: (vehicle.brand, vehicle.model))[:count]

        for vehicle in sorted_vehicles:
            vehicle.is_damaged = False
            vehicle.battery_level = 100

        return f"{len(damaged_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda u: -u.rating)
        result = "*** E-Drive-Rent ***\n"

        for user in sorted_users:
            result += str(user) + '\n'
        return result

    def __find_user_by_license_number(self, license_number):

        for user in self.users:
            if user.driving_license_number == license_number:
                return user
        return None

    def __find_vehicle_by_plate_number(self, plate_number):

        for vehicle in self.vehicles:
            if vehicle.license_plate_number == plate_number:
                return vehicle
        return None

    def __find_route_by_route_id(self, route_id):
        for route in self.routes:
            if route.route_id == route_id:
                return route
        return None

    def __find_route(self, start, end):

        for route in self.routes:
            if route.start_point == start and route.end_point == end:
                return route

        return None

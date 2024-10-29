from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):

    def __init__(self, brand, model, license_plate_number):
        super().__init__(brand, model, license_plate_number, max_mileage=450.00)

    def drive(self, mileage):

        percentage_reduce = round((mileage * 100) / self.max_mileage)
        self.battery_level -= percentage_reduce

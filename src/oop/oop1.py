# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    pass
# base class (has sub classes FlightVehicle and GroundVehicle)


class FlightVehicle(Vehicle):
    pass
# (has sub classes Airplane and Starship)


class GroundVehicle(Vehicle):
    pass
# (has sub classes Car and Motorcycle)


class Airplane(FlightVehicle):
    pass


class Starship(FlightVehicle):
    pass


class Car(GroundVehicle):
    pass


class Motorcycle(GroundVehicle):
    pass

from package import get_truck3, get_truck1, get_truck2, truck_1
import csv
import datetime




# Truck class
class Truck:

    def __init__(self, capacity, speed, load, depart, packages):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.depart = depart
        self.packages = packages

    # def insert(self, package):r

    def __str__(self):
        return "%s, %s, %s, %s, %s" % (self.capacity, self.speed, self.load, self.depart, self.packages)


# reads distance file and stores distances in 2D array
distance_data = list(csv.reader(open("DistanceTable.csv"), delimiter=','))
# reads address file and stores addresses in 2D array
address_data = list(csv.reader(open('AddressFile.csv'), delimiter=','))


# function to get address data
def lookup_address(address):
    for i, row in enumerate(address_data):
        if address in row[2]:
            return int(row[0])
    print('Address not found', address)


# function to get total mileage
def get_mileage_total(row, column, mileage_total):
    mileage = distance_data[row][column]
    if mileage == '':
        mileage = distance_data[column][row]
    return mileage_total + float(mileage)


# function to get mileage for each delivery
def get_mileage(row, column):
    mileage = distance_data[row][column]
    if mileage == '':
        mileage = distance_data[column][row]
    return float(mileage)


# truck departure times
truck1_depart = datetime.time(8, 0, 0)
truck2_depart = datetime.time(9, 5, 0)
truck3_depart = datetime.time(11, 0, 0)


truck1_load = Truck(16, 18, True, datetime.time(8, 0, 0), truck_1)
truck2_load = Truck(16, 18, True, datetime.time(9, 5, 0), get_truck2())
truck3_load = Truck(16, 18, True, truck3_depart, get_truck3())

print("\nTruckLoads\n", truck1_load.packages, "\n", truck2_load.depart, "\n", truck3_load)
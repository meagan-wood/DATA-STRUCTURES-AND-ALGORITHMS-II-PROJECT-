from package import get_truck3, get_truck1, get_truck2, truck_1, myHash
import csv
import datetime


# Truck class
class Truck:

    def __init__(self, capacity, speed, load, depart, packages):
        self.capacity = capacity
        self.speed = 3.3  # 18mph = 3.3 mins per mile
        self.load = load
        self.depart = self.time = depart
        self.packages = packages
        self.current_location = 0
        self.total_mileage = 0.0

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
truck1_depart = datetime.timedelta(hours=8, minutes=0, seconds=0)
truck2_depart = datetime.timedelta(hours=9, minutes=5, seconds=0)
truck3_depart = datetime.timedelta(hours=11, minutes=0, seconds=0)

truck1_load = Truck(16, 18, True, truck1_depart, get_truck1())
truck2_load = Truck(16, 18, True, truck2_depart, get_truck2())
truck3_load = Truck(16, 18, True, truck3_depart, get_truck3())


def get_closest_distance(truck):
    min_mileage = 50.0
    location = 0
    for i in truck.packages:
        package = myHash.search(i)
        value = lookup_address(package.address)
        if get_mileage(truck.current_location, value) <= min_mileage:
            min_mileage = get_mileage(truck.current_location, value)
            location = value

    truck.current_location = location
    delivery_duration = min_mileage * truck.speed
    truck.time = truck.time + datetime.timedelta(minutes=delivery_duration)  # adds the trip mins to the truck.time
    truck.total_mileage += min_mileage
    for i in truck.packages:
        package = myHash.search(i)
        if location == lookup_address(package.address):
            package.departure_time = truck.depart
            package.delivery_time = truck.time
            package.status = "delivered"
            truck.packages.remove(i)
    # print("\nID", package.id, "\nTripMileage", min_mileage, "\nTruckMileage", truck.total_mileage, "\nTime",
    #               truck.time)


while truck1_load.packages:
    get_closest_distance(truck1_load)
while truck2_load.packages:
    get_closest_distance(truck2_load)
while truck3_load.packages:
    get_closest_distance(truck3_load)


def total_mileage():
    mileage = "{0:.2f}".format(truck1_load.total_mileage + truck2_load.total_mileage +
                               truck3_load.total_mileage, 2)
    return mileage


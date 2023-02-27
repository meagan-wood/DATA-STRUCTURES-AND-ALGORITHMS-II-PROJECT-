from package import get_truck3, get_truck1, get_truck2, truck_1, myHash, truck_2, truck_3
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
# def get_mileage_total(row, column, mileage_total):
#     mileage = distance_data[row][column]
#     if mileage == '':
#         mileage = distance_data[column][row]
#     return mileage_total + float(mileage)


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

truck1_packages = []
truck2_packages = []
truck3_packages = []


# function that add the packages to a new list after they are delivered
def delivered_packages(package):
    if package in truck1_load.packages:
        truck1_packages.append(package)
    elif package in truck2_load.packages:
        truck2_packages.append(package)
    elif package in truck3_load.packages:
        truck3_packages.append(package)
    return package


# Nearest Neighbor algorithm.
# Sets initial mileage and location.
# Iterates through the packages, storing the address for the package and the location.
# Mileage updates as truck moves to new location.
# Location updates to current location as truck moves.
# Calculates the trip time using the trip mileage and multiplying it by truck speed(3.3) since it takes 3.3 minutes for
# every mile traveled if moving at 18mph and adds that to the trucktime.
# Miles traveled gets added to the total miles for the truck as it travels to each address.
# If the location matches the package address then the package status is updated to delivered, the time is stored
# as delivery time and that package is moved from the truck list and added to a truck delivered list to be used
# in the UI.
# This will loop through for each truck until the list is empty and then move to the next truck until all trucks
# are empty.
#
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
            package.status = "DELIVERED"
            delivered_packages(i)
            truck.packages.remove(i)


while truck1_load.packages:
    get_closest_distance(truck1_load)
while truck2_load.packages:
    get_closest_distance(truck2_load)
while truck3_load.packages:
    get_closest_distance(truck3_load)


# Function to get the total miles traveled from all the trucks after all packages are delivered.
def total_mileage():
    mileage = "{0:.2f}".format(truck1_load.total_mileage + truck2_load.total_mileage +
                               truck3_load.total_mileage, 2)
    return mileage

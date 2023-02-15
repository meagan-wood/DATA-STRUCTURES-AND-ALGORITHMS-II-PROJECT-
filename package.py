# Package class
import csv
import datetime

from hashTable import HashTable


class Package:
    def __init__(self, package_id, address, city, state, zipcode, deadline, mass, special, status):
        self.id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.mass = mass
        self.special = special
        self.status = status
        self.delivery_time = None
        self.departure_time = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city,
                                                       self.state, self.zipcode, self.deadline,
                                                       self.mass, self.special, self.status)


truck_1 = []
truck_2 = []
truck_3 = []


# function to read package data, create package object, sort packages into truck lists, returns truck lists
def read_package_data(filename):
    with open(filename) as package_file:
        package_data = csv.reader(package_file, delimiter=',')
        next(package_data)

        for packages in package_data:
            p_id = int(packages[0])
            p_address = packages[1]
            p_city = packages[2]
            p_state = packages[3]
            p_zipcode = packages[4]
            p_deadline = packages[5]
            p_mass = packages[6]
            p_special = packages[7]
            p_status = "At Hub"
            # package.append(p_status)
            p = Package(p_id, p_address, p_city, p_state, p_zipcode, p_deadline, p_mass, p_special, p_status)
            myHash.insert(p_id, p)
            if p.id in [15, 19]:
                truck_1.append(p.id)
                continue
            if p.deadline == '10:30 AM' and 'none' in p.special:
                truck_1.append(p.id)
            if 'Must be' in p.special:
                truck_1.append(p.id)
            if p.deadline == '10:30 AM' and 'Delayed' in p.special:
                truck_2.append(p.id)
            if 'Delayed' in p.special and p.deadline == 'EOD':
                truck_2.append(p.id)
            if p.deadline == 'EOD' and 'Must be' in p.special or 'Can only be' in p.special:
                truck_2.append(p.id)
            if p.id == 9:
                truck_3.append(p.id)
                continue
            if p.deadline == 'EOD' and 'none' in p.special:
                if len(truck_3) < 16:
                    truck_3.append(p.id)
                else:
                    truck_2.append(p.id)


myHash = HashTable()

read_package_data('PackageFile.csv')

print("\nTruck1", truck_1)
print("\nTruck2", truck_2)
print("\nTruck3", truck_3)


# function to read package data from hashtable
def get_package_data():
    print("PackageFile from Hashtable")
    for i in range(len(myHash.table) + 1):
        print("Key: {} and Package: {}".format(i + 1, myHash.search(i + 1)))


# function to get packages for truck one
def get_truck1():
    return truck_1


# function to get packages for truck two
def get_truck2():
    return truck_2


# function to get packages for truck three
def get_truck3():
    return truck_3

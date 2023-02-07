# Package class
import csv

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

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city,
                                                       self.state, self.zipcode, self.deadline,
                                                       self.mass, self.special, self.status)


def read_package_data(filename):
    with open(filename) as package_file:
        package_data = csv.reader(package_file, delimiter=',')
        next(package_data)
        truck_1 = []
        truck_2 = []
        truck_3 = []
        for package in package_data:
            p_id = int(package[0])
            p_address = package[1]
            p_city = package[2]
            p_state = package[3]
            p_zipcode = package[4]
            p_deadline = package[5]
            p_mass = package[6]
            p_special = package[7]
            p_status = "At Hub"

            package = (p_id, p_address, p_city, p_state, p_zipcode, p_deadline, p_mass, p_special, p_status)

            if package[0] == 15:
                truck_1.append(p_id)
            if package[5] == '10:30 AM' and 'none' in package[7]:
                truck_1.append(p_id)
            if package[0] == 19:
                truck_1.append(p_id)
            if 'Must be' in package[7]:
                truck_1.append(p_id)
            if package[5] == '10:30 AM' and 'Delayed' in package[7]:
                truck_2.append(p_id)
            if 'Delayed' in package[7] and package[5] == 'EOD':
                truck_2.append(p_id)
            if package[5] == 'EOD' and 'Must be' in package[7] or 'Can only be' in package[7]:
                truck_2.append(p_id)
            if package[0] == 9:
                truck_3.append(p_id)
            if package[5] == 'EOD' and 'none' in package[7]:
                if len(truck_3) < 17:
                    truck_3.append(p_id)
                else:
                    truck_2.append(p_id)

            myHash.insert(p_id, package)
    print("\nTruck1")
    print(truck_1)
    print("\nTruck2")
    print(truck_2)
    print("\nTruck3")
    print(truck_3)


myHash = HashTable()

read_package_data('PackageFile.csv')


def get_package_data():
    print("PackageFile from Hashtable")
    for i in range(len(myHash.table) + 1):
        print("Key: {} and Package: {}".format(i + 1, myHash.search(i + 1)))


# assigns packages to trucks
# 15 deliver by 9:00, others 10:30
# truck_1 = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
# truck_1_priority = [15]


# 6, 25 deliver by 10:30, others EOD
# truck_2 = [3, 6, 18, 22, 23, 24, 25, 26, 27, 28, 32, 33, 35, 36, 38, 39]
# truck_2_priority = [6, 25]

# deliver by EOD, 9 wrong address deliver after 10:20
# truck_3 = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 21]


# function to get packages for truck one
def get_truck1():
    return truck_1


# function to get packages for truck two
def get_truck2():
    return truck_2


# function to get packages for truck three
def get_truck3():
    return truck_3

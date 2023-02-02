import csv

import numpy as numpy


class Truck:

    def __init__(self, capacity, speed, load, packages):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages

    # def insert(self, package):

    def __str__(self):
        return "%s, %s, %s, %s" % (self.capacity, self.speed, self.load, self.packages)


# distance_data = list(csv.reader(open('DistanceTable.csv'), delimiter=','))
distance_data = open("DistanceTable.csv")
distance_2dlist = numpy.genfromtxt(distance_data, delimiter=",")

address_data = list(csv.reader(open('AddressFile.csv'), delimiter=','))


def lookup_address():
    return address_data


def get_mileage_total(row, column, mileage_total):
    mileage = distance_2dlist[row][column]
    if mileage == '':
        mileage = distance_2dlist[column][row]
    return mileage_total + float(mileage)


def get_mileage(row, column):
    mileage = distance_2dlist[row][column]
    if mileage == '':
        mileage = distance_2dlist[column][row]
    return float(mileage)

class Truck:

    def __init__(self, capacity, speed, load, packages):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages

    # def insert(self, package):

    def __str__(self):
        return "%s, %s, %s, %s" % (self.capacity, self.speed, self.load, self.packages)


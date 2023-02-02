from hashTable import myHash, read_package_data
from truck import distance_data, address_data, distance_2dlist

for i in range(len(myHash.table) + 1):
    print("Key: {} and Package: {}".format(i + 1, myHash.search(i + 1)))

print("\nSearch:")
print(myHash.search(22))
print(myHash.search(37))

print("\nDistance:")
# print(distance_data[3][2])
print(distance_2dlist[1][1])
print("\nAddress:")
print(address_data)

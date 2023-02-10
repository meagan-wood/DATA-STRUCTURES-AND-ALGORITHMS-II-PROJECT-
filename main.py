from package import myHash, read_package_data, get_package_data
from truck import distance_data, address_data, lookup_address, get_mileage

print("\nSearch:")
print(myHash.search(22))
print(myHash.search(37))

print("\nDistance:")
# print(distance_data[3][2])
truck1_address = '4001 South 700 East'
package = myHash.search(25)
# print(distance_2dlist[lookup_address(truck1_address)][lookup_address(package.address)])
print(get_mileage(lookup_address(truck1_address), lookup_address(package.address)))
print("\nAddress:")
print(address_data)
print("\nPackageData:")

get_package_data()

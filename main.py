from package import myHash, get_package_data
from truck import lookup_address, get_mileage, truck1_depart, truck2_depart, truck3_depart

print("\nSearch:")
print(myHash.search(22))
print(myHash.search(37))

print("\nDistance:")
# print(distance_data[3][2])
truck1_address = '4001 South 700 East'
package = myHash.search(25)
print(get_mileage(lookup_address(truck1_address), lookup_address(package.address)))

get_package_data()

print("\nDepart", truck1_depart, truck2_depart, truck3_depart)

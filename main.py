# Meagan Wood ID: 000933763
# mwoo195@wgu.edu

import truck
from package import myHash, get_package_data, get_truck2
from truck import lookup_address, get_mileage

# print("\nSearch:")
# print(myHash.search(15))
print(myHash.search(9))


#
# print("\nDistance:")
# truck1_address = '4001 South 700 East'
# package = myHash.search(25)
# print(get_mileage(lookup_address(truck1_address), lookup_address(package.address)))
# def time_lookup():


def app():
    print('\nWelcome to the WGUPS!')
    print('\nThe total mileage to deliver all packages:', truck.total_mileage(), 'miles.')
    selection = input("\nHow can I help? Please enter the number associated with the task you'd like to complete: \n"
                      "1 - Lookup package using the package ID \n"
                      "2 - Check status of packages at a specific time \n"
                      "0 - To exit the program \n")
    if selection == "1":
        enter_id = input("Please enter the package ID:")
        convert_id = int(enter_id)
        package_info = myHash.search(convert_id)
        print(package_info)

    if selection == "2":
        print("2")

    else:
        print("Thanks for choosing WGUPS! Goodbye")


app()

# Meagan Wood ID: 000933763
# mwoo195@wgu.edu
import datetime
from datetime import datetime, timedelta

import package
import truck
from package import myHash


# print("\nSearch:")
# print(myHash.search(15))
# print(myHash.search(9))

# def time_lookup_1(truck):
#     truck_packages = truck.packages
#     for i in truck.packages:
#         package = myHash.search(i)
#         time = package.delivery_time
#         if delta > time:
#             print(package.id, time)

# UI to get package information when user enters package ID, or a specific time.
# Entering a package ID will return all the information for that specified package.
# Entering a time will return all truck and package statuses,
# if the package has been delivered will return the delivery time with the package ID.
# Error handling for invalid entries or format
def app():
    print('\nWelcome to the WGUPS!')
    print('\nThe total mileage to deliver all packages:', truck.total_mileage(), 'miles.')
    # gets user input
    selection = input("\nHow can I help? Please enter the number associated with the task you'd like to complete: \n"
                      "1 - Lookup package using the package ID \n"
                      "2 - Check status of packages at a specific time \n"
                      "0 - To exit the program \n")
    if selection == "1":
        enter_id = int(input("Please enter the package ID:"))
        package_info = myHash.search(enter_id)  # searches hash table using enter_id
        print("PackageID:", package_info.id, "\nAddress:", package_info.address, package_info.city, package_info.state,
              package_info.zipcode, "\nDeadline:", package_info.deadline, "\nMass:", package_info.mass,
              "\nNotes:", package_info.special, "\nStatus:", package_info.status, "\nTime Delivered:",
              package_info.delivery_time)

    elif selection == "2":
        try:
            entered_time = input(
                "Please enter the time you wish to search using the 'HH:MM:SS' format:")  # getting user input
            convert_time = datetime.strptime(entered_time, "%H:%M:%S")  # converting user input to datetime
            input_time = timedelta(hours=convert_time.hour, minutes=convert_time.minute,
                                   seconds=convert_time.second)  # converting time to timedelta
            print("\nTime Entered:", input_time)
            if input_time < truck.truck1_depart:
                print("\nTrucks are still at the hub.", "\nTruck 1 departs at:", truck.truck1_depart,
                      "\nTruck 2 departs at:", truck.truck2_depart, "\nTruck 3 departs at:", truck.truck3_depart)
            elif input_time > truck.truck1_depart:
                if input_time < truck.truck2_depart:
                    print("\nTruck 1 is en route", "\nStatus of packages", )
                    for count in range(1, 41):
                        package_i = myHash.search(count)  # searching myHash
                        time = package_i.delivery_time  # getting delivery time of package
                        if input_time > time:  # comparing input time to delivery time of package
                            print("Package:", package_i.id, "Delivered at:", time)
                            truck.truck1_packages.remove(package_i.id)  # removing the package from truck package list
                    print("\nTruck 1 packages still in route", truck.truck1_packages)
                    print("\nTruck 2 will depart at:", truck.truck2_depart, "\nTruck 3 will depart at:",
                          truck.truck3_depart)
                elif input_time == truck.truck2_depart:
                    print("\nTruck 2 is now leaving the hub, no packages from truck 2 have been delivered yet.")
                    print("\nTruck 1 is en route", "\nStatus of packages", )
                    for count in range(1, 41):
                        package_i = myHash.search(count)
                        time = package_i.delivery_time
                        if input_time > time:
                            print("Package:", package_i.id, "Delivered at:", time)
                            truck.truck1_packages.remove(package_i.id)
                    print("\nTruck 1 packages still in route", truck.truck1_packages)
                    print("\nTruck 2 packages are now in route:", truck.truck2_packages)
                    print("\nTruck 3 will depart at:", truck.truck3_depart)
                elif input_time < truck.truck3_depart:
                    print("Complete")

            else:
                print("Unable to get truck status for that time")

        except ValueError as e:
            print("Invalid time format, time must be entered in 'HH:MM:SS' format. Goodbye.")
            print(e)
            # exit()

    elif selection == "0":
        print("Thanks for choosing WGUPS! Goodbye")

    else:
        print("Invalid selection, please try again. Goodbye.")


app()

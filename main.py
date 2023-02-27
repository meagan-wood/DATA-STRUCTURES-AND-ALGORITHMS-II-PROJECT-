#
# NHP2 — NHP2 TASK 1: WGUPS ROUTING PROGRAM
# DATA STRUCTURES AND ALGORITHMS II — C950
# Meagan Wood
# ID: 000933763
# mwoo195@wgu.edu
#
#
import datetime
from datetime import datetime, timedelta
import package
import truck
from package import myHash


# UI to get package information when user enters package ID, or a specific time.
# Entering a package ID will return all the information for that specified package.
# Entering a time will return all trucks and packages' status,
# If the package has been delivered, will return the delivery time with the package ID.
# Error handling for invalid entries or format.
def app():
    print('\nWelcome to the WGUPS!')
    print("\nDeparture times and packages assigned to each truck:", "\nTruck 1:", truck.truck1_depart,
          truck.truck1_packages, "\nTruck 2:", truck.truck2_depart, truck.truck2_packages,
          "\nTruck 3:", truck.truck3_depart, truck.truck3_packages)
    print('\nThe total mileage to deliver all packages:', truck.total_mileage(), 'miles.')
    # Option choices for user, gets user input
    selection = input("\nHow can I help? Please enter the number associated with the task you'd like to complete: \n"
                      "1 - Lookup package status and info using the package ID and time \n"
                      "2 - Check status of packages at a specific time \n"
                      "3 - View all packages with their delivery time and package information \n"
                      "0 - To exit the program \n")
    if selection == "1":
        enter_id = int(input("Please enter the package ID:"))
        package_info = myHash.search(enter_id)  # searches hash table using enter_id
        # Provides all package info the user searched for
        if package_info is None:
            print("\nERROR:", "\nPackage ID:", enter_id, "not found. Please try again.")
        else:
            entered_time = input("Please enter the time using Military Time in the 'HH:MM' format:")
            convert_time = datetime.strptime(entered_time, "%H:%M")  # converting user input to datetime
            input_time = timedelta(hours=convert_time.hour, minutes=convert_time.minute)  # converting time to timedelta
            if input_time < package_info.departure_time:  # comparing input time to package depart time
                package_info.status = "AT HUB"  # updating status if input time < departure time
                # printing package information for given time
                print("PackageID:", package_info.id, "\nAddress:", package_info.address, package_info.city,
                      package_info.state, package_info.zipcode, "\nDeadline:", package_info.deadline, "\nMass:",
                      package_info.mass, "\nNotes:", package_info.special, "\nStatus:", package_info.status)
            elif input_time > package_info.departure_time:
                if input_time < package_info.delivery_time:
                    package_info.status = "EN ROUTE"  # updating status if input time > departure time < delivery time
                    # printing package information for given time
                    print("PackageID:", package_info.id, "\nAddress:", package_info.address, package_info.city,
                          package_info.state, package_info.zipcode, "\nDeadline:", package_info.deadline, "\nMass:",
                          package_info.mass, "\nNotes:", package_info.special, "\nStatus:", package_info.status)
                else:
                    # if input time is greater than delivery time, prints package info w/delivery time
                    print("PackageID:", package_info.id, "\nAddress:", package_info.address, package_info.city,
                          package_info.state, package_info.zipcode, "\nDeadline:", package_info.deadline, "\nMass:",
                          package_info.mass, "\nNotes:", package_info.special, "\nStatus:", package_info.status,
                          "\nTime Delivered:", package_info.delivery_time)

    elif selection == "2":
        try:
            entered_time = input \
                ("Please enter the time using Military Time in the 'HH:MM' format:")  # getting user input
            convert_time = datetime.strptime(entered_time, "%H:%M")  # converting user input to datetime
            input_time = timedelta(hours=convert_time.hour, minutes=convert_time.minute)  # converting time to timedelta
            print("\nTime Entered:", input_time)  # displaying the time the user entered
            if input_time < truck.truck1_depart:  # comparing time with truck depart time displays truck depart times
                print("\nTrucks and ALL packages are still at the hub.", "\nTruck 1 departs at", truck.truck1_depart,
                      "and contains the following packages", truck.truck1_packages,
                      "\nTruck 2 departs at", truck.truck2_depart, "and contains the following packages",
                      truck.truck2_packages, "\nTruck 3 departs at", truck.truck3_depart,
                      "and contains the following packages", truck.truck3_packages)
            elif input_time == truck.truck1_depart:
                print("\nTruck 1 is now leaving the hub.")
                print("\nPakages 'EN ROUTE' on truck 1:", truck.truck1_packages)
                print("\nTruck 2 will depart at", truck.truck2_depart, "packages 'AT HUB'", truck.truck2_packages,
                      "\nTruck 3 will depart at", truck.truck3_depart, "packages 'AT HUB'", truck.truck3_packages)
            elif input_time > truck.truck1_depart < truck.truck2_depart:
                if input_time < truck.truck2_depart:  # checking input time with truck times
                    print("\nPackages delivered:\n")
                    for count in range(1, 41):  # comparing time to delivery times to return status/times of packages
                        package_i = myHash.search(count)  # searching myHash
                        time = package_i.delivery_time  # getting delivery time of package
                        if input_time > time:  # comparing input time to delivery time of package
                            print("PackageID:", package_i.id, "\nAddress:", package_i.address, package_i.city,
                                  package_i.state, package_i.zipcode, "\nDeadline:", package_i.deadline,
                                  "\nMass:", package_i.mass, "\nNotes:", package_i.special, "\nStatus:",
                                  package_i.status,
                                  "\nTime Delivered:", package_i.delivery_time, "\n")
                            truck.truck1_packages.remove(package_i.id)  # removing the package from truck package list
                    print("\nTruck 1 packages still 'EN ROUTE'", truck.truck1_packages)
                    print("\nTruck 2 will depart at", truck.truck2_depart, "packages 'AT HUB'", truck.truck2_packages,
                          "\nTruck 3 will depart at", truck.truck3_depart, "packages 'AT HUB'", truck.truck3_packages)
                elif input_time == truck.truck2_depart:
                    print("\nTruck 2 is now leaving the hub.")
                    print("\nPackages delivered:\n")
                    # iterating through packages comparing time to delivery times to return status of packages
                    for count in range(1, 41):
                        package_i = myHash.search(count)
                        time = package_i.delivery_time
                        if input_time > time:
                            print("PackageID:", package_i.id, "\nAddress:", package_i.address, package_i.city,
                                  package_i.state, package_i.zipcode, "\nDeadline:", package_i.deadline,
                                  "\nMass:", package_i.mass, "\nNotes:", package_i.special, "\nStatus:",
                                  package_i.status, "\nTime Delivered:", package_i.delivery_time, "\n")
                            truck.truck1_packages.remove(package_i.id)  # removing the package from truck package list
                    print("\nTruck 1 packages still 'EN ROUTE'", truck.truck1_packages)
                    print("\nTruck 2 is just leaving the hub, packages are now 'EN ROUTE'", truck.truck2_packages)
                    print("\nTruck 3 will depart at", truck.truck3_depart, "packages 'AT HUB':", truck.truck3_packages)
                elif input_time > truck.truck2_depart:
                    if input_time < truck.truck3_depart:
                        print("\nPackages delivered:\n")
                        for count in range(1, 41):
                            package_i = myHash.search(count)  # searching myHash
                            time = package_i.delivery_time  # getting delivery time of package
                            if input_time > time:  # comparing input time to delivery time of package
                                print("PackageID:", package_i.id, "\nAddress:", package_i.address, package_i.city,
                                      package_i.state, package_i.zipcode, "\nDeadline:", package_i.deadline,
                                      "\nMass:", package_i.mass, "\nNotes:", package_i.special, "\nStatus:",
                                      package_i.status, "\nTime Delivered:", package_i.delivery_time, "\n")
                                # removing the package from the package list where it is found
                                if package_i.id in truck.truck1_packages:
                                    truck.truck1_packages.remove(package_i.id)
                                elif package_i.id in truck.truck2_packages:
                                    truck.truck2_packages.remove(package_i.id)
                        # displaying status of packages/trucks
                        print("\nTruck 1 packages still 'EN ROUTE'", truck.truck1_packages)
                        print("\nTruck 2 packages still 'EN ROUTE'", truck.truck2_packages)
                        print("\nTruck 3 will depart at", truck.truck3_depart, "packages 'AT HUB':",
                              truck.truck3_packages)

                    if input_time == truck.truck3_depart: # checking input time is equal to truck 3 depart time
                        print("\nTruck 3 is now leaving the hub.")
                        print("\nPackages delivered:\n")
                        # iterating through packages compares input time to delivery time
                        for count in range(1, 41):
                            package_i = myHash.search(count)  # searching myHash
                            time = package_i.delivery_time  # getting delivery time of package
                            if input_time > time:  # comparing input time to delivery time of package
                                print("PackageID:", package_i.id, "\nAddress:", package_i.address, package_i.city,
                                      package_i.state, package_i.zipcode, "\nDeadline:", package_i.deadline,
                                      "\nMass:", package_i.mass, "\nNotes:", package_i.special, "\nStatus:",
                                      package_i.status, "\nTime Delivered:", package_i.delivery_time, "\n")
                                # removing the package from associated list
                                if package_i.id in truck.truck1_packages:
                                    truck.truck1_packages.remove(package_i.id)
                                elif package_i.id in truck.truck2_packages:
                                    truck.truck2_packages.remove(package_i.id)
                                elif package_i.id in truck.truck3_packages:
                                    truck.truck3_packages.remove(package_i.id)
                        # prints packages on truck 3 updating truck to en route, prints truck 1 and 2 completed route
                        # and mileage for each truck
                        print("\nTruck 3 packages now 'EN ROUTE'", truck.truck3_packages)
                        print("\nTruck 1 completed all deliveries:", truck.truck1_packages,
                              "\nTotal miles for Truck 1:", "{0:.2f}".format(truck.truck1_load.total_mileage, 2))
                        print("\nTruck 2 completed all deliveries:", truck.truck2_packages,
                              "\nTotal miles for Truck 2:", "{0:.2f}".format(truck.truck2_load.total_mileage, 2))
                    if input_time > truck.truck3_depart:  # comparing input time to truck 3 depart time
                        print("\nPackages delivered:")
                        # iterating through packages compares input time to delivery time
                        for count in range(1, 41):
                            package_i = myHash.search(count)  # searching for package using myHash search
                            time = package_i.delivery_time  # getting delivery time of package
                            if input_time > time:  # comparing input time to delivery time of package
                                # prints packages delivered with delivery time
                                print("PackageID:", package_i.id, "\nAddress:", package_i.address, package_i.city,
                                      package_i.state, package_i.zipcode, "\nDeadline:", package_i.deadline,
                                      "\nMass:", package_i.mass, "\nNotes:", package_i.special, "\nStatus:",
                                      package_i.status, "\nTime Delivered:", package_i.delivery_time, "\n")
                                # removing the package from associated list
                                if package_i.id in truck.truck1_packages:
                                    truck.truck1_packages.remove(package_i.id)
                                elif package_i.id in truck.truck2_packages:
                                    truck.truck2_packages.remove(package_i.id)
                                elif package_i.id in truck.truck3_packages:
                                    truck.truck3_packages.remove(package_i.id)
                        if len(truck.truck3_packages) == 0:  # if truck3 package list is empty
                            # prints each truck completed route and mileage for each truck as well as combined mileage
                            # for all trucks
                            print("\nTruck 1 completed all deliveries:", truck.truck1_packages,
                                  "\nTotal miles for Truck 1:", "{0:.2f}".format(truck.truck1_load.total_mileage, 2))
                            print("\nTruck 2 completed all deliveries:", truck.truck2_packages,
                                  "\nTotal miles for Truck 2:", "{0:.2f}".format(truck.truck2_load.total_mileage, 2))
                            print("\nTruck 3 completed all deliveries:", truck.truck3_packages,
                                  "\nTotal miles for Truck 3:", "{0:.2f}".format(truck.truck3_load.total_mileage, 2))
                            print("\nTotal miles for all trucks:", truck.total_mileage())
                        else:
                            # if truck3 package list is not empty, prints packages still en route on truck 3 and
                            # that truck 1 and 2 have completed route and provides individual truck mileage
                            print("\nTruck 3 packages still 'EN ROUTE':", truck.truck3_packages)
                            print("\nTruck 1 completed all deliveries:", truck.truck1_packages,
                                  "\nTotal miles for Truck 1:", "{0:.2f}".format(truck.truck1_load.total_mileage, 2))
                            print("\nTruck 2 completed all deliveries:", truck.truck2_packages,
                                  "\nTotal miles for Truck 2:", "{0:.2f}".format(truck.truck2_load.total_mileage, 2))

            else:
                print("Unable to get truck status for that time. Please try again.")
        # Error handling
        except ValueError as e:
            print("\nERROR:", "\nInvalid time format, time must be MILITARY TIME (24hr clock) entered in 'HH:MM' "
                              "format. Goodbye.")
            print(e)

    elif selection == "3":
        # iterating through packages to print package information
        for count in range(1, 41):
            package_i = myHash.search(count)  # searching myHash
            print("PackageID:", package_i.id, "\nAddress:", package_i.address, package_i.city,
                  package_i.state, package_i.zipcode, "\nDeadline:", package_i.deadline,
                  "\nMass:", package_i.mass, "\nNotes:", package_i.special, "\nStatus:", package_i.status,
                  "\nTime Delivered:", package_i.delivery_time, "\n")

    elif selection == "0":
        # if user inputs 0 prints exit statement
        print("Thanks for choosing WGUPS! Goodbye")

    else:
        # if user inputs anything other than a selection lets user know to try again
        print("Invalid selection, please try again. Goodbye.")


# Calling the app function for the UI
app()

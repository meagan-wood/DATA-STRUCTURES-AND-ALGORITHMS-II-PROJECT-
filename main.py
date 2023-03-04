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
import truck
from package import myHash


# Creates the UI to get package information.
# Entering a package ID will return all the information for that package at the provided time.
# Entering a time will return all trucks and packages' status,
# if the package has been delivered, will return the delivery time with the package ID.
# Option 3 will return ALL the packages with their information and the delivery time after all deliveries are complete
# Error handling for invalid entries or format and keyboardInterrupt.
def app():
    try:
        CRed = '\33[31m'
        print('\nWelcome to the WGUPS!')
        print("\nTruck departure times and packages assigned to each truck:", "\nTruck 1:", truck.truck1_depart,
              truck.truck1_packages, "\nTruck 2:", truck.truck2_depart, truck.truck2_packages,
              "\nTruck 3:", truck.truck3_depart, truck.truck3_packages)
        print('\nThe total mileage to deliver all packages:', '\033[4m' + CRed + truck.total_mileage() + '\033[0m',
              'miles.')
        # Option choices for user, gets user input
        selection = input(
            "\nHow can I help? Please enter the number associated with the task you'd like to complete: \n"
            "1 - Lookup package status and info using the package ID and time \n"
            "2 - Check status of ALL packages at a given time \n"
            "3 - View all packages with their delivery time and package information \n"
            "0 - To exit the program \n")
        if selection == "1":
            enter_id = int(input("Please enter the package ID:"))
            package_info = myHash.search(enter_id)  # searches hash table using enter_id
            # Provides all package info the user searched for
            if package_info is None:
                print("\nERROR:", "\nPackage ID:", enter_id, "- not found. Please try again.")
            else:
                try:
                    entered_time = input("Please enter the time using Military Time in the 'HH:MM' format:")
                    convert_time = datetime.strptime(entered_time, "%H:%M")  # converting user input to datetime
                    input_time = timedelta(hours=convert_time.hour,
                                           minutes=convert_time.minute)  # converting time to timedelta
                    print("\nPackageID Entered:", enter_id)
                    print("Time Entered:", input_time, "\n")  # displaying the time the user entered
                    if input_time < package_info.departure_time:
                        package_info.status = "Hub"
                    elif input_time < package_info.delivery_time:
                        package_info.status = "En-Route"
                    else:
                        package_info.status = "Delivered at %s" % package_info.delivery_time
                    print("ID:", package_info.id, "\nAddress:", package_info.address, package_info.city,
                          package_info.state, package_info.zipcode, "\nDeadline:", package_info.deadline, " Mass:",
                          package_info.mass, "\nNotes:", package_info.special, "\nStatus:", package_info.status, "\n")

                except ValueError as e:
                    print("\nERROR:",
                          "\nInvalid time format, time must be MILITARY TIME (24hr clock) entered in 'HH:MM' "
                          "format. Goodbye.")
                    print(e)

        elif selection == "2":
            try:
                entered_time = input(
                    "Please enter the time using Military Time in the 'HH:MM' format:")  # getting user input
                convert_time = datetime.strptime(entered_time, "%H:%M")  # converting user input to datetime
                input_time = timedelta(hours=convert_time.hour,
                                       minutes=convert_time.minute)  # converting time to timedelta
                print("\nTime Entered:", input_time, "\n")  # displaying the time the user entered
                for count in range(1, 41):
                    package_i = myHash.search(count)
                    if input_time < package_i.departure_time:
                        package_i.status = "Hub"
                    elif input_time < package_i.delivery_time:
                        package_i.status = "En-Route"
                    else:
                        package_i.status = "Delivered at %s" % package_i.delivery_time
                    print("ID:", package_i.id, "Address:", package_i.address, package_i.city, package_i.state,
                          package_i.zipcode, "Deadline:", package_i.deadline, "Mass:", package_i.mass, "Notes:",
                          package_i.special, "Status:", package_i.status, "\n")

            # Error handling
            except ValueError as e:
                print("\nERROR:", "\nInvalid time format, time must be MILITARY TIME (24hr clock) entered in 'HH:MM' "
                                  "format. Goodbye.")
                print(e)

        elif selection == "3":
            # iterating through packages to print package information for each package
            for count in range(1, 41):
                package_i = myHash.search(count)  # searching myHash
                print("ID:", package_i.id, " Address:", package_i.address, package_i.city,
                      package_i.state, package_i.zipcode, " Deadline:", package_i.deadline,
                      " Mass:", package_i.mass, " Notes:", package_i.special, " Status:", package_i.status,
                      "at", package_i.delivery_time, "\n")

        elif selection == "0":
            # if user inputs 0 prints exit statement
            print("Thanks for choosing WGUPS! Goodbye")

        else:
            # if user inputs anything other than a selection lets user know to try again
            print("Invalid selection, please try again. Goodbye.")
    except KeyboardInterrupt:
        print("\nNothing entered. Please try again")


# Calling the app function for the UI
app()

# Meagan Wood ID: 000933763
# mwoo195@wgu.edu
import datetime
from datetime import datetime, timedelta
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
        enter_id = int(input("Please enter the package ID:"))
        package_info = myHash.search(enter_id)
        print(package_info)

    elif selection == "2":
        try:
            entered_time = input("Please enter the time you wish to search using the 'HH:MM:SS' format:")
            convert_time = datetime.strptime(entered_time, "%H:%M:%S")
            delta = timedelta(hours=convert_time.hour, minutes=convert_time.minute, seconds=convert_time.second)
            print(delta)

        except ValueError:
            print("Invalid time format, time must be entered in 'HH:MM:SS' format. Goodbye.")
            exit()

    elif selection == "0":
        print("Thanks for choosing WGUPS! Goodbye")

    else:
        print("Invalid selection, please try again. Goodbye.")


app()

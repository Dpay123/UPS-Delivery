# Dominic Payer, ID: 010482349
from datetime import datetime

from controllers.DeliveryManager import DeliveryManager

# Run the Main Application
if __name__ == '__main__':

    # GUI
    while True:
        # create a DeliveryManager
        dm = DeliveryManager()

        # Display Menu
        print("\n--------Main Menu--------")
        print("1: Simulate Total Delivery")
        print("2: Report a single package status at a given time")
        print("3: Report overall status at a given time")
        print("4: Exit the Program\n")

        choice = input("Enter a number to select one of the options: ")
        print()

        if choice == "1":
            # run the complete program
            dm.run()
            dm.status()
        elif choice == "2":
            # run the program and report the status of given package at given time
            # TODO: dm.run(id, time)
            pass
        elif choice == "3":
            time = input("Enter a time in HH:MM format: ")
            time_search = datetime.strptime(time, '%H:%M')
            # run the program and report overall status at given time
            dm.run()
            print()
            dm.status_with_time(time_search)

        elif choice == "4":
            break

    print("Exiting Program")


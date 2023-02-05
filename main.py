# Dominic Payer, ID: 010482349

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
            print("Simulating delivery.....")
            # run the complete program
            dm.run()
        elif choice == "2":
            id = input("Enter a package ID from 1-40: ")
            time = input("Enter a time in HH:MM format: ")
            id = int(id)
            # run the program and report the status of given package at given time
            # TODO: dm.run(id, time)
        elif choice == "3":
            time = input("Enter a time in HH:MM format: ")
            # run the program and report overall status at given time
            # TODO: dm.run(time)
        elif choice == "4":
            break

    print("Exiting Program")


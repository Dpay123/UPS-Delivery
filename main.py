# Dominic Payer, ID: 010482349

from controllers.DeliveryManager import DeliveryManager

# Run the Main Application
if __name__ == '__main__':

    # GUI
    while True:
        # Display Menu
        print("\n--------Main Menu--------")
        print("1: Simulate Total Delivery")
        print("2: Other")
        print("3: Other")
        print("4: Exit the Program\n")

        choice = input("Enter a number to select one of the options: ")
        print()
        if choice == "1":
            print("Simulating delivery.....")
            # create a DeliveryManager
            dm = DeliveryManager()
            # run the complete program
            dm.run()
        elif choice == "2":
            print("Function")
        elif choice == "3":
            print("Function")
        elif choice == "4":
            break

    print("Exiting Program")


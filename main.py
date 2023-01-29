from controllers.DeliveryManager import DeliveryManager

# Run the Main Application
if __name__ == '__main__':

    # create a DeliveryManager
    dm = DeliveryManager()

    # load trucks
    dm.load_first_trucks()

    # TEST: delivery via truck functionality
    dm.run()

    # TEST: delivery via dm functionality
    # dm.truck_deliver_packages(dm.truck1)
    # dm.truck_deliver_packages(dm.truck2)
    # test final truck delivery
    # dm.load_third_truck()
    # dm.truck_deliver_packages(dm.truck3)
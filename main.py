from controllers.DeliveryManager import DeliveryManager

# Run the Main Application
if __name__ == '__main__':

    # create a DeliveryManager
    dm = DeliveryManager()

    # TEST: delivery via truck functionality
    dm.run()

    # TEST: time
    print(dm.timeAtMiles(116.80000))
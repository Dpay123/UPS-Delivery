from controllers.DeliveryManager import DeliveryManager

# Run the Main Application
if __name__ == '__main__':

    # create a DeliveryManager
    dm = DeliveryManager()

    # implement functionality using manager
    dm.load_first_trucks()
    dm.truck_deliver_packages(dm.truck1)
    dm.status()

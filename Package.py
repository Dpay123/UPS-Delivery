# A package to be delivered
class Package:
    # each package has an id, address, city, state, zip, deadline, and weight
    def __init__(self, id, address, city, state, zip, deadline, weight):
        self.id = int(id)
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = "At Hub"

    # return a string representation of the package for GUI
    def __str__(self):
        return "ID: %s " \
               "| Address: %s " \
               "| City:  %s " \
               "| State: %s " \
               "| Zip:  %s " \
               "| Deadline: %s " \
               "| Weight: %s " \
               "| Status: %s" % (self.id,
                                 self.address,
                                 self.city,
                                 self.state,
                                 self.zip,
                                 self.deadline,
                                 self.weight,
                                 self.status)
# A Package is to be delivered to a Location
# delivery Location corresponds to address
import datetime

class Package:
    # each package has an id, address, city, state, zip, deadline, and weight
    # status represents the current status of the package, depending on where it is
    # delivered_at is a placeholder that gets finalized when the package is delivered
    def __init__(self, id, address, city, state, zip, deadline, weight):
        self.id = int(id)
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = "At Hub"
        self.delivered_at = datetime.timedelta(0,0)

    # return a string representation of the package for GUI
    def __str__(self):
        return "ID: %s " \
               "| Address: %s " \
               "| Deadline: %s " \
               "| Weight: %s " \
               "| Status: %s " % (self.id,
                                 self.address + ", " + self.city + ", " + self.state + " " + self.zip,
                                 self.deadline,
                                 self.weight,
                                 self.status)
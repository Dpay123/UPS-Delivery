# A Location corresponds to a delivery point of packages
class Location:
    # A location has an id, name, street address, and zip code
    def __init__(self, id, name, street, zip):
        self.id = int(id)
        self.name = name
        self.street = street
        self.zip = zip

    # return a string representation of the location for GUI display
    def __str__(self):
        return "Id: %s " \
                "| Name: %s " \
                "| Street: %s " \
                "| Zip: %s" % (self.id, self.name, self.street, self.zip)

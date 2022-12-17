class MyHashTable:
    # Constructor
    def __init__(self, initial_capacity):
        # initialize table
        self.table = []
        # add n buckets (n = initial_capacity)
        for i in range(initial_capacity):
            self.table.append([])

    def get_bucket(self, item):
        # apply hash to get the bucket
        bucket = hash(item) % len(self.table)
        # retrieve bucket
        return self.table[bucket]

    # Insert an item
    def insert(self, item):
        bucket = self.get_bucket(item.id)
        # insert item into bucket
        bucket.append(item)

    # Search for item by specifying the key
    def search(self, key):
        bucket = self.get_bucket(key)
        if bucket:
            return bucket[0]
        else:
            return None

    # remove an item with matching key
    def remove(self, key):
        bucket = self.get_bucket(key)
        if key in bucket:
            bucket.remove(key)

    # string rep
    def __str__(self):
        string = "Packages at the Hub:\n"
        for row in self.table:
            for p in row:
                string = string + str(p) + "\n"
        return string

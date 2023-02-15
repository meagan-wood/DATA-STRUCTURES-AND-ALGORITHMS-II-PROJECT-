import csv


# HashTable class
class HashTable:

    # Constructor, initial capacity.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        # initialize the empty hash table .
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, item):  # inserts and updates
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # updates if found
        # print(key, item)
        for k_val in bucket_list:
            if k_val[0] == key:
                k_val[1] = item
                return True

        # insert into the end of the bucket list if not found.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches with matching key.
    # Returns if found, or None if not found.
    def search(self, key):
        # finds bucket list for given key.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # search for the key in the list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    # Removes item by key.
    def remove(self, key):
        # finds bucket list with key.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # if found, removes the item from the list.
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])


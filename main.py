from hashTable import myHash, read_package_data

for i in range(len(myHash.table) + 1):
    print("Key: {} and Package: {}".format(i + 1, myHash.search(i + 1)))


print("\nSearch:")
print(myHash.search(22))
print(myHash.search(37))


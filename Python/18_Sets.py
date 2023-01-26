# Sets = collection which is unordered, unindexed. No duplicate values
#               [] ---> List
#               () ---> Tuple
#               {} ---> Set


utensils = {"fork", "spoon", "knife"}
dishes = {"cup", "plate", "bowl", "knife"}

utensils.add("chopsticks")                  # adds a value to set
utensils.remove("fork")                     # removes a value from set
# utensils.clear()                          # clear the set
# utensils.update(dishes)                   # adds one set to another
dinner_table = utensils.union(dishes)       # combines the two sets into one

for x in utensils:
    print(x, end=", ")

print()

for x in dinner_table:
    print(x, end=", ")

print()

print(utensils.difference(dishes))          # returns the difference
print(utensils.intersection(dishes))        # returns the common

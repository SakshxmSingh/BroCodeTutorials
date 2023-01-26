# dictionary =  A changeable, unordered collection of unique key:value pairs
#               Fast because they use hashing, allow us to access a value quickly
#               []          ---> List
#               ()          ---> Tuple
#               {}          ---> Set
#               {' ':' '}   ---> Dictionary

capitals = {'India': 'New Delhi',
            'China': 'Beijing',
            'France': 'Paris',
            'Brazil': 'Brasilia'}

print(capitals['Brazil'])                   # returns the keyed value
print(capitals.get('Germany'))              # returns the keyed value, returns with 'None' if there is no key
print(capitals.keys())                      # returns only the keys
print(capitals.values())                    # returns only the values
print(capitals.items())                     # returns all key-value pairs
capitals.update({'Germany': 'Berlin'})      # updates the dictionary
capitals.update({'China': 'Shanghai'})      # updates the value of a particular key too
capitals.pop('France')                      # removes the given key-value pair
# capitals.clear()                            clears the dictionary
for i in capitals:
    print(i)
    if i == 'Brazil':
        break
for key, values in capitals.items():
    print(key, values)

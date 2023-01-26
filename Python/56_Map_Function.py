# map() = applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function, iterable)

store = [("Shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

to_euros = lambda data: (data[0], data[1]*0.97)
to_dollars = lambda data: (data[0], data[1]/0.97)

store_euros = list(map(to_euros, store))
for i in store_euros:
    print(i)
print("-----------------------------------------")

store_dollars = list(map(to_dollars, store_euros))
for i in store_dollars:
    print(i)
print("-----------------------------------------")

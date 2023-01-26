# zip(*iterables) =  aggregates elements from two or more iterables (list, tuples, sets, etc.)
#                    creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_date = ["1/1/2022", "1/2/2022", "1/3/2022"]

users = zip(usernames, passwords, login_date)               # zips two or more iterables together
print(type(users))                                          # returns <class 'zip'> which shows type as 'zip' object

users = list(zip(usernames, passwords, login_date))         # type casting to list
print(type(users))                                          # returns <class 'list'>

for i in users:
    print(i)
print("___________________________________________________________________")

users = dict(zip(usernames, passwords))                     # type casting to dictionary

for (key, value) in users.items():
    print(key+":"+value)



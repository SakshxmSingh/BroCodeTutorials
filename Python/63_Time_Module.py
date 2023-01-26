import time


print(time.ctime(0))                    # convert a time expressed in seconds since epoch to a readable string
#                                       # epoch = when your computer thinks time began (reference point)
print(time.ctime(1000000000))           # displays date and time 1000000000 since epoch time

#_______________________________________________________________________________________________________________________

print(time.time())                      # returns current seconds since epoch using computer's clock

#_______________________________________________________________________________________________________________________

print(time.ctime(time.time()))          # returns the current time

#_______________________________________________________________________________________________________________________

time_object = time.localtime()          # creates a time object with current time
print(time_object)                      # returns all the time data separated in different parameters
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
#                                         strft = string+format, used to display the above time data in a string format
#                                         %B for month_name, %d for day_num, %Y for year, etc. respectively
print(local_time)

#_______________________________________________________________________________________________________________________

time_string = "20 April, 2020"
time_object = time.strptime(time_string, "%d %B, %Y")   # converts time string into object
print(time_object)

#_______________________________________________________________________________________________________________________

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)

time_tuple = (2022, 9, 5, 23, 15, 32, 0, 0, 0)
time_string = time.asctime(time_tuple)                  # accepts a time object or a tuple, creates time string
print(time_string)

time_tuple = (2022, 9, 5, 23, 15, 32, 0, 0, 0)
time_string = time.mktime(time_tuple)                  # accepts a time object or a tuple, returns secs since epoch time
print(time_string)

# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

# ----------------------using indexing[]-------------------------- #
name = "Saksham Singh"
first_name = name[0:7]
last_name = name[8:14]
funky_name = name[::2]                  # [0:end:2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

# ----------------------using slicing()--------------------------- #
website_1 = "http://www.google.com"
website_2 = "http://www.wikipedia.com"
slice = slice(11, -4)
print(website_1[slice])
print(website_2[slice])

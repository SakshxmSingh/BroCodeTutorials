# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key, value) in iterable}
# dictionary = {key: expression for (key, value) in iterable if conditional}
# dictionary = {key: (if/else) for (key, value) in iterable}
# dictionary = {key: function(value) for (key, value) in iterable}

#________________________________________________________________________________

cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

cities_in_C = {key: round((value-32)*5/9) for (key, value) in cities_in_F.items()}          # basic
print(cities_in_C)

#________________________________________________________________________________

weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}

sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}        # if conditional
print(sunny_weather)

#________________________________________________________________________________

cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities_weather = {key: ("Warm" if value >= 75 else "Cold") for (key, value) in cities.items()}
print(cities_weather)                                                                       # if-else

#________________________________________________________________________________

def check_temp(temp):
    if temp <= 70:
        return "Cold"
    else:
        return "Warm"

cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities_weather = {key: check_temp(value) for (key, value) in cities.items()}                # function()
print(cities_weather)
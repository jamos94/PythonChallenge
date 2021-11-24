# this program adds to a list; travel log
# travel log contains two dictionaries
# add_new_country() is called to add a new dictionary to the list

travel_log = [
{
  "country": "France", # key : value
  "visits": 12,         # key : int
  "cities": ["Paris", "Lille", "Dijon"]     #key : list
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(country_visited, times_visits, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visits
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "SStuttgart"],
}

#Nesting Dictionary in a Dictionary
travel_log_2 = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
        },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "SStuttgart"],
        "total_visits": 11
        },
}

#Nesting Dictionary in a List
travel_log_3 = [
    {   "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {   "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "SStuttgart"],
        "total_visits": 11,
    },
]




country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(country, visits, list_of_cities):
  add_dic = {}
  add_dic["country"] = country
  add_dic["visits"] = visits
  add_dic["cities"] = list_of_cities
  
  travel_log.append(add_dic)

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
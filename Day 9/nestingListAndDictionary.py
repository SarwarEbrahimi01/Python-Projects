#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berline",
}

#Nesting a list in a Dictionary
travel_log = {
    "France" : ["Paris","Lille","Dijon"],
    "Germany": ["Berline","Hamburg", "Stuttga"],
}

#Nesting Dictionay in a Dictionary
travel_log = {
    "France" : {"cities_visited" : ["Paris","Lille","Dijon"],"total_visits":12},
    "Germany": {"cities_visited" : ["Berline","Hamburg", "Stuttga"],"hotels_visited":["Niko","kylel","huntire"]},
}

#Nesting Dictionary in a List
travel_log = [
    {
        "country":"France",
        "cities_visited" : ["Paris","Lille","Dijon"],
        "total_visits":12
    },
    {
       "country":"Germany",
       "cities_visited" : ["Berline","Hamburg", "Stuttga"],
       "total_visits": 5
    },
]

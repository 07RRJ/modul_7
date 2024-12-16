import os
os.system("cls")

cars = [                    # dictionary
    {
    "make": "Audi",
    "model": "R8",
    "year": "2020",
    "color": ["red", "green", "blue"]
    },
    {
    "make": "Lamborghinin",
    "model": "Huracan EVO",
    "year": "2024",
    "color": ["orange", "red", "blue"],
    },
]

while True:                 # make varables of the dictionary values
    for car in cars:
        make = car["make"]
        model = car["model"]
        year = car["year"]
        print(f"{make} {model} {year}")

    make = input("new car: ")                    # add a car and its properties
    model = input("model: ")
    year = input("year: ")

    cars.append(                    # add the new values to the list/dictionary
        {
            "make": make,
            "model": model,
            "year": year
        }
    )
    
    remove = int(input(f"do you want to remove a list item? removable 1 to {len(cars) + 1}, anything else to keep"))
    
    cars.pop(remove)

    os.system("cls")
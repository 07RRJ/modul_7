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
    for index,car in enumerate(cars, 1):
        make = car["make"]
        model = car["model"]
        year = car["year"]
        print(f"{index}) {make} {model} {year}")

    new_car = input("\nwant to add a car, \"y\" to add ").lower()
    if new_car == "y":
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
        os.system("cls")
        while True:
            for index,car in enumerate(cars, 1):
                make = car["make"]
                model = car["model"]
                year = car["year"]
                print(f"{index}) {make} {model} {year}")
            break
    
    while True:
        try:
            remove = int(input(f"\ndo you want to remove a car? removable 1 to {len(cars) + 1}, 0 to keep it as it is "))
            if remove != 0 and remove > -1 and remove < len(cars):
                cars.pop(remove - 1)
                break
            if remove == 0:
                break
        except:
            print("plese use a \"0\" to keep it as it is and any list number to remove them")
        os.system("cls")
        while True:
            for index,car in enumerate(cars, 1):
                make = car["make"]
                model = car["model"]
                year = car["year"]
                print(f"{index}) {make} {model} {year}")
            break
    
    change_car = input("change a car, \"y\" to change").lower()
    if change_car == "y":
        try:
            car_change = input(f"which car do you want to change 1 to {len[cars] + 1}")
            cars[car_change - 1] = {
                "make": make,
                "model": model,
                "year": year
            }
        except:
            print("use a valid number")
        os.system("cls")
        while True:
            for index,car in enumerate(cars, 1):
                make = car["make"]
                model = car["model"]
                year = car["year"]
                print(f"{index}) {make} {model} {year}")
            break

    os.system("cls")
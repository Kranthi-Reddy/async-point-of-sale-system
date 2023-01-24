import asyncio
from inventory import Inventory
from order import Order


def display_catalogue(catalouge):
    burgers = catalouge["Burgers"]
    sides = catalouge["Sides"]
    drinks = catalouge["Drinks"]

    print("--------- Burgerss ---------")
    for burger in burgers:
        item_id = burger[id]
        name = burger["name"]
        price = burger["price"]
        print(f"{item_id}. {name} ${price}")
              
    print("\n--------- Sides ---------")
    for side in sides:
        sizes = side[sides]

        
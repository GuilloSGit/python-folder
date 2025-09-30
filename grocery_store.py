grocery_inventory = {
    "Milk": ["Dairy", 3.50, 8],
    "Eggs": ["Dairy", 5.50, 30],
    "Bread": ["Bakery", 2.99, 15],
    "Apples": ["Produce", 1.50, 50],
}

if grocery_inventory["Eggs"][1] > 5:
    print("Eggs are too expensive, reducing the price by $1")
    grocery_inventory["Eggs"][1] -= 1
else:
    print("The price of eggs is reasonable")  


# agregar a grocery_inventory el producto "Tomatoes"
grocery_inventory["Tomatoes"] = ["Produce", 1.20, 30]
print("Inventory after adding Tomatoes: ", grocery_inventory)

if grocery_inventory["Milk"][2] < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"][2] += 20
else:
    print("Milk has sufficient stock.")


if grocery_inventory["Apples"][1] > 2:
    print("Apples removed from inventory due to high price.")
    del grocery_inventory["Apples"]



    
from utils import getInt, getFloat, getText
 
 
cars = []
 
 
# CREATE - add car
def addCar():
    try:
        brand = getText("Brand: ")
        model = getText("Model: ")
        price = getFloat("Price: ")
        year = getInt("Year: ")
        color = getText("Color: ")
 
        if 1886 > year or 2026 < year:
            raise ValueError("year is not correct!")
 
        if price <= 0:
            raise ValueError("price is not correct!")
 
        car = {
            "id": max([c["id"] for c in cars], default=0) + 1,
            "brand": brand,
            "model": model,
            "price": price,
            "year": year,
            "color": color
        }
 
        cars.append(car)
 
        print("Car added succesfully.")
 
    except ValueError as e:
        print("some error ocured:", e)
 
 
# READ - show car
def showCar(car):
    print("-" * 20)
    print("\n")
 
    print(f"ID: {car["id"]}")
    print(f"Brand: {car["brand"]}")
    print(f"Model: {car["model"]}")
    print(f"Price: {car["price"]}")
    print(f"Year: {car["year"]}")
    print(f"Color: {car["color"]}")
 
    print("\n")
    print("-" * 20)
 
 
# READ - show all cars
def showAllCars():
    if not cars:
        print("There is not a car.")
        return

    for car in cars:
        showCar(car)
 
 
# UPDATE - update car
def updateCar():
    if not cars:
        print("There is not a car.")
        return
 
    carID = getInt("enter Car ID: ")
    car = None
 
    for i in cars:
        if i["id"] == carID:
            car = i
            break
 
    if car is None:
        print("Car not found...")
        return
 
    showCar(car)
 
    print("""
 
    1. Price
    2. Color
 
    """)
 
    try:
        choice = int(input("enter choice: "))
 
        if choice == 1:
            car["price"] = getFloat("enter new price: ")
        elif choice == 2:
            car["color"] = getText("enter new color: ")
        else:
            print("wrong choice...")
            return
 
        print("Car updated.")
       
    except ValueError as e:
        print(e)




def deleteCar():
    if not cars:
            print("There is not a car.")
            return
    deletedID = getInt('enter car ID')
    car = None

    for i in cars:
        if i["id"] == deletedID:
            car = i
            break
        
    if car is None:
        print("Car not found")
        return
    showCar(car)
    
    confirm = getText("Are you sure you want to delete this car? (y/n): ").lower()

    if confirm == "y":
        cars.remove(car)
        print("Car deleted successfully.")
    else:
        print("Delete cancelled.")


def filterByPrice():
    
    if not cars:
        print("There is not a car.")
        return

    try:
        price = getFloat("Price: ")

        if price <= 0:
            raise ValueError("price is not correct!")

        result = [c for c in cars if c["price"] <= price]

        if not result:
            print("No car found.")
            return

        for car in result:
            showCar(car)

    except ValueError as e:
        print("some error occurred:", e)





def filterByYear():
    
    if not cars:
        print("There is not a car.")
        return

    try:
        year = getInt("Year: ")

        if year < 1886 or year > 2026:
            raise ValueError("year is not correct!")

        result = [c for c in cars if c["year"] >= year]

        if not result:
            print("No car found.")
            return

        for car in result:
            showCar(car)

    except ValueError as e:
        print("some error occurred:", e)





def filterCars():
    while True:
        print("""
 
        1. Filter by Price
        2. Filter by Year
        3. Back
 
        """)
 
        choice = getInt("enter choice: ")
 
        if choice == 1:
            filterByPrice()
        elif choice == 2:
            filterByYear()
        elif choice == 3:
            break
        else:
            print("wrong choice...")
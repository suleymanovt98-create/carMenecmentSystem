import os
import msvcrt

from cars import addCar, showAllCars, updateCar, deleteCar, filterCars


def menu():
    options = [
        "Add Car",
        "Show All Cars",
        "Update Car",
        "Delete Car",
        "Filter Cars",
        "Exit"
    ]

    selected = 0

    while True:
        os.system("cls")

        print("$$$$$$ WELCOME CAR MANAGEMENT $$$$$$\n")

        for index, option in enumerate(options):
            if index == selected:
                print(f" --> {option}")
            else:
                print(f"     {option}")

        key = msvcrt.getch()

        if key == b'\xe0':
            key = msvcrt.getch()

            if key == b'H':
                selected = (selected - 1) % len(options)

            elif key == b'P':
                selected = (selected + 1) % len(options)

        elif key == b'\r':

            os.system("cls")

            if selected == 0:
                addCar()

            elif selected == 1:
                showAllCars()

            elif selected == 2:
                updateCar()

            elif selected == 3:
                deleteCar()

            elif selected == 4:
                filterCars()

            elif selected == 5:
                print("Goodbye!")
                break

            input("\nPress Enter to continue...")


menu()
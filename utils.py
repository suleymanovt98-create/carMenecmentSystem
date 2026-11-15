def getInt(message):
    while True:
        try:
            return int (input(message))
        except ValueError:
            print("error, please enter int value")

def getFloat(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("error, please enter a number")


def getText(message):
    while True:
        value = input(message).strip()

        if value:
            return value
        print("Field cannot be empty")
            
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read and return list of to-dos """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """ Write the to-do items list in a text file. """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_local)


def parse(feet_inches):
    feet_inches = feet_inches.split(" ")
    feet = float(feet_inches[0])
    inches = float(feet_inches[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = (feet * 0.3048) + (inches * 0.0254)
    return meters


def state(temperature_local):
    points = {"freezing_point": 0, "boiling_point": 100}
    if points["freezing_point"] < temperature_local < points["boiling_point"]:
        return "Liquid"
    elif temperature_local >= points["boiling_point"]:
        return "Gas"
    else:
        return "Solid"


if __name__ == "__main__":
    print("hello FROM FUNCTIONS")
    print(get_todos())

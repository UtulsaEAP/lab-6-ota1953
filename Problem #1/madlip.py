# Owen Anderson THUR 2:00 - 3:15
def food_input():
    user_input = input()
    tokens = user_input.split()
    while tokens[0] != "done" and tokens[1] != 0:
        print("Eating "+tokens[1]+ " "+ tokens[0]+" a day keeps you happy and healthy.")
        user_input = input()
        tokens = user_input.split()
        return


if __name__ == "__main__":
    food_input()
    
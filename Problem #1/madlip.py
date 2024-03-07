'''
Name: Owen Anderson 
Lab Time: THUR 2:00 - 3:15
'''
def food_input():
    while True:
        user_input = input()
        tokens = user_input.split()
        if tokens[0] != "quit" and tokens[1] != 0:
            print("Eating "+tokens[1]+ " "+ tokens[0]+" a day keeps you happy and healthy.")
        else:
            break
    

if __name__ == "__main__":
    food_input()
    
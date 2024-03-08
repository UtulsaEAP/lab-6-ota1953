'''
Name: Owen Anderson 
Lab Time: THUR 2:00 - 3:15
'''
def calculate_car_wash_price(service_choice1, service_choice2):
    services = {'Air freshener': 1, 'Rain repellent': 2, 'Tire shine': 2, 'Wax': 3, 'Vacuum': 5}
    base_wash = 10
    total = 0
   
   #type your code here 
    print("ZyCar Wash")
    print("Base car wash - $"+str(base_wash))
    if service_choice1 == "-":
        pass
    elif service_choice1 in services:
        print(service_choice1+' - $'+str(services[service_choice1]))

    if service_choice2 == "-":
        pass
    elif service_choice2 in services:
        print(service_choice2+' - $',str(services[service_choice2]))

    if service_choice2 == "-":
        if service_choice1 == "-":
            total = base_wash
        elif service_choice1 != "-":
            total = base_wash+services[service_choice1]
    else:
        total = base_wash+services[service_choice1]+services[service_choice2]
    print("-----")
    print("Total price: $"+str(total))

    
if __name__ == '__main__':
    # Get user input for service choices
    service_choice1 = input("Enter first service choice: ")
    service_choice2 = input("Enter second service choice: ")

    # Call the function to calculate car wash price
    calculate_car_wash_price(service_choice1, service_choice2)

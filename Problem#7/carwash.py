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
    if service_choice1 != '-':
        choice1_price = services.get(service_choice1)
        print (str(service_choice1) + ' - $' + str(choice1_price))
    else:
        choice1_price = 0
    
    if service_choice2 != '-':
        choice2_price = services.get(service_choice2)
        print (str(service_choice2) + ' - $' + str(choice2_price))
    else:
        choice2_price = 0

    total_price = base_wash + choice1_price + choice2_price

    print (f'-----\nTotal price: ${total_price}')



    
if __name__ == '__main__':
    # Get user input for service choices
    service_choice1 = input("Enter first service choice: ")
    service_choice2 = input("Enter second service choice: ")

    # Call the function to calculate car wash price
    calculate_car_wash_price(service_choice1, service_choice2)

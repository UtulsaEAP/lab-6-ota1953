'''
Name: Owen Anderson 
Lab Time: THUR 2:00 - 3:15
'''
def process_user_contacts(user_input):
    myDict ={}
    user_contacts = user_input.split()
    for tokens in user_contacts:
        name, phone = tokens.split(',')
        myDict[name] = phone


    # Get contact name from input, output contact's phone number
    contact_name = input("Enter the contact name: ")
    if contact_name in myDict:
        print(myDict[contact_name])
    else:
        pass

   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)

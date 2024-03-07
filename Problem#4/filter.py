def process_and_print(user_input):
      # Split into separate strings
    split = user_input.split()
        # Convert strings to integers and filter out negative values
    input_data = []
    for i in split:
        if int(i) < 0:
            input_data.append(int(i))

    # Sort integers in reverse order
    input_data.sort(reverse=True)
    #input_data.reverse()
    # Print sorted integers
    for values in input_data:
        print(values, end=' ')

   
    
    

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)

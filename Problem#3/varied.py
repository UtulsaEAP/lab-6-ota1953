# #Owen Anderson THUR 2:00-3:15
def process_input(input_string):
       # Split into separate strings

  string_list = input_string.split()
  length = len(string_list)
  val_list =[]
  while length > 0:
    length -= 1
    val_list.append(float(string_list[length]))
    
  max_value = max(val_list)
  average_value = (sum(val_list)/(len(val_list)))
  return max_value, average_value

if __name__ == "__main__":
     # User inputs string w/ numbers
     user_input = (input("Enter a space-separated string of numbers: "))

     # Call the function and get the results
     max_value, average_value = process_input(user_input)

     print(f'Max Value: {max_value:.2f}')
     print(f'Average Value: {average_value:.2f}')



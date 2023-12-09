# Defining a list of elements
input_data = [1, "hello", 3.14,None]
# Define a lambda function that checks if an element was an integer or a string
list_int_or_str = lambda x: isinstance(x, (int, str))
# Apply the lambda function to check each element in the list and store the results in a after_check variable
After_check = [list_int_or_str(x) for x in input_data]
# Display the output
print("After_check:,",After_check)

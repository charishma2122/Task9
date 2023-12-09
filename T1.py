

data=[10, 501, 22, 37, 100, 999, 87, 351]
result = filter (lambda x: x > 4, data)
print (list(result))
"""
1.lambda function lambda x: x > 4 checks if each element in the data list is greater than 4
2.all the elements in the data list are greater than 4, 
so the filter function does not remove any elements, and the entire list is given as output
"""
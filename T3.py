def fibonacci(count): #Defined a fibonacci function and pass the number --> count
   my_var = [0, 1] # initial numbers of the Fibonacci sequence
   # Fibonacci sequence by summing the last two elements and append the result to my_varis and is used the map the output to generate the new sequence
   any(map(lambda _:my_var.append(sum(my_var[-2:])),range(2, count)))
   return my_var[:count] # it returns the elements of the Fibonacci sequence
#Displaying the fibonacci output
print("fibonacci series",fibonacci(50)) # you can change 50 to n number which you wavnt
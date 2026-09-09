# Take three numbers as input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third nu

# Check which number is the largest
if (num1 >= num2) and (num1 >= num3):
  
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    larg

# Print the result
print(f"The largest number is: {largest}")

from mpmath import mp

# Set precision to 50 decimal places (adjust as needed)
noOfDigits=int(input("Enter the number of digits: "))
mp.dps = noOfDigits
pi_value = mp.pi

print(f"Value of π : {pi_value}")

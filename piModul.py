from mpmath import mp
Digit=int(input("Enter the number of digits: "))
# mp.dps = Digit
# print(mp.pi)
def print_pi_to_n_digits(Digit):

    # Set precision to n decimal places

    mp.dps = Digit + 1  # Adding 1 to account for the "3." before the decimals

    # Return pi to n decimal places as a string

    return str(mp.pi)

print(print_pi_to_n_digits(Digit))
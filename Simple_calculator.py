import Simple_calculator as Simple_calculator
import calculator as calc


# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=",
                    calc.add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=",
                    calc.subtract(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=",
                    calc.multiply(number_1, number_2))
import Simple_calculator as Simple_calculator
import calculator as calc


# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=",
                    calc.add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=",
                    calc.subtract(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=",
                    calc.multiply(number_1, number_2))

    



number = float(input("Please input your number: "))
if (number > 0 and number%2 == 0):
	print("Your number is positive")
	print("And your number is even")
	print("Thank you for playing")

if (number > 0 and number%2 is not 0):
        print("Your number is positive")
        print("And your number is odd")
        print("Thank you for playing")

if (number < 0 and number%2 != 0):
	print("Your number is negative")
	print("And your number is odd")
	print("Thank you for playing")

if (number < 0 and number%2 == 0):
        print("Your number is negative")
        print("And your number is even")
        print("Thank you for playing")

if (number == 0):
	print("Your number is zero")
	print("Thank you for playing")

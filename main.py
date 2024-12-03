def fizzbuzz(number):

    for num in range(1,number + 1):
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

number = int(input("Enter a number between 1 and 100: "))

if number < 1 or number > 100:
    print("invalid input. Please enter a number between 1 and 100.")
else:
    fizzbuzz(number)
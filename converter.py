def main():
    print("Welcome to Unit Converter: Kilometer to Mile!")

while True:
    kilometers = float(input("Enter the number of kilometers:"))
    miles = kilometers * 0.621371
    print(f"{kilometers} kilometers is equal to {miles:.2f} miles")

    another_conversion = input("Do you want to do another conversion? (yes/no): ")
    if another_conversion.lower() != "yes":
            break

print("Thank you for using our Converter. Bye!")

if __name__ == "__main__":
    main()
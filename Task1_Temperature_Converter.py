def convert_temperature():
    print("Temperature Converter")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")

    choice = int(input("Convert from (1/2/3): "))
    temp = float(input("Enter temperature value: "))

    if choice == 1:  # Celsius
        print("Fahrenheit:", (temp * 9/5) + 32)
        print("Kelvin:", temp + 273.15)

    elif choice == 2:  # Fahrenheit
        print("Celsius:", (temp - 32) * 5/9)
        print("Kelvin:", ((temp - 32) * 5/9) + 273.15)

    elif choice == 3:  # Kelvin
        print("Celsius:", temp - 273.15)
        print("Fahrenheit:", ((temp - 273.15) * 9/5) + 32)

    else:
        print("Invalid choice")

convert_temperature()

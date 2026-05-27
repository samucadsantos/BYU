temperature = float(input("What is the temperature in Fahrenheit? "))

convert_to_celsius = (temperature - 32) * 5 / 9
format_decimal = f"{convert_to_celsius:.1f}"

print(f"The temperature in Celsius is {format_decimal} degrees.")
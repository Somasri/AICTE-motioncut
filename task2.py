def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def temperature_converter():
    print("Temperature Converter:")
    source_unit = input("Enter source unit (Celsius or Fahrenheit): ").strip().lower()
    if source_unit not in ["celsius", "fahrenheit"]:
        print("Unsupported unit. Please enter Celsius or Fahrenheit.")
        return
    
    try:
        value = float(input("Enter the value to convert: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    if source_unit == "celsius":
        result = celsius_to_fahrenheit(value)
        target_unit = "Fahrenheit"
    else:
        result = fahrenheit_to_celsius(value)
        target_unit = "Celsius"

    print(f"{value} {source_unit} is equal to {result:.2f} {target_unit}")

def length_converter():
    print("Length Converter:")
    source_unit = input("Enter source unit (Meters or Feet): ").strip().lower()
    if source_unit not in ["meters", "feet"]:
        print("Unsupported unit. Please enter Meters or Feet.")
        return
    
    try:
        value = float(input("Enter the value to convert: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    if source_unit == "meters":
        result = meters_to_feet(value)
        target_unit = "Feet"
    else:
        result = feet_to_meters(value)
        target_unit = "Meters"

    print(f"{value} {source_unit} is equal to {result:.2f} {target_unit}")

def weight_converter():
    print("Weight Converter:")
    source_unit = input("Enter source unit (Kilograms or Pounds): ").strip().lower()
    if source_unit not in ["kilograms", "pounds"]:
        print("Unsupported unit. Please enter Kilograms or Pounds.")
        return
    
    try:
        value = float(input("Enter the value to convert: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    if source_unit == "kilograms":
        result = kilograms_to_pounds(value)
        target_unit = "Pounds"
    else:
        result = pounds_to_kilograms(value)
        target_unit = "Kilograms"

    print("{value} {source_unit} is equal to {result:.2f} {target_unit}")

def main():
    print("Unit Converter")
    conversion_type = input("Choose a conversion type (Temperature, Length, Weight): ").strip().lower()

    if conversion_type == "temperature":
        temperature_converter()
    elif conversion_type == "length":
        length_converter()
    elif conversion_type == "weight":
        weight_converter()
    else:
        print("Unsupported conversion type. Please choose Temperature, Length, or Weight.")

if __name__ == "__main__":
    main()

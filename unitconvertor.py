def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def kg_to_ounces(kg):
    return kg * 35.2741

def ounces_to_kg(ounces):
    return ounces / 35.274

def convert_weight():
    print("Select the unit you want to convert from:")
    print("1. Kilograms")
    print("2. Pounds")
    print("3. Ounces")
    
    choice_from = int(input("Enter your choice (1/2/3): "))
    value = float(input("Enter the weight value to convert: "))

    if choice_from == 1:
        print("Select the unit you want to convert to:")
        print("1. Pounds")
        print("2. Ounces")
        
        choice_to = int(input("Enter your choice (1/2): "))
        
        if choice_to == 1:
            converted_value = kg_to_pounds(value)
            print(f"{value} kilograms is equal to {converted_value} pounds")
        elif choice_to == 2:
            converted_value = kg_to_ounces(value)
            print(f"{value} kilograms is equal to {converted_value} ounces")
        else:
            print("Invalid choice")
            
    elif choice_from == 2:
        # Conversion from pounds to other units
        pass  # Add code for pounds to other units conversion
        
    elif choice_from == 3:
        # Conversion from ounces to other units
        pass  # Add code for ounces to other units conversion
        
    else:
        print("Invalid choice")

convert_weight()

print("--- Vote Checker (Band karne ke liye 0 dabayein) ---")

while True:  # Ye loop chalta rahega
    age = int(input("Apni umar likhiye: "))

    if age == 0:
        print("Program band ho raha hai. Bye!")
        break  # Loop se bahar nikalne ke liye
    
    if age >= 18:
        print("Aap vote de sakte ho.")
    else:
        print("Aap vote nahi de sakte.")
    
    print("-" * 20) # Ek line design ke liye
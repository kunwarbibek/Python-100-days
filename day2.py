name = input("Enter your name: ")
age = int(input("Enter age: "))
amount = int(input("Enter amount: "))
profession = input("Enter profession (student / non-student): ").lower()

if profession == "student":
    if age < 10:
        discount = amount * 0.5
    elif 10 <= age <= 17:
        discount = amount * 0.3
    elif 18 <= age <= 25:
        discount = amount * 0.2
    else:
        discount = amount * 0.1
else:
    if age < 18:
        discount = amount * 0.1
    elif 18 <= age <= 60:
        discount = amount * 0.05
    else:
        discount = amount * 0.15

final_price = amount - discount

print("\n--- Discount Summary ---")
print("Name:", name)
print("Age:", age)
print("Profession:", profession.capitalize())
print("Original Amount:", amount)
print("Discount Amount:", discount)
print("Final Price to Pay:", final_price)

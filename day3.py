# my_list = [1, 2, 3, "Python", True]
# my_dict = {"name": "Alice", "age": 25, "language": "Python"} key:value pair

# ===> while loop 
i = 1
while i <= 5:
    print("Number:", i)
    i += 1
print("***********************************************")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)
print("***********************************************")
count = 0
while True:
    count += 1
    print("Count:", count)
    if count == 3:
        break

print("***********************************************")


def calculate_discount(profession, age, amount):
    if profession == "student":
        if age < 10:
            return amount * 0.5
        elif 10 <= age <= 17:
            return amount * 0.3
        elif 18 <= age <= 25:
            return amount * 0.2
        else:
            return amount * 0.1
    else:
        if age < 18:
            return amount * 0.1
        elif 18 <= age <= 60:
            return amount * 0.05
        else:
            return amount * 0.15

def main():
    while True:
        print("\n--- New Customer ---")
        name = input("Enter customer name: ")
        age = int(input("Enter age: "))
        profession = input("Enter profession (student / non-student): ").lower()

        items = []
        while True:
            price = float(input("Enter item price (or 0 to finish): "))
            if price == 0:
                break
            items.append(price)

        total_amount = sum(items)
        discount = calculate_discount(profession, age, total_amount)
        final_amount = total_amount - discount

        print("\n--- Bill Summary ---")
        print(f"Customer: {name}")
        print(f"Age: {age}")
        print(f"Profession: {profession.capitalize()}")
        print(f"Total Amount: Rs. {total_amount:.2f}")
        print(f"Discount: Rs. {discount:.2f}")
        print(f"Amount to Pay: Rs. {final_amount:.2f}")

        cont = input("\nProcess another customer? (yes/no): ").lower()
        if cont != 'yes':
            print("Thank you! Have a nice day.")
            break

if __name__ == "__main__":
    main()

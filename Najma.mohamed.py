def make_sandwich(*ingredients):
    print("You ordered a sandwich with the following ingredients:")
    for item in ingredients:
        print(f"- {item}")
    print()  # blank line for spacing


make_sandwich("Tuna", "Mayo", "Banana Peppers", "Cheese", "Ranch")

make_sandwich("Turkey", "Egg", "Cheese")
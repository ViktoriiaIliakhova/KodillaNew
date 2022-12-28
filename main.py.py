# Task 1
product_dictionary = {
    "bakery": ["bread", "donuts", "buns"],
    "grocery_store": ["carrot", "celery", "arugula"]
}
for key, val in product_dictionary.items():
    val = [i.title() for i in val]
    print(f"I am going to {key.capitalize()} and buy there {val}.")

print("Total number of products:")
print(sum([len(product_dictionary[val]) for val in product_dictionary]))

# Task 2
number_list = [x**3 for x in range(0, 100) if x % 5 == 0]
print(number_list)
shopping_list = []

while True:
    item = input("Enter item (or 'done' to finish): ")
    if item == "done":
        break
    shopping_list.append(item)
for i, item in enumerate(shopping_list, 1):
    print(f"{i}. {item}")

print(f"Total items: {len(shopping_list)}")
print((max(shopping_list, key=len)))

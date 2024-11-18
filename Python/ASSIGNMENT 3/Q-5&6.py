# Defult Index
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars"
print(myorder.format(quantity, itemno, price))

# Q6. Changing the order
myorder = "I want {1} pieces of item num {0} for {2} dollars"
print(myorder.format(itemno,quantity, price))

# f String
print(f"I want {quantity} pieces of item {itemno} for {price} dollars")

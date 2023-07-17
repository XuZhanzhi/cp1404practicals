total_price = 0
number_of_item = int(input("Number of items: "))
for i in range(number_of_item):
    price = float(input("Price of item: "))
    total_price += price
if total_price > 100:
    discount = total_price * 0.1
    total_price -= discount
print("Total price for ", number_of_item, " items is $", "{:.2f}".format(total_price))

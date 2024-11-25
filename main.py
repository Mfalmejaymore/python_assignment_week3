# mek a function for calculating it
def calculate_discount(price, discount_percent):
	discount = price * (discount_percent / 100)
	final_price = price

	if discount_percent >= 20:
		final_price = price - discount

	return final_price

# a test
# res = calculate_discount(200,35)
# print(res)

# prompt user to enter a price and discount

myprice = input("enter the item's price : ");
mydiscount = input("enter your discount percentage : ");

if int(mydiscount) > 0:
	res = calculate_discount(int(myprice),int(mydiscount))
	print("final price : " + str(res))
else:
	print("your price : " + str(myprice))
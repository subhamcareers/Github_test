price=int(input("Enter the price of cake: Rs. "))
quantity=int(input("Enter the no. of cakes: "))
amount=price*quantity

if amount>1000:
    print("Congratulations......! You're getting a Discount of 10%")
    discount=amount*10/100
    amount=amount-discount
print ("Your total amount is: Rs.", amount)

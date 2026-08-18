customer_name=input("Enter customer name: ")
customer_id=input("Enter customer ID: ")
number_of_items=int(input("Enter number of items: "))

items=[]

for i in range(number_of_items):
    print("Enter details for item",i+1)
    item_name=input("Enter item name: ")
    quantity=int(input("Enter quantity: "))

    if quantity<=0:
        print("Invalid quantity")
        quantity=1
    else:
        pass

    price=float(input("Enter price per unit: "))

    if price<=0:
        print("Invalid price")
        price=0
    else:
        pass

    total_price=quantity*price
    item=(item_name,quantity,price,total_price)
    items.append(item)

total_bill=0

for item in items:
    total_bill=total_bill+item[3]

if total_bill>5000:
    discount_percent=15
elif total_bill>=3000:
    discount_percent=10
elif total_bill>=1000:
    discount_percent=5
else:
    discount_percent=0

discount_amount=total_bill*discount_percent/100
final_amount=total_bill-discount_amount

customer={"Name":customer_name,"ID":customer_id}
print()
print("Customer Name:",customer["Name"])
print("Customer ID:",customer["ID"])
print()
print("Purchased Items")

for item in items:
    print()
    print("Item:",item[0])
    print("Quantity:",item[1])
    print("Unit Price:",item[2])
    print("Total Price:",item[3])

print()
print("Total Bill:",total_bill)
print("Discount:",discount_percent,"%")
print("Discount Amount:",discount_amount)
print("Final Payable Amount:",final_amount)
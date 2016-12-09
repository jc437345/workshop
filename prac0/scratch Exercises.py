__author__ = 'jc437345'
instruction = "welcome to our program \nInput negative number of items"

print(instruction)
numberofitems = 1
while numberofitems > 0 :
    numberofitems = int (input("please input the number of items: "))
    costperitem = float(input("The shipping cost for each item: $"))
    totalshippingcost = numberofitems * costperitem
    if totalshippingcost > 100:
        totalshippingcost = totalshippingcost * 0.9
    print("the total shipping cost ",totalshippingcost)

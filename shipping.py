weight = 41.5

# ground shipping
flatRate = 20
if weight <= 2:
    pricePerPound = 1.5
elif weight > 2 and weight <= 6:
    pricePerPound = 3
elif weight > 6 and weight <= 10:
    pricePerPound = 4
elif weight > 10:
    pricePerPound = 4.75
else: 
    print("error")


print(flatRate + (weight * pricePerPound))


#premium ground shipping
premiumShipping = 125

print("Premium Ground Shipping Costs: $", premiumShipping)

#drone shipping
flatRate = 0
if weight <= 2:
    pricePerPound = 4.5
elif weight > 2 and weight <= 6:
    pricePerPound = 9
elif weight > 6 and weight <= 10:
    pricePerPound = 12
elif weight > 10:
    pricePerPound = 14.25
else: 
    print("error")

print(flatRate + (weight * pricePerPound))
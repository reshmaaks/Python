p=float(input("Enter the principle amount : "))
r=float(input("Enter the rate of interest : "))
t=float(input("Enter the time in years : "))
compound_interest = p*(pow((1+r/100),t))
print("Principle amount : ",p)
print("Interest rate : ",r)
print("Time in years : ",t)
print("copmpound interest : ",compound_interest)
a = int(input("Enter first number : "))
b = int(input("Enter second number : " ))
def compute_hcf(a,b):
    if a > b:
        smaller = a
    else:
        smaller = b
    for i in range(1, smaller+1):
        if((a % i == 0) and (b % i == 0)):
            hcf = i
    return hcf
print("The hcf of a and b",compute_hcf(a,b))
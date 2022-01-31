def character_mix(a,b):
    a1=b[:2]+a[2:]
    b1=a[:2]+b[2:]
    return a1+' '+b1
print(character_mix('mango', 'apple'))
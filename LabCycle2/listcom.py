#Generate positive list of numbers from a given list of integers
nlist=[-2,3,-4,5,-6,7,-8,9]
print("nlist : ",nlist)
print("positive numbers : ")

#Square of N numbers

for num in nlist :
    if num>=0:
        print(num)
print("nlist :",nlist)
print("square of list : ")
for n in nlist :
        print(n**2)
#Form a list of vowels selected from a given word

vlist=['a','e','i','o','u']
n=input("Enter the word")
list1=[]
for x in n:
    if x in vlist and x not in list1:
         list1.append(x)
print("vowels :",list1)

#List ordinal value of each element of a word
n=input("Enter a word")
list1=[]
print("The ordinal values ")
for a in n:
   list1.append(ord(a))
print(list1)



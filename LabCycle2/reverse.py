# 7.Write a program to Print list in reverse order using a loop.
list1 = [27, 'MCAB', 'amal' 'jyothi', 408]
print("list1 : ", list1)
list2 = []
for i in range(len(list1)):
    list2.insert(i, list1[-1])
    list1.pop(-1)
print("Reverse order list : ", list2)

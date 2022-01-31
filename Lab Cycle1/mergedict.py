dict1 = {1:'A',2:'B',3:'C',4:'D',5:'E'}
dict2 = {6:'F',7:'G',8:'H',9:'I',10:'J'}
def Merge(dict1,dict2):
    return dict2.update (dict1)
print(Merge(dict1,dict2))
print(dict2)
thisdict = {1:'Ajith',5:'Sam',3:'reema',2:'manu',4:'binu'}
l=list(thisdict.items())
l.sort()
print('Ascending order is',l)
l=list(thisdict.items())
l.sort(reverse=True)
print('Descending order is',l)
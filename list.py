l=[10,20,70,30,50,200,210]
print(l)
print(l[0:7:2]) #sliceing
l.insert(2,100)
print(l) #insertion
l.sort()
print(l) #sorting
l.reverse() #reverse
print(l)
l.remove(100) #remove one element
print(l)
del l[0] #delete one element
print(l)
l.append(100) # add one element at the end
print(l)
l.extend([110,120]) #add a list add the end
print(l)
l.clear() #Clear the list
print(l)
#set we use{}
A= {1,2,3,4,4,4,5,6,5,6,7,8,9}
print(A)

print(len(A))

A.add(10) #run on console, if you'll add same value another time it will show same data
A.update([19,20,12,11]) #run on console
A.remove(1) #run on console, it will throw error if number is not there
A.discard(2) #run on console, it will not throw error if number is not there
A.pop() #run on console, it will come up with any random value not as list that it will give you last number


C=set(('Mac','tom','dick','harry')) #if you use set(()) than you can use commom bracket
print(C)

D=set([1,2,3,4,4]) #if you use set([]) than you can use commom bracket
print(D)


X={2,3,4,5,6,7}
Y={1,2,3,9,8,19}

#union = | = mix of both

print(X|Y)
print(X.union(Y))

#Intersection = & = common in them

print(X&Y)
print(X.intersection(Y))

#Difference = - = what is not in 2nd and not same
print(X-Y)
print(X.difference(Y))

print(Y-X)
print(Y.difference(X))

#symmetric difference = ^ = what diff in both
print(X^Y)
print(X.symmetric_difference(Y))


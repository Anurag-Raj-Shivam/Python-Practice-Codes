#List is an order set of value and it allows us to put many values in single Variable

"""in this
x= variable
3,5,6,4,8,67,34,1 = elements
[] = index(it always start with 0"""

x = [3,5,6,4,8,67,34,1]
print(x[0])
print(x[4])
print(max(x))
print(len(x))
print(x.pop())
print(x[0:5])
(x.insert(6,'Don'))
(x.remove(8))
print(x)


y = [3,5,6,4,8,67,34,1]
print(y.pop())
y.sort()
y.reverse()
y.append(67)
y.copy()
y.count(37)
y.clear()

"""z = [3,5,6,4,8,67,34,1]
del z
print(z[0])"""


#Tupples are a little similar to list it means they
#are used to store the collections of elements in single variable but
#but as list tupple once created they cannot be changed or there content cannot be change
#.append will not work
z=(5,6,7,8,9,9,9,9,1,23,60)
print(z)
print (z[3])
print(z.count(9))    #.count = how many same numbers in one list
print(len(z))


m=(2,'BOT', 'HOT', 9,10,26)
n=(1,4,55,46,6,3,55,3,40)
o=m+n
print(o)


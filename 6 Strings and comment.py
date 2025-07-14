# String and Comment
"""String
and
Comment"""

# this we use for 1 line
"""This
we
use
for
multiple
line"""

#\ this we use to remove power of any comma or escape from any character


x="hello's world"
y='hello\'s world'

print (x.capitalize())
print(y.capitalize())


x="hello's world"
y='hello\'s world'

print (x[5])
print(y[9])

"""[] this we use as index by this we can call the
word which is on that place and by this we can do slicing as well"""

x="hello's world"
y='hello\'s world'

print (x[0:7])
print(y[2:11])


#use of .islower & .isupper these both says true or false & .replace

x="hello's world"
y='hello\'s world'

print (x.islower())
print(y.isupper())
print(x.replace("h","x"))

#to duplicate the value

x="hello world "
y='hello\'s world '

print (x * 5)
print (y * 5)
print(x*3+y*3)
print((x+y)*3)
print((x + y + "\n") * 4)   #"\n" this we use for new line
print((x+"\n")*2+(y+"\n")*4)
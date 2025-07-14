#in slice every counting start from 0

a=[0,1,2,3,4,5,6,7,8,9]         #list
b=(0,1,2,3,4,5,6,7,8,9)         #tupple
c='0123456789'                  #string
x= slice(0,5)


#all 3 are same
print(a[x])
print(a[0:5])
print(a[:5])


print(b[4:]) #as nothing in end so it will go from 5 number to end

print(a[:6])  #as nothing in start so it will start from o and go till 6th value

#only : this gives whole value
print(a[:])
print(b[:])
print(c[:])

#if i want evey 2nd value from the list in a , b or c- all 3 same ans
print(a[0:10:2])
print(a[:10:2])
print(a[::2])

#if i want evey 3nd value from the list in a , b or c
print(a[0:10:3])
print(a[:10:3])
print(a[::3])


e=(4,7,6,3,1,5,0,7,8,9)
  #0 1 2 3 4 5 6 7 8 9
#-10-9-8-7-6-5-4-3-2-1

print(e[-1])
print(e[-5])
print(e[::-1]) #it will give you reverse value of e #(9, 8, 7, 0, 5, 1, 3, 6, 7, 4)
print(e[:-3:-1]) #(9, 8)
print(e[-3::-1]) #(7, 0, 5, 1, 3, 6, 7, 4)

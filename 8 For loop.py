#for Loop

A =[0,1,2,4,5,7,8.9] #list
B ={1,2,4,6,7,8,9}   #set
C =(0,1,2,3,4,5,6,7,8,9) #tuple
D ='01234 is Password of Abu' #string
E ={'Name':'max','age':20} #dictionary

for word in A:  #at pace of word you can choose anything
    print(word)

for word in B:
    print(word)

for word in C:
    print(word)

for word in D:
    print(word)

for word in D:
    print(word, end="")

for word in E:
    print(word) #but this will not print whole E.

for word in E.values(): #it will only provide dictionary value
    print(word)

for key,value in E.items():
    print(key, value)

for words in range(4,22):
    print(words)

for words in range(4,22,5):
    print(words)

else:
    print("Finished")
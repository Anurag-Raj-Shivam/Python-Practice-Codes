print('Rahul',98, 68,58)        #this will give a normal value with space

print('Hina',18,20,22,sep='')    #this will give a value without space because we use sep=''

print('Hina',18,20,22,sep=',,,,')   #this will give a value with 3 comma because we put it between sep=''

print('Hina',18,20,22,sep='\n')   #this will give a value under line because we use \n


print('Rahul',98, 68,58,end='')   #this both print value give result in one line because of end=''
print('Hina',18,20,22)


print('Rahul',98, 68,58,end='------')   #this both print value give result in one line because of end='----'
print('Hina',18,20,22)




#this both print value give result in underline till 2nd last value of 1st print then it will come again in 1 line
print('Rahul',98, 68,58,sep='\n',end='----')
print('Hina',18,20,22)
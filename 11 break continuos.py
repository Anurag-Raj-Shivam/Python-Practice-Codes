#continous

a=[0,1,2,3,4,5]
for numbers in a:
    if numbers==2:
        continue  #in this for loop continus will not run
    print(numbers) # the given word apart it will run all



print('nnnnnnnnnnnn')

i=0
while i<9:
    if i==4:
        continue   #in this while loop continus will not run
    print(i)       #the given word till moving forward
    i+=1

print("breKKKKKK")

#break

z=[3,4,5,6,7,8,9,22,33]

for num in z:
    if num==7:
        break #ye har galat term tak run karega but jaise hi
              #ye num==7 sahi hoga ye run karna chod dega
    print(num)


b = (1,2,3,4,5,6,7)
for nun in b:
    if nun >=3:
        break#ye har galat term tak run karega but jaise hi
              #ye nun>=3 sahi hoga ye run karna chod dega
    print(nun)

    i = 0
    while i < 9:
        if i == 4:
            break
        print(i)
        i += 2
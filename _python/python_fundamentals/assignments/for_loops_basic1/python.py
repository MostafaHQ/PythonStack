for num in range(151):
    print(num)

for num in range(5,1_000,5):
        print (num)

for num in range(1,101,1):
    if num%10==0:
        print ("Coding Dojo")
    elif num%5==0:
        print ("Coding")
    else: 
        print (num)

sum = 0
for num in range(500000):
    if num%2!=0:
        sum = sum+num
print(sum)

for num in range(2018,0,-4):
    print(num)

lowNum=1
highNum=100
mult=3
for num in range(lowNum,highNum):
    if num % mult==0:
        print(num)
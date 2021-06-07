#1. Basic
for x in range(0, 151):
    print(x)

#2. Multiples of 5
for x in range(5, 1005, 5):
    print(x)

#3. Counting the Dojo Way
for x in range(1, 100):
    if (x%5==0):
        print("Coding")
    if (x%10==0):
        print("Coding Dojo")
    else:
        print(x)
#4.
sum = 0
for x in range(1, 500000, 2):
    sum+= x

print(sum)

#5.
for x in range(2018, 0, -4):
    print(x)

#6.
lowNum = 2
hiNum = 9
mult = 3
x=0
while x < hiNum:
    x = x+3
    print(x)
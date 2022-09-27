num = 1

while num < 1000:
    print("\n While Loop Iteration: " + str(num))
    
    for i in range(2):
        print("For Loop Iteration: ", str(i))
        
    num += 1

# start at 1
# take  starting number ** 3
# take number increase value by 1
# run it again
# end when sum of **3 = 1000

list=[1,2,3,4,5,6,7,8,9,10]

popped = list.pop(0)
cubed = popped**3
if cubed <= 1000:
    print(cubed)

else:
    print("Done")
print(cubed)

for num in range(2,101):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)

num_list = []

for num in range(1, 11):
    cubed = num**3
    num_list.append(cubed)
for cubed in num_list:
    print(cubed)


for number in range (2,101):
    count = 0
    for i in range(2, (number//2 +1)):
        if(number % i == 0):
            count += 1
            break
    if(count == 0 and number != 1):
        print(" %d" %number, end=" ")
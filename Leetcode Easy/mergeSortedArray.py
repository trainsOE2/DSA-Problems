# num1 = [1, 6, 12, 0, 0, 0, 0, 0, 0, 0]
# m = 3
# num2 = [2, 3, 4, 8, 9, 15, 20]
# n = 7


num1 = [2, 0]
m = 1
num2 = [1]
n = 1


# num1 = [0]
# m = 0
# num2 = [1]
# n = 1

i=m-1
j=n-1

while(j>=0 and i>=0):
    
    if num2[j] > num1[i]:
        num1[i+j+1] = num2[j]
        j -= 1
    else:
        num1[i+j+1] = num1[i]
        num1[i] = 0
        i-=1

if i == -1:
    for k in range(j + 1):
        num1[k] = num2[k]

print(num1)




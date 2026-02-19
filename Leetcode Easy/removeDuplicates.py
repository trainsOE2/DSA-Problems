#nums = [1,1,2]
#nums = [1, 1]
# nums = [1]
#nums=[1,1,2]
#nums = [1, 2, 2, 3, 4]
#nums = [1,1,2,3]
nums = [0,0,1,1,1,2,2,3,3,4]

newIndex = 0
i=0
lastIndex = len(nums)-1

if(lastIndex == 0):
  print(nums)
  print(lastIndex)

while ( i <= lastIndex-1):
  if(nums[i] != nums[i+1]):
    if(newIndex == 0):
        newIndex = i+1
    nums[newIndex] = nums[i+1]
    newIndex += 1
    i += 1
  else:
    if(i == 0):
        newIndex = 1
    i += 1

print(nums)
print(newIndex)
    
    

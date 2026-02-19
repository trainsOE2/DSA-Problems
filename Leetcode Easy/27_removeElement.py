nums = [0,1,2,2,3,0,4,2]
val = 2

corr = []
for item in nums:
    if(item != val):
        corr.append(item)

# print(corr)
# print(nums)

i = 0
for item in corr:
    nums[i] = item
    # print("i: ", i)
    # print("item: ", item)
    # print(nums)
    i = i+1

print(corr)
print(len(corr))
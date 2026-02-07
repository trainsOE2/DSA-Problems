class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

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

        return len(corr)
nums_str = input("请输入：").split(" ")
print(nums_str)
nums = []
for a in nums_str:
    nums.append(int(a))
count = len(nums)
for i in range(0, count - 1):
    for j in range(count - 1 - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(nums)
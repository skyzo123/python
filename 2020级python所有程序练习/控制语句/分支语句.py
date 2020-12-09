
nums = [2, 5, 9, 14, 56, 79, 92, 100]
low = 0
high = len(nums) - 1
n=int(input("Enter:"))
while low <= high :
    mid = (low + high) // 2
    if n == nums[mid]:
        print("输入的数字在列表中！")
        break
    elif n > nums[mid]:
        low = mid + 1
    else:
        high = mid - 1
if low >high:
        print("输入的数字不在列表中！")




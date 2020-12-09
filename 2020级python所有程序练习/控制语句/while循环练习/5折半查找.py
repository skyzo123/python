def func(n, nums):
    low = 0
    high = len(nums) - 1
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



nums_list = [2, 5, 9, 14, 56, 79, 92, 100]
num = int(input("请输入一个数字，判断在不在列表中："))
func(num, nums_list)
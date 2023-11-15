
def quicksort(nums):
    if len(nums) <= 1:
        return nums
    sel = nums[0]
    left = []
    right = []

    for i in range(1,n):
        if nums[i] <= sel:
            left.append(nums[i])
        else:
            right.append(nums[i])
    
    return left + sel + right

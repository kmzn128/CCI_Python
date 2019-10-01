def centered_average(nums):
    min = max = nums[0]
    min_i = max_i = 0
    for i in range(1, len(nums)):
        if(min > nums[i]):
            min = nums[i]
            min_i = i
        if(max < nums[i]):
            max = nums[i]
            max_i = i
    a = (sum(nums)-min-max)
    b = (len(nums)-2)
    return a/b

print(centered_average([1, 2, 3, 4, 100])) 
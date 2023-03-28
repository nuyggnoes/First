def subsets(nums):
    n = len(nums)
    res = []
    for i in range(2**n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(nums[j])
        res.append(subset)
    return res

a = [1,2,3,4]
print(subsets(a))
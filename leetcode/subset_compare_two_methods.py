import time

nums = [i for i in range(20)]


def subset(nums, res, start, temp):
    if start == len(nums):
        res.append(temp[:])
        return
    subset(nums, res, start + 1, temp)
    subset(nums, res, start + 1, temp + [nums[start]])

res  = []
start_time = time.time()
subset(nums, res, 0, [])
end_time = time.time()
print(end_time - start_time)

def subset2(nums, res, start, temp):
    res.append(temp[:])
    for i in range(start, len(nums)):
        subset2(nums, res, i + 1, temp + [nums[i]])

res  = []
start_time = time.time()
subset(nums, res, 0, [])
end_time = time.time()
print(end_time - start_time)

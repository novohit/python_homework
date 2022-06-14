nums = input().split()
nums = [int(nums[i]) for i in range(len(nums))]
target = eval(input())
lens = len(nums)
x = -1
for i in range(lens):
    if (target - nums[i]) in nums:
        if (nums.count(target - nums[i]) == 1) and (target - nums[i] == nums[i]):
            continue
        else:
            x = nums.index(target - nums[i], i + 1)
            break
if x > 0:
    print('{} {}'.format(i, x))
else:
    print('Fail')
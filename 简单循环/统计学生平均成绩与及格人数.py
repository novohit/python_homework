nums = list(map(int, input().split()))
count = 0
sum = 0
for num in nums:
    if num >= 60: count += 1
    sum += num
print('average =', sum / len(nums))
print('count =', count)
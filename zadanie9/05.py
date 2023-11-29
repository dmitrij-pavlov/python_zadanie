n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
for i in range(len(nums)):
    if len(nums) - i == 1:
        break
    print(nums[i] + nums[i + 1])
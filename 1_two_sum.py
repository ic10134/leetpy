# Given a list of integers, return indices of the numbers
# such that they add up to a specific target.
# 
# Added couple of twists to the leetcode problem.
# 
# Twist1: More than two indices can be summed
# Twist2: More than one result set possible
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

import ast

def find_combinations(nums, target, start, path, res)->list:
    if target == 0:
        res.append(path)
    else:
        for itr in range(start, len(nums)):
            if target >= nums[itr]:
                find_combinations(nums, target-nums[itr], itr+1, path+[itr], res)

def twoSum(nums:list, target:int)->list:
    res = []
    find_combinations(nums, target, 0, [], res)
    new_res = []
    for x in res:
        new_res.append(list(set(x)))
    return new_res

if __name__ == '__main__':
    nums = ast.literal_eval(input("Enter the elements of the array as list: "))
    target = int(input("Enter the target number: "))
    print(twoSum(nums, target))

# Sample execution
# Enter the elements of the array as list: [2,5,7,14]
# Enter the target number: 14
# [[0, 1, 2], [3]]
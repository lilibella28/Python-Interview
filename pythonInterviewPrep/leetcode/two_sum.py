"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


"""
nums = [2, 7, 11, 15]
target = 9


def two_sum(my_nums, target_num):
    values_dic = {}
    for num in range(len(my_nums)):
        target_value = target_num - my_nums[num]
        if target_value in values_dic:
            return [values_dic[target_value], num]
        else:
            values_dic[my_nums[num]] = num



print(two_sum(nums, target))

"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, NOAH YU and SAMUEL SUH, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: ny3259
UT EID 2: sjs5658
"""


def group_sum(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    # base case
    if start >= len(nums):
        # return t or f dependent on if sum = target
        return target == 0
    # decision we try and undo
    if group_sum(start + 1, nums, target - nums[start]):
        return True
    return group_sum(start + 1, nums, target)


def group_sum_6(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target. Additionally, if there is are 6's present in the array, they must all
    be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    # base case
    if start >= len(nums):
        # return t or f dependent on if sum = target
        return target == 0
    # make sure 6 is included
    if nums[start] == 6:
        return group_sum_6(start + 1, nums, target - nums[start])
    # decision we try and undo
    if group_sum_6(start + 1, nums, target - nums[start]):
        return True
    return group_sum_6(start + 1, nums, target)


def group_no_adj(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a value is chosen, the value immediately after
    (the value adjacent) cannot be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    # base case
    if start >= len(nums):
        return target == 0

    if nums[start] <= target:  # continues if less than target
        current = group_no_adj(start + 2, nums, target - nums[start])
        if current:
            return True

    skip = group_no_adj(start + 1, nums, target)
    return skip


def group_sum_5(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a multiple of 5 is in the array, it must be included
    If the value immediately following a multiple of 5 if 1, it must not be chosen

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    # base case
    if start >= len(nums):
        # return t or f dependent on if sum = target
        return target == 0
    # make sure 5 is included
    if nums[start] % 5 == 0:
        if start >= len(nums) - 1 or nums[start + 1] != 1:
            return group_sum_5(start + 1, nums, target - nums[start])
        else:  # all remaining instances are instances of 5,1 and the 1 should not be counted
            return group_sum_5(start + 2, nums, target - nums[start])
    # decision we try and undo
    if group_sum_5(start + 1, nums, target - nums[start]):
        return True
    return group_sum_5(start + 1, nums, target)


def group_sum_clump(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if there is a group of identical numbers in succession,
    they must all be chosen, or none of them must be chosen.
    EX: [1, 2, 2, 2, 5, 2], all three of the middle 2's must be chosen, or none of them must be
    chosen to be included in the sum. One loop is allowed to check for identical numbers.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """

    if start >= len(nums):
        return target == 0
    crt = nums[start]
    count = 1

    for i in range(start + 1, len(nums)):
        if nums[i] == crt:
            count += 1
        else:
            break

    if group_sum_clump(start + count, nums, target - crt * count):
        return True

    return group_sum_clump(start + count, nums, target)


def split_array(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    quota = sum(nums) / 2

    def helper(start, current):
        if quota == current:  # base case
            return True
        elif (
            start >= len(nums) or quota < current
        ):  # check if out of bounds or sum is too much
            return False
        else:
            if helper(start + 1, current + nums[start]):  # include current element
                return True
            else:
                return helper(start + 1, current)  # don't include current element

    return helper(0, 0)


def split_odd_10(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of one group must be odd, while the other group must be a multiple of 10
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """

    def helper(idx, group1, group2):
        if idx == len(nums):
            return (sum(group1) % 10 == 0 and sum(group2) % 2 == 1) or (
                sum(group2) % 10 == 0 and sum(group1) % 2 == 1
            )

        return helper(idx + 1, group1 + [nums[idx]], group2) or helper(
            idx + 1, group1, group2 + [nums[idx]]
        )

    return helper(0, [], [])


# redo sam?


def split_53(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Additionally, all multiples of 5 must be in one group, and all multiples of 3 (and not 5)
    must be in the other group
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    quota = sum(nums) // 2

    def helper(start, current):
        if quota == current:  # base case
            return True
        elif (
            start >= len(nums) or quota < current
        ):  # check if out of bounds or sum is too much
            return False
        else:
            if nums[start] % 5 == 0:  # include current element if multiple of 5
                return helper(start + 1, current + nums[start])
            elif nums[start] % 3 == 0:  # dont include element if multiple of 3
                return helper(start + 1, current)
            else:  # handle  all other numbers
                if helper(start + 1, current + nums[start]):
                    return True
                return helper(start + 1, current)  # don't include current element

    if len(nums) == 0 or sum(nums) % 2 != 0:  # handle empty lists and odd sum lists
        return False
    return helper(0, 0)

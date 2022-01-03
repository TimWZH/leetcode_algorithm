# Three types of two pointers algorithm:
# 1. Opposite direction (check palindrome)
# 2. Going backwards (longest palindrome)
# 3. Same direction

# 1. Opposite direction
#   1) Reverse 
#   2) Two Sum
#   3) Partition

# 2. Going backwards
#   1) Longest palindromic sbustring
#   2) Find K Closest Elements

# 3. Same direction
#   1) Sliding window
#   2) Fast & Slow Pointers

# 1. https://leetcode.com/problems/valid-palindrome/
def isPalindrome(self, s):
    if not s:
        return False
    left, right = 0, len(s) - 1
    while left < right:
        while left< right and not self.isValid(s[left]):
            left += 1
        while left < right and not self.isValid(s[right]):
            right -= 1
        if left < right and s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True

def isValid(self, char):
    return char.isdigit() or char.isalpha()

# 2. Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
def validPalindrome(self, s):
    if not s:
        return False
    
    left, right = self.findDeference(s,0,len(s) - 1)
    if left >= right:
        return True
    
    return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)

def isPalindrome(self, s, left, right):
    left, right = self.findDifference(s, left, right)
    return left >= right

def findDifference(self, s, left, right):
    while left < right:
        if s[left] != s[right]:
            return left, right
        left += 1
        right -= 1
    return left, right

# 3. Two Sum III
# Design and implement a TwoSum class. It should support the following operations: add and find.
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.
class TwoSum:
    def add(self, number):
        # write your code here
        return
    
    def find(self, value):
        # write your code here
        return -1

# solution 1: sorted list + two pointers
class TwoSum:
    def __init__(self) -> None:
        self.nums = []
    
    def add(self, num):
        self.nums.append(num)
        index = len(self.nums) - 1

        while index > 0 and self.nums[index - 1] > self.nums[index]:
            self.nums[index - 1], self.nums[index] = \
                self.nums[index], self.nums[index - 1]
            index -= 1

    def find(self, target):
        left, right = 0, len(self.nums) - 1
        while left < right:
            if self.nums[left] + self.nums[right] < target:
                left += 1
            elif self.nums[left] + self.nums[right] > target:
                right -= 1
            else:
                return True
        return False

# Solution 2 dict/HashMap
class TwoSum:
    def __init__(self) -> None:
        self.hashMap = {}
    
    def add(self, num):
        self.hashMap[num] += 1
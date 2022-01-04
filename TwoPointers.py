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
        self.hashMap[num] = self.hashMap.get(num,0) + 1
    
    def find(self, value):
        for num1 in self.hashMap:
            num2 = value - num1
            cnt = 2 if num2 == num1 else 1
            if self.hashMap(num2,0) >= cnt:
                return True
        
        return False

# 4. Three Sum
# Given an array S of n integers, are there there elements a, b, c
# in S such that a + b + c = 0?
# Elements in a triplet (a,b,c) must be in non-descending order
# The solution set must not contain duplicate triplets
def threeSum(self, nums,target):
    results = []
    if not nums or len(nums) < 3:
        return results
    
    nums.sort()

    length = len(nums)
    for i in range(0, length - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left = i + 1
        right = length - 1
        target -= nums[i]
        self.find_twoSum(nums,left,right,target,results)
    return results

def find_twoSum(self, nums, left, right, target, results):
    while left < right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            results.append([-target,nums[left], nums[right]])
            while left < right and nums[left+1] == nums[left]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
    

# 5. Triangle count
def triangleCount(self, nums):
    if not nums or len(nums) < 3:
        return 0

    length = len(nums)
    nums.sort()
    ans = 0
    for i in range(2,len(nums)):
        ans += self.get_trianlge_count(nums,i)
    
    return ans

# This is not a A + B = Target problem, which has O(n) time complexity, 
# but a A + B > Target problem, which has O(nxn) time complexity if all answers must be shown.
# In this problem however, we can do batch caculation using right - left, so it still has O(n) complexity.
def get_triangle_count(self, nums, i):
    left, right = 0, i - 1
    target = nums[i]
    cnt = 0
    while left < right:
        if nums[left] + nums[right] > target:
            cnt += right -left
            right -= 1
        else:
            left += 1
    
    return cnt


# 6. Four Sum II
# Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero
# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500.
# All integers are in the range of -2^28 to 2^28 - 1 and the result is guaranteed to be at most 2^31 - 1
def fourSumCount(self, A, B, C, D):
    dictionary = {}
    ans = 0
    if not A or not B or not C or not D:
        return 0
    for a in A:
        for b in B:
            dictionary[a+b] = dictionary.get(a+b,0) + 1
    
    for c in C:
        for d in D:
            ans +=dictionary.get(-c-d,0)
    
    return ans

# Partition
# 7. Partition Array
# Given an array nums of inegers and an int k, partition the array (i.e move the elements in "nums") such that:
# All elements < k are moved to the left, all elements >=k are moved to the right
# Return the partitioning index, i.e the first index inums[i] >=k
def partitionArray(self, nums, k):
    if not nums:
        return -1
    
    left, right = 0, len(nums) - 1
    while left <= right:
        while left <= right and nums[left] < k:
            left += 1
        while left <= right and nums[right] >=k:
            right -= 1
        
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    return left

# 8. Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.
# You are not necessary to keep the original order of positive integers or negative integers.
# Do it in-place and without extra memory.
def partition(self, nums):
    if not nums:
        return []
    
    left, right = 0, len(nums) - 1
    while left <= right:
        while left <= right and nums[left] < 0:
            left += 1
        while left <= right and nums[right] > 0:
            right -= 1
        
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    return left 

def rerange(self, A):
    neg_cnt = self.partition(A)
    pos_cnt = len(A) - neg_cnt
    left = 1 if neg_cnt > pos_cnt else 0
    right = len(A) - 2 if pos_cnt > neg_cnt else len(A) - 1
    self.interleave(A,left, right)

def interleave(self, A, left, right):
     while left < right:
        A[left], A[right] = A[right] - A[left]
        left += 2
        right -= 2

# 9. Sort Colors
# count the numbers of each color and then overwrite the origin list

# Solution 1
def sortColors(self, nums):
    if not nums:
        return nums
    cntR, cntW, cntB = 0,0,0
    for num in nums:
        if num == 0:
            cntR += 1
        elif num == 1:
            cntW += 1
        else:
            cntB += 1

    for i in range(len(nums)):
        if cntR > 0:
            nums[i] = 0
            cntR -= 1
        elif cntW > 0:
            nums[i] = 1
            cntW -= 1
        else:
            nums[i] = 2
    
    # cannot use the following code, num is iter, won't change original list
    # for num in nums:
    #     if cntR > 0:
    #         num = 0
    #         cntR -= 1
    #     elif cntW > 0:
    #         num = 1
    #         cntW -= 1
    #     else:
    #         num = 2

# Solution 2
def sortColors(self, nums):
    self.partition(nums, 1)
    self.partition(nums,2)

def partition(self, nums, k):
    if not nums:
        return nums
    left, right = 0, len(nums) - 1
    while left < right:
        while left < right and nums[left] < k:
            left += 1
        while left < right and nums[right] >=k:
            right -= 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right -1

# Solution 3
def sortColor(self,nums):
    zeroPointer = -1
    twoPointer = len(nums)
    i = 0

    while i < len(nums) and i < twoPointer:
        if nums[i] == 0:
            zeroPointer += 1
            nums[zeroPointer], nums[i] = nums[i], nums[zeroPointer]
        
        elif nums[i] == 2:
            twoPointer -= 1
            nums[twoPointer],nums[i] = nums[i], nums[twoPointer]
            i -= 1
        i += 1
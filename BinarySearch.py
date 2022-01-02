# 1. Simple Binary Search Template
def BinarySearch(self, nums, target):
    if not nums:
        return -1
    start, end = 0, len(nums) - 1
    while start + 1 < end:
        mid = start + (end - start) // 2
        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] == target:
            end = mid
            # ....
            # ....
        else:
            end = mid 

    if nums[start] == target:
        return start
    elif nums[end] == target:
        return end

    return -1

# 2. Find first or last postion that satisfies conditions
# Given a big sorted array with positive integers sorted by ascending order. 

# The array is so big so that you can not get the length of the whole array directly, 
# and you can only access the kth number byArrayReader.get(k)(or ArrayReader->get(k) for C++). 

# Find the first index of a target number. Your algorithm should be in O(log k), 
# where k is the first index of the target number.

# Return -1, if the number doesn't exist in the array.
# Notice
# If you accessed an inaccessible index (outside of the array), ArrayReader.get will return2,147,483,647.

# Example
# Given[1, 3, 6, 9, 21, ...], and target =3, return1.
# Given[1, 3, 6, 9, 21, ...], and target =4, return-1.
def SearchBigArray(self, reader, target):
    total_range = 1

    while total_range < target:
        total_range *=2
    
    start, end = 0, total_range

    while start + 1 < end:
        mid = start + (end - start) // 2
        if reader.get(mid) < target:
            start = mid
        elif reader.get(mid) == target:
            return 1
        else:
            end = mid

    if reader.get(start) == target:
        return start
    elif reader.get(end) == target:
        return end
    
    return -1;


# 3. Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. 
# The result should also be sorted in ascending order.
def kClosestNumber(self, nums, target, k):
    if not nums:
        return []
    
    
    start, end = 0, len(nums) - 1

    while start + 1 < end:
        mid = start + (end - start) // 2
        if nums[mid] < target:
            start = mid
        else:
            end = mid

    result = []
    for _ in range(k):
        if self.isLeftCloser(nums, target, start, end):
            result.append(start)
            start -= 1
        else:
            result.append(end)
            end += 1

    return sorted(result)

def isLeftCloser(nums, target, left, right):
    if left < 0:
        return False
    if right >= len(nums):
        return True
    
    if abs(nums[left] - target) <= abs(nums[right] - target):
        return True
    
    return False

# 4. Maximum Number in Mountain Sequence 
# Given a mountain sequence of n integers which increase firstly and then decrease (no equal value), 
# find the mountain top(Maximum).
def findMax(self, nums):
    if not nums:
        return -1
    
    start, end = 0, len(nums) - 1
    while start + 1 < end:
        mid = start + (end - start) // 2

        if nums[mid] < nums[mid + 1]:
            start = mid
        else:
            end = mid
    
    # if nums[start] < nums[end]:
    #     return nums[end]
    # return nums[start]
    return max(nums[start], nums[end])

# 5. Suppose a sorted array in ascending order is rotated at some pivot unknown to you forehand
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2)
# Find theminimum element. You can assume no duplicate exists in the array.
def findMin(self, nums):
    if not nums:
        return -1
    
    start, end = 0, len(nums) - 1
    if nums[start] < nums[end]:
        return nums[start]
    while start + 1 < end:
        mid = (start + end) // 2
        if nums[start] < nums[mid]:
            # if nums[mid] > nums[end]:
            #     start = mid
            start = mid
        else:
            end = mid
    
    return min(nums[start], nums[end])

# 6. Find particular value in a rotated sorted array using binary search once.
def search(self, nums, target):
    if not nums:
        return -1
    
    start, end = 0, len(nums) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if nums[mid] < nums[end]:
            if nums[mid] <= target <= nums[end]:
                start = mid
            else:
                end = mid
        else:
            if nums[start] < target < nums[mid]:
                end = mid
            else:
                start = mid

    
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    
    return -1

# Binary search on unsorted datasets
# 7. Find Peak Element
def findPeak(self, nums):
    if not nums:
        return -1
    
    start, end = 0, len(nums) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if nums[mid] < nums[mid + 1]:
            start = mid
        elif nums[mid] < nums[mid-1]:
            end = mid
        else:
            return mid

    if nums[start] > nums[end]:
        return start
    return end

# Binary search on result sets
# 8. Given n pieces of wood with length L[i] (integer array). 
# Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. 
# What is the longest length you can get from the n pieces of wood? 
# Given L&K, return the maximum length of the small pieces. The unit of length is centimeter. 
# The length of the woods are all positive integers, you couldn't cut wood into float length. 
# If you couldn't get >= k pieces, return 0.
def cutWood(self, L, k):
    if not L:
        return 0
    
    start, end = 1, min(max(L),sum(L)//k)

    if end < 1:
        return 0
    
    while start + 1 < end:
        mid = (start + end) // 2
        if self.get_count(L,mid) >= k:
            start = mid
        else:
            end = mid
    return end if self.get_count(L,end) >=k else start


def get_count(self,L, length):
    return sum(l // length for l in L)
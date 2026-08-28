"""
Given a rotated sorted array with no duplicates, find the index of target.

"""

def binarySearch(nums,target):
    low = 0
    high = len(nums)-1
    # result = -1

    while low <= high:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid

        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid-1
            else: 
                low = mid +1
        else:
            if nums[mid] < target <= nums[high]:
                low = mid+1
            else:
                high = mid -1

    return -1
   

if __name__ == "__main__":
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # target = 0
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # target = 3
    nums = [6, 7, 0, 1, 2, 4, 5]
    target = 6
    print(binarySearch(nums,target))

"""
approach:
main case - the input can be sorted in right or left from the mid , even after finding the sorted side the target may or may not present in that half
A-when the left side of mid is sorted to satisfy this use logic nums[low] < nums[mid]
A1- the target may here 
so if present to check nums[low] <= target < nums[mid]
now the high will be reduce to mid -1
A2-  the target maynot here
so in this case the target maybe in right side 
low will be mid+1
B- when the right side sorted
B1- target maybe here
to check nums[mid] < target <= nums[high]
yes - low = mid +1
B2 - target not in sorted side
high = mid-1


space complexity:
O(1) - as we are not using any extra space, we are just using the input list and a few variables to keep track of the indices.

time complexity:
O(log n) - as we are dividing the list into half each time, so the time complexity is logarithmic.
"""
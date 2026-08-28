"""
Given a sorted array with duplicates, return the number of times target occurs.
nums = [1, 2, 2, 2, 2, 3, 4]
target = 2
Expected: 4
"""

def binarySearch(nums, target,position):
    low = 0
    high = len(nums)-1
    result = -1
    while low <= high:
        mid =  (low+high)//2
        if nums[mid] == target:
            result = mid
            if position == "firstIndex":
                high = mid -1
            elif position == "lastIndex":
                low = mid +1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return result


if __name__ == "__main__":
    nums = [1, 2, 2, 2, 2, 3, 4]
    target = 2
    firstIndexV = binarySearch(nums, target,"firstIndex")
    lastIndexV = binarySearch(nums, target, "lastIndex")
    print(lastIndexV,firstIndexV)
    if (firstIndexV or lastIndexV) == -1:
        print(0)
    else :
        totalCount =  lastIndexV-firstIndexV+1
        print(totalCount)

"""
approach : need low or starting index, need last index point high = len(input1)-1, mid = low+high//2 usage of // is give number without decimal, as the elements in the list are orders, take the mid index compare the value if the mid element is value == target store the value and keep going right to see for last index with low = mid+1 in value == target this is for lastindex and for firstindex high = mid-1, if the mid element is greater > target then we modify the last index to (mid-1), if not low index is (mid+1), so this to loop through in while low <=high
then we get the  position of first and last and then using 
totalCount =  lastIndexV-firstIndexV+1 to get total count

space complexity:
O(1) - as we are not using any extra space, we are just using the input list and a few variables to keep track of the indices.

time complexity:
O(log n) - as we are dividing the list into half each time, so the time complexity is logarithmic.
two O(logN) process for two it will represented as O(logN) + Olog(N) = O(2logN) =O(log N)
"""
"""
Given a sorted array that may contain duplicates, return the first index where target occurs.
"""

def binarySearch(nums, target):
    low = 0
    high = len(nums)-1
    result = -1

    while low <= high:
        mid = (low + high)//2
        guess = nums[mid]
        if guess == target:
            result = mid
            high = mid -1
        elif guess > target:
            high = mid -1
        else:
            low = mid +1
        
    return result




if __name__ == "__main__":
    nums = [1, 2, 2, 2, 3, 4, 5]
    target = 2

    # nums = [1, 2, 2, 2, 3, 4, 5]
    # target = 4

    # nums = [1, 2, 2, 2, 3, 4, 5]
    # target = 6
    print(binarySearch(nums,target))


"""
approach : need low or starting index, need last index point high = len(input1)-1, mid = low+high//2 usage of // is give number without decimal, as the elements in the list are orders, take the mid index compare the value if the mid element is value == target store the value and keep going left to see for first index, if the mid element is greater > target then we modify the last index to (mid-1), if not low index is (mid+1), so this to loop through in while low <=high

space complexity:
O(1) - as we are not using any extra space, we are just using the input list and a few variables to keep track of the indices.

time complexity:
O(log n) - as we are dividing the list into half each time, so the time complexity is logarithmic.
"""
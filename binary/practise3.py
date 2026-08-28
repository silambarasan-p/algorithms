"""
Given a sorted array containing duplicates, return the last index where target occurs.

"""
def binarySearch(nums, target):
    low = 0
    high = len(nums)-1
    result = -1
    while low <= high:
        mid = (low+high)//2
        print(type(nums[mid]))
        if nums[mid] == target:
            result = mid
            low = mid+1
        elif nums[mid] > target:
            high = mid -1
        else:
            low = mid +1
        
    return result

if __name__ == "__main__":
    nums = [1,2,2,2,2,3,4]
    target = 2
    print(binarySearch(nums,target))
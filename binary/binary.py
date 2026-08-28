
def binarySearch(arry,item):
    low = 0
    high = len(arry)-1  #3

    while low <= high:
        #each time check the middle element 
        mid = (low + high )//2   
        print("mid",mid)
        guess = arry[mid]   # how to create alist using the index number
        print("guess",guess)
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid+1
    return None

if __name__ == "__main__":
    arry = [2,4,6,8]
    print(binarySearch(arry,6))
    print(binarySearch([1,3,4,5,6,7,8,10],6))
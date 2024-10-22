if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

# Map doesn't return a list. Instead, it returns an iterator object and since sort is an attribute of list object, we will get error so we used sorted function which accepts an iterable and return a sorted list and then reassign the result to the original name.
# Set function is a powerful tool to obtain unique values from a list. It automatically removes duplicates and returns a set object containing only the unique elements. We can then convert this set back into a list if needed.

a = sorted(list(set(arr)))      
if 2<= n <=10:
    print(a[-2])
        

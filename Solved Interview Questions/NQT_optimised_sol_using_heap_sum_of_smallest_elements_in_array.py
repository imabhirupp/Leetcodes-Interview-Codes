import heapq

def reduce_array(arr):
    # Convert list to a heap (min-heap)
    heapq.heapify(arr)
    
    while len(arr) > 1:
        # Extract the two smallest elements
        smallest = heapq.heappop(arr)
        second_smallest = heapq.heappop(arr)
        
        # Calculate their sum and add it back to the heap
        new_element = smallest + second_smallest
        heapq.heappush(arr, new_element)
        
        # Print the updated array
        print("Current array:", sorted(arr))

# Example usage
arr = [5, 3, 8, 2, 7, 1]
reduce_array(arr)

def add_smallest_elements(l):
    while len(l) > 1:
        # Sort the array to get the two smallest elements
        l.sort()
        
        # Add the two smallest elements
        smallest_sum = l[0] + l[1]
        
        # Remove the two smallest elements from the array
        l = l[2:]
        
        # Add the sum of the two smallest elements back to the array
        l.append(smallest_sum)
        
        # Print the array after each operation
        print(l)

# Example usage:
l = [4, 3, 7, 1, 5]
add_smallest_elements(l)

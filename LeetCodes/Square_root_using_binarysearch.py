# Python implementation to find square root of given number upto given precision using binary search.

def squareRoot(number, precision):

    start = 0                                    # starting from 0 to check the probable numbers, 1x1 or 2x2 or 3x3 or 4x4 etc
    end, ans = number, 1                         # end will always be the number and the minimum answer can be 1

    
    while (start <= end):                        # A loop which will iterate tills it reaches the end or breaks due to the given conditions
        mid = int((start + end) / 2)             # Getting the mid value to find the exact number for the square root


# Eg : 28
# 1-28, mid = 14, now we will check if 14x14 = 28
# if not then again find the mid from 1-14 since any number greater than 14 wouldn't be the answer since 14x14 > 28
# now mid = 7, if 7x7 == number, if not then again repeat the same

        
        if (mid * mid == number):                # Checking if the mid == the given number
            ans = mid
            break                                # If yes then break

       
        if (mid * mid < number):                 # If mid*mid < number
            start = mid + 1                      # Incrementing start by mid + 1, for eg: 28, mid = 5, 5x5 < 28 therefore now start will be 5 and end will 6 since 6x6 > 28
            ans = mid

      
        else:
            end = mid - 1                        # If mid*mid > number, then end = mid -1, eg: 28, mid = 7, 7x7 > 28 therefore, end will be mid-1 that is 6 because numbers > 7 cannot be a square of 28

    # For computing the fractional part
    # of square root upto given precision
    increment = 0.1                              # For precision we increment by 0.1
    for i in range(0, precision):                
        while (ans * ans <= number):             # if ans*ans <= number then we increment the ans by 0.1
            ans += increment

        # loop terminates when ans * ans > number
        ans = ans - increment                    # When ans*ans > number then the loop ends and ans is decremented by 0.1 again to get the exact value 
        increment = increment / 10               # The increment is divided by 10 to get the precised answer in more than 2 decimal places

    return ans


# Driver code
print(round(squareRoot(50, 3), 4))
print(round(squareRoot(10, 4), 4))

def birthdayCakeCandles(candles):
    """ Counts the frequency of maximum number """
    # Write your code here
    # candles.sort()
    # print(candles)
    candles.sort() # arranging the elements of the array
    max_value = candles[-1] # Finding the max value
    count = 0
    
    for num in range(0, len(candles)):
        if candles[num] == max_value:
            count += 1
    
    return count


print(birthdayCakeCandles([4, 4, 1, 3]))
print(birthdayCakeCandles([3, 2, 1, 3]))        

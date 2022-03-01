def miniMaxSum(arr):
    """ Minimum sum is sum of first 4 digits
    Maximum sum is sum of index 1 to 5th index sum
    """
    # Write your code here
    arr.sort()
    # print(arr)
    series_1 = arr[0:-1]
    # print(series_1)
    
    series_2 = arr[1:]
    # print(series_2)
    
    number1 = sum(series_1)
    number2 = sum(series_2)
    
    print(number1, number2) 
    

miniMaxSum([1, 2, 3, 4, 5])

def staircase(n):
    # Write your code here
    space = '*'
    
    for num in range(1, n +1):
        print(' '*(n - num) + (num * '#'))
        

staircase(6)

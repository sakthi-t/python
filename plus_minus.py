def plusMinus(arr):
    positive = []
    negative = []
    zero = []
    for num in arr:
        if num > 0:
            positive.append(num)
        elif num < 0:
            negative.append(num)
        else:
            zero.append(num)
    
    print(len(positive) / len(arr))
    print(len(negative) / len(arr))
    print(len(zero) / len(arr))
    

plusMinus([-4, 3, -9, 0, 4, 1])

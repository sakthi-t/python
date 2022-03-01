 # The function accepts following parameters:
#  1. INTEGER s (starting point of house)
#  2. INTEGER t (Endign point of house)
#  3. INTEGER a (apple tree is at point a)
#  4. INTEGER b (orange tree is at point b)
#  5. INTEGER_ARRAY apples (array of apples)
#  6. INTEGER_ARRAY oranges (array of oranges)
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    m = len(apples)
    n = len(oranges)
    
    landing_apple = [] # contains a + apples
    landing_orange = [] # contains b + oranges
    
    sum_apples = 0 # Used inside for loop to sum a + apple
    sum_oranges = 0 # used inside for loop to sum b + orange
    
    apple_between_range = 0
    orange_between_range = 0
    
    for apple in apples:
        sum_apples = a + apple
        landing_apple.append(sum_apples)
        
    for orange in oranges:
        sum_oranges = b + orange
        landing_orange.append(sum_oranges)
    
    # print(landing_apple)
    # print(landing_orange)
    
    for apple in landing_apple:
        if apple in range(s, t+1):
            apple_between_range += 1
            
    for orange in landing_orange:
        if orange in range(s, t+1):
            orange_between_range += 1
            
    print(apple_between_range)
    print(orange_between_range)

countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])

def count_integers(lst):
    hashmap = {}
    
    for num in lst:
        hashmap[num] = hashmap.get(num, 0) + 1
        
    return hashmap



numbers = [1, 2, 3, 1, 4, 2, 3]

count_numbers = count_integers(numbers)

for key, val in count_numbers.items():
    print("%s : %s" % (key, val))
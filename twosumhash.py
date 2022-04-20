def two_sum_hash(arr, target):
    hash_map_arr = {}
    for p in range(len(arr)):
        if target - arr[p] in hash_map_arr:
            return [hash_map_arr[target - arr[p]], p]
        else:
            hash_map_arr[arr[p]] = p
           
    return -1


print(two_sum_hash([2, 7, 11, 15], 9))
print(two_sum_hash([3, 2, 4], 6))
print(two_sum_hash([3, 3], 6))
print(two_sum_hash([1, 3, 7, 9, 2], 11))
print(two_sum_hash([2, 8, 12, 15], 20))
# Finding two sum, it is a very naive solution
# Works well only for consecutive numbers


numbers = [3, 2, 4]

target = 6

final_indices = []

i = 1

two_sum = []

for num in range(len(numbers)):
    if i < len(numbers):
        # print(numbers[i])
        
        add_numbers = numbers[num] + numbers[i]
        two_sum.append(add_numbers)
        
        if add_numbers == target:
            final_indices.append(num)
            final_indices.append(i)
            

        i += 1
    # print(numbers[num])
# print(two_sum)
# print(i)

# print(final_indices)


def twosum(nums, target):
    final_indices = []
    i = 1
    
    for num in range(len(nums)):
        if i < len(nums):
        
            add_numbers = nums[num] + nums[i]  
            
            if add_numbers == target:
                final_indices.append(num)     
                final_indices.append(i)     
                
            
            i += 1
            
            
    return final_indices


print(twosum([3, 2, 4], 6))
print(twosum([2, 7, 11, 15], 9))
print(twosum ([3, 3],6))
def longestConsecutive(nums) -> int:
        
    if not nums:
        return 0
    
    
    length = 0
    count = 1

    nums = sorted(set(nums))
    
    for i in range(0, len(nums)-1):
        if nums[i+1] - nums[i] == 1:
            count+=1
        else:
            count = 1
            
        length = max(length, count)
        
    return max(length, count)


max_length = longestConsecutive(nums=[100,4,200,1,3,2])
print(max_length)


    

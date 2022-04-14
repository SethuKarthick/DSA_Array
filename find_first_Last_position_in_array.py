def searchRange(nums, target):
    i = 0
    from_to = []
    
    while i < len(nums):
        if nums[i] == target:
            from_to.append(i)
        i+=1
        
    return [min(from_to), max(from_to)] if len(from_to) else [-1, -1]


find_positions = searchRange(nums=[5, 7, 7, 8, 8, 10], target=8)
print(find_positions)
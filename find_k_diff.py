def findPairs(nums, k) -> int:
        
        
    res = []
        
    nums.sort()
    
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[j] - nums[i] > k:
                break
            if nums[j] - nums[i] == k:
                res.append(str(nums[i]) + str(nums[j]))
                
    return len(set(res))
                
                
                    
    

diff = findPairs(nums=[1,3,1,5,4], k=0)
print(diff)
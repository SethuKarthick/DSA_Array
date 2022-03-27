class Solution:
    def threeSum(self, nums: list) -> list:
        
        if not nums:
            return []
        
        nums.sort()
        triplets = []
        print(nums)
        count = len(nums)
        
        for i in range(count-2):
            left_idx = i+1
            right_idx = len(nums) - 1
            
            current_sum = nums[i] + nums[left_idx] + nums[right_idx]
            
            while left_idx < right_idx:
                if  current_sum == 0:
                    triplets.append([nums[i], nums[left_idx], nums[right_idx]])
                    left_idx += 1
                    right_idx -= 1
                    
                elif current_sum < 0:
                    left_idx += 1
                    
                elif current_sum > 0:
                    right_idx -= 1
                    
        return triplets

print(Solution().threeSum(nums=[0,0,0,0]))
                    
                    
            
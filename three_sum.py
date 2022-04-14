# input  array of intergers 

array = [12, 3, 1, 2, -6, 5, -8, 6]

# output return the possible triplets comminations that sums to target value

target_sum = 0

def find_triplets_sum(array, target_sum):
    array.sort()
    triplets = []

    for i in range(len(array)-2):
        left_idx = i+1
        right_idx = len(array) - 1

        while left_idx < right_idx:

            current_sum = array[i] + array[left_idx] + array[right_idx]

            if current_sum == target_sum:
                triplets.append([array[i], array[left_idx], array[right_idx]])
                left_idx += 1
                right_idx -= 1
            elif current_sum < target_sum:
                left_idx += 1
            elif current_sum > target_sum:
                right_idx -= 1

    return triplets

     
# possible_combinations = find_triplets_sum(array=array, target_sum=target_sum)

# print(possible_combinations)





class Solution:
    
    def threeSum(self, nums: list) -> list:
        
        nums.sort()
        
        triplets = []
        
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
                
            left_idx = i+1
            right_idx = len(nums) -1
            
            while left_idx < right_idx:
                current_sum = nums[i]+nums[left_idx]+nums[right_idx]
                
                if current_sum < 0:
                    left_idx += 1
                elif current_sum > 0:
                    right_idx -= 1
                    
                else:
                    triplets.append([nums[i], nums[left_idx], nums[right_idx]])
                    
                    while left_idx < right_idx and nums[left_idx] == nums[left_idx+1]:
                        left_idx += 1
                    while left_idx < right_idx and nums[right_idx] == nums[right_idx-1]:
                        right_idx -= 1
                    left_idx += 1
                    right_idx -= 1
                    
        return triplets 


Solution().threeSum(nums = [0,0,0,0])


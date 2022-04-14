# def fourNumberSum(array, targetSum):
#     # Write your code here.
#     res = []
	
#     for i in range(len(array)-4):
#         for j in range(i+1, len(array)-3):
#             goal = targetSum - array[i] - array[j]
#             begin = j+1
#             end = len(array) - 1
			
#             while begin < end:
#                 current_sum = array[begin] + array[end]
				
#                 if current_sum < goal:
#                     begin += 1
#                 elif current_sum > goal:
#                     end -= 1
					
#                 else:
#                     res.append([array[i], array[j], array[begin], array[end]])
#                     begin += 1
#                     end -= 1
#     return res


def fourNumberSum(array, target_sum):
    # Write your code here.
    all_pairs = {}
    quadruplets = []



    for i in range(1, len(array)-1):
        for j in range(i+1, len(array)):
            current_sum = array[i] + array[j]
            difference = target_sum - current_sum
            if difference in all_pairs:
                for pairs in all_pairs[difference]:
                    quadruplets.append(pairs + [array[i], array[j]])
        for k in range(0, i):
            current_sum = array[k] + array[i]
            if current_sum not in all_pairs:
                all_pairs[current_sum] = [[array[k], array[i]]]
            else:
                all_pairs[current_sum].append([array[k], array[i]])

    return quadruplets



quad = fourNumberSum(array=[7,6,4,-1, 1, 2], target_sum=16)
print(quad)
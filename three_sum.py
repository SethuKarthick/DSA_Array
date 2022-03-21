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

     
possible_combinations = find_triplets_sum(array=array, target_sum=target_sum)

print(possible_combinations)
# input array of intergers with duplicates. 
array = [2, 0, 1, 2, 2,0,0,0, 2, 3, 4, 2,0,0,'ehgf','s',3]
integer = 0
# output --> move the instances of given interger to the end of array. 
[2,1,2,2,2,3,4,2,'ehgf','s',3]  # the numbers 1, 3, 4 can be ordered differently

def move_to_end(array, gvn_integer):
    left_idx = 0
    right_idx = len(array) - 1

    while left_idx < right_idx:
        while left_idx < right_idx and array[right_idx] == gvn_integer:
            right_idx -= 1
        if array[left_idx] == gvn_integer:
            array[left_idx], array[right_idx] = array[right_idx], array[left_idx]    
        left_idx += 1
    return array

new_array = move_to_end(array=array, gvn_integer=integer)
print(new_array)


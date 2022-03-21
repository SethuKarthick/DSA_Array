

# input
array = [-4, 2, 3, 4, 5 ,6 , 8, 9]

# output 
# [4, 9, 16, 16, 25, 36, 64, 81]

def get_sorted_sqaured_array(array):
    squared_array = [x*x for x in array]
    squared_array.sort()
    print(squared_array)

# get_sorted_sqaured_array(array)

# Linear solution 


def get_sorted_squares(array):
    sorted_squares = [0 for _ in array]
    smaller_value_idx = 0
    larger_value_idx = len(array) - 1

    for idx in reversed(range(len(array))):
        small_value = array[smaller_value_idx]
        large_value = array[larger_value_idx]
        print(large_value)

        if abs(small_value) > abs(large_value):
            sorted_squares[idx] = small_value * small_value
            smaller_value_idx += 1
        else:
            sorted_squares[idx] = large_value * large_value
            larger_value_idx -= 1
    print(sorted_squares)


get_sorted_squares(array=array)
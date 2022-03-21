
# input
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

def is_monotonic(array):
    is_non_decreasing = True
    is_non_increasing = True

    for i in range (1, len(array)):
        if array[i] < array[i-1]:
            is_non_decreasing = False
        if array[i] > array[i-1]:
            is_non_increasing = False
        
    return is_non_decreasing or is_non_increasing


is_array_monotonic = is_monotonic(array=array)
print(is_array_monotonic)
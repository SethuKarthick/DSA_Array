# input 
array_1 = [-1, 5, 10, 20, 28, 3]
array_2 = [26, 134, 135, 15, 17]

# reference output 
# 28 from array_1 and 26 from array_2 is the pair which makes smallest_diff 
# [28, 26]

def find_smallest_diff(array_1, array_2):
    array_1.sort()
    array_2.sort()

    idx_one = 0
    idx_two = 0

    smallest = float('inf')
    current = float('inf')
    smallest_pair = []

    while idx_one < len(array_1) and idx_two < len(array_2):
        first_num = array_1[idx_one]
        second_num = array_2[idx_two]

        if first_num < second_num:
            current = second_num - first_num
            idx_one += 1
        elif second_num < first_num:
            current = first_num - second_num
            idx_two += 1
        else:
            return [first_num, second_num]

        if smallest > current:
            smallest = current 
            smallest_pair = [first_num, second_num]

    return smallest_pair

smallest_pair_array = find_smallest_diff(array_1=array_1, array_2=array_2)
print(smallest_pair_array)

    
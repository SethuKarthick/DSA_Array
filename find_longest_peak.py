from distutils.spawn import find_executable


def find_longest_peak(array):
    longest_peak = 0
    i = 1 
    while i < len(array)-1:
        is_peak = array[i] > array[i-1] and array[i] > array[i+1]
        if not is_peak:
            i += 1
            continue
        left_char = i-2
        while left_char >= 0 and array[left_char] < array[left_char+1]:
            left_char -=1 
        right_char = i+2
        while right_char < len(array) and array[right_char] < array[right_char-1]:
            right_char +=1 
        current_peak =  right_char-left_char-1
        longest_peak = max(longest_peak, current_peak)
        i = right_char
    return longest_peak

longest_peak = find_longest_peak(array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3])

print(longest_peak)
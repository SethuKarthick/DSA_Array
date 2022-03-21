array = [6, 1, 22, 25, 8, -1, 10, 11]
sequence = [1, 6, -1, 10]

def validate_sub_squence(array, sequence):
    array_index = 0
    sequence_index = 0
    while array_index < len(array) and sequence_index < len(sequence):
        if array[array_index] == sequence[sequence_index]:
            sequence_index += 1
        array_index += 1
    print(sequence_index == len(sequence))


validate_sub_squence(array=array, sequence=sequence)

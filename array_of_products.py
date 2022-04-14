def arrayOfProducts(array):
    # Write your code here.
	new_array = []
	for num in array:
		count = 1
		for j in range(len(array)):
			idx = array.index(num)
			if idx != j:
				count *= array[j]
				
		new_array.append(count)
	
	return new_array

new_array_list = arrayOfProducts(array=[5,1,4,2])
print(new_array_list)


def array_of_products(array):
    products = [1 for _ in range(len(array))]

    left_running_length = 1
    for i in range(len(array)):
        products[i] = left_running_length
        left_running_length *= array[i]

    right_running_length = 1
    for i in reversed(range(len(array))):
        products[i] *= right_running_length
        right_running_length *= array[i]

    return products
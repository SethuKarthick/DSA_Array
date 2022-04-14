def find_max_product(nums):

    max_product = min_product = nums[0]

    res = max_product

    for i in range(1, len(nums)):
        n = nums[i]

        temp = max(n, max_product*n, min_product*n)
        min_product = min(n, max_product*n, min_product*n)

        max_product = temp

        res = max(res, max_product)

    return res

max_product = find_max_product(nums=[2, 3, -2, 4])
print(max_product)
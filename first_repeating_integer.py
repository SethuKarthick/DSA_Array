def find_first_repeating_interger(nums):

    integers_count = {}

    for integer in nums:
        integers_count[integer] = integers_count.get(integer, 0) +1

        if integers_count[integer] > 1:
            return integer

    return -1

    

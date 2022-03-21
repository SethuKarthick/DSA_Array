# input 
coins = [5, 7, 1, 1, 2, 3, 22]

# min denomination amount that we cannot get. 
# sample input [1, 1, 4]
# min amount 3 we cannot make  

def find_min_change(array):
    array.sort()
    current_change_create = 0

    for coin in coins: 
        if coin > current_change_create+1:
            # print(current_change_create + 1)
            break
        current_change_create += coin
    print(current_change_create + 1 )

find_min_change(array=coins)
array_list = [1, 2, 2, 1, 7, 8]
target_num = 3
target_set_list = []

def two_sum(array_list, target_num):
    for i in range(len(array_list)-1):
        first_num = array_list[i]
        for j in range(i+1, len(array_list)):
            second_num = array_list[j]
            if first_num+second_num == target_num:
                target_set_list.append([first_num, second_num])
                
    print(target_set_list)


two_sum(array_list=array_list, target_num=target_num)
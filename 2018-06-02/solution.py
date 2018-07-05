def solver(num_list,k):
    n = len(num_list)
    for i in range(n):
        num = num_list[i]
        del num_list[i]
        if (k-num) in num_list:
            num_list.insert(i,num)
            return True
        num_list.insert(i,num)
    return False

arr = [2,4,5,12,1]
k = 8
print(solver(arr,k))
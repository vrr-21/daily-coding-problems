def solver_with_division(arr):
    # This is the solution without the follow-up.
    final_prod = 1
    for i in arr:
        final_prod = final_prod*i
    for i in range(len(arr)):
        arr[i] = final_prod/arr[i]
    return arr

def solver_wo_division(arr):
    # This is the solution with the follow-up.
    left_prod = [1] * len(arr)
    right_prod = [1] * len(arr)
    for i in range(1,len(arr)):
        left_prod[i] = arr[i-1] * left_prod[i-1]
    j = n-2
    while j>=0:
        right_prod[j] = arr[j+1] * right_prod[j+1]
        j = j-1
    prod = []
    for i in range(len(arr)):
        prod.append(left_prod[i] * right_prod[i])
    return prod

n = int(input())
ip_array = []
for i in range(n):
    ip_array.append(int(input()))
print(solver_wo_division(ip_array))
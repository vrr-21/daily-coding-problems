def solver(arr):
    max_sum = [0]*len(arr)
    max_sum[0] = arr[0]
    for i in range(1,len(arr)):
        if max_sum[i-1]+arr[i] > arr[i]:
            max_sum[i] = max_sum[i-1] + arr[i]
        else:
            max_sum[i] = arr[i]
    if max(max_sum) < 0:
        return 0
    return max(max_sum)

if __name__ == '__main__':
    print(solver([-5, -1, -8, -9]))
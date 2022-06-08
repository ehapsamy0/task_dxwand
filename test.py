
def countway(arr, l): 
    count = [0 for i in range(l)]
    sum_list = 0
    sum_list = sum(arr)
    if (sum_list % 3 != 0):
        return 0
    sum_list //= 3
    ts = 0
    for i in range(l - 1, -1, -1):
        ts += arr[i]
        if (ts == sum_list):
            count[i] = 1
    for i in range(l - 2, -1, -1):
        count[i] += count[i + 1]
    ans = 0
    ts = 0
    for i in range(0, l - 2):
        ts += arr[i]
        if (ts == sum_list):
            ans += count[i + 2]
    return ans
l = 5
arr = [2,2,4,0,4]
print(countways(arr, l))
 

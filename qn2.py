def rr1(arr,n):
    last = arr[-1]
    for i in reversed(range(n - 1)):
        arr[i + 1] = arr[i]
 
    arr[0] = last
def rr(arr, k,n):
    for i in range(k):
        rr1(arr,n)
arr = [1, 2, 3, 4, 5, 6, 7]
n=len(arr)
k = 3
rr(arr, k,n)
print(arr)

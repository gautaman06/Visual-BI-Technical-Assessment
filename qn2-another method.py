def rr(a, n, k):
    k = k % n
    for i in range(0, n):
        if(i < k):
            print(a[n + i - k], end = " ")
        else:
            print(a[i - k], end = " ")
a = [ 1, 2, 3, 4, 5 ,6 , 7] 
N = len(a)
K = 3
rr(a, N, K)

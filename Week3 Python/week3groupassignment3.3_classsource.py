import datetime as dt

memo = []

    
def fibonacciRecDP(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if memo[n-1] != -1:
        return memo[n-1]
    memo[n-1] = fibonacciRecDP(n-1) + fibonacciRecDP(n-2)
    return memo[n-1]

def fibonacciIter(n):
    arr = []
    arr.append(1)
    arr.append(1)
    for i in range(2, n):
        arr.append( arr[i-1] + arr[i-2])
    return arr[n-1]

def main():
    n = int(input("Enter the number: "))
    
    
    # bottom up approach
    begin_bu = dt.datetime.now()
    print(fibonacciIter(n))
    elap_bu = dt.datetime.now() - begin_bu
    print(f'Bottom up approach {elap_bu}')
    
    begin_rec = dt.datetime.now()
    for i in range(n):
        memo.append(-1)
    # top down recursive
    print(fibonacciRecDP(n))
    elap_rec = dt.datetime.now() - begin_rec
    print(f'Recursive approach {elap_rec}')
    

main()

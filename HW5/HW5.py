import sys
def max_zondor_coins(T, n, coins) :
#innit
    dp = [-float ('inf')] * (T + 1)
    dp [0] = 0
    for coin in coins:
        for value in range(T, coin - 1, -1): 
            for count in range(1,6):
                if value - coin * count >= 0:
                    dp [value] = max(dp[value], dp[value - coin * count] + count) 
            #recurrence
    return dp[T] if dp[T] != -float ('inf') else -1

if __name__ == "__main__":
    # Read input from standard input
    t, n = map(int, sys.stdin.readline().split())
    coins = list(map(int, sys.stdin.readline().split()))
    
    # Print input
    print(f"input:\n{t} {n}\n{' '.join(map(str, coins))}")
    
    # Compute result
    result = max_zondor_coins(t,n, coins)
    
    # Print output
    print(f"output:\n{result}")

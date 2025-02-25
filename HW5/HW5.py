import sys

def max_coins(target, denominations):
     # Initialize DP array where dp[i] stores max coins to sum up to i
    dp = [-1] * (target + 1)
    dp[0] = 0  # Base case: 0 coins to make sum 0
    
    for coin in denominations:
        for t in range(target, coin - 1, -1):
            if dp[t - coin] != -1 and dp[t - coin] < 5:
                dp[t] = max(dp[t], dp[t - coin] + 1)
    
    return dp[target]

if __name__ == "__main__":
    # Read input from standard input
    t, n = map(int, sys.stdin.readline().split())
    denominations = list(map(int, sys.stdin.readline().split()))
    
    # Print input
    print(f"input:\n{t} {n}\n{' '.join(map(str, denominations))}")
    
    # Compute result
    result = max_coins(t, denominations)
    
    # Print output
    print(f"output:\n{result}")

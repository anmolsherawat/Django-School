def minCut(s):
    n = len(s)
    dp = [0] * n
    palindrome = [[False] * n for _ in range(n)]

    for end in range(n):
        min_cut = end
        for start in range(end + 1):
            if s[start] == s[end] and (end - start <= 1 or palindrome[start + 1][end - 1]):
                palindrome[start][end] = True
                if start == 0:
                    min_cut = 0
                else:
                    min_cut = min(min_cut, dp[start - 1] + 1)
        dp[end] = min_cut
    return dp[-1]

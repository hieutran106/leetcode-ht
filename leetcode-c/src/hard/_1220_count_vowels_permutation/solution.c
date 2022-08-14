#define PRIME 1000000007

int countVowelPermutation(int n)
{
    if (n == 1)
    {
        return 5;
    }
    
    unsigned long dp[2][5] = {
        {1, 1, 1, 1, 1},
        {0, 0, 0, 0, 0}};

    for (int i = 1; i < n; i++)
    {
        int c = i % 2;
        int p = c == 1 ? 0 : 1;
        dp[c][0] = dp[p][1] % PRIME + dp[p][4] % PRIME + dp[p][2] % PRIME;
        dp[c][1] = dp[p][0] % PRIME + dp[p][2] % PRIME;
        dp[c][2] = dp[p][1] % PRIME + dp[p][3] % PRIME;
        dp[c][3] = dp[p][2] % PRIME;
        dp[c][4] = dp[p][2] % PRIME + dp[p][3] % PRIME;
    }
    int r_index = (n-1) % 2;
    unsigned long sum = 0;
    for (int i =0; i < 5; i++) {
        sum+= dp[r_index][i];
    }
    return sum % PRIME;
}
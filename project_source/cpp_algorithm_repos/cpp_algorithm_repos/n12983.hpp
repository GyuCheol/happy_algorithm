#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

int solution(vector<string> strs, string t)
{
    vector<int> dp(t.size() + 1);
    unordered_set<string> set(strs.begin(), strs.end());

    for (int i = 1; i <= 5; ++i)
    {
        if (i <= t.size() && set.find(t.substr(0, i)) != set.end())
        {
            dp[i] = 1;
        }
    }

    for (int i = 2; i <= t.size(); ++i)
    {
        int tmp = i - 1;

        if (dp[tmp] == 0)
        {
            continue;
        }

        for (int j = 1; j <= 5; j++)
        {
            if ((tmp + j) <= t.size() && set.find(t.substr(tmp, j)) != set.end())
            {
                if (dp[tmp + j] == 0)
                {
                    dp[tmp + j] = dp[tmp] + 1;
                }
                else
                {
                    dp[tmp + j] = min(dp[tmp + j], dp[tmp] + 1);
                }
            }
        }
    }

    return (dp[t.size()] == 0) ? -1 : dp[t.size()];
}


void do_test()
{
    // solution({ "app", "le" }, "apple");
    solution({ "ab", "na", "n", "a", "bn" }, "nabnabn");
}
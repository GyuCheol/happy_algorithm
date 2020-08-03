#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>
#include <unordered_set>

using namespace std;

vector<int> solution(vector<string> gems)
{
    unordered_set<string> allGems(gems.begin(), gems.end());
    unordered_map<string, int> gemMap;
    int min = 0x7fffffff;
    int min_start = 0;
    int min_end = 0;
    int start = 0;
    int end = 0;
    int cnt = 0;
    
    for (const string& g : allGems) {
        gemMap.insert(pair<string, int>(g, 0));
    }

    while (end < gems.size())
    {

        if (cnt < allGems.size())
        {
            if (gemMap[gems[end]] == 0)
            {
                ++cnt;
            }

            ++gemMap[gems[end]];
            ++end;
        }

        while (cnt == allGems.size())
        {
            if (min > (end - start))
            {
                min = end - start;
                min_start = start + 1;
                min_end = end;
            }

            if (gemMap[gems[start]] == 1)
            {
                --cnt;
            }

            --gemMap[gems[start]];
            ++start;
        }

    }

    return { min_start, min_end };
}

void do_test()
{
    solution({ "A", "B", "C" });
    solution({ "A", "B", "A", "A", "C", "A", "A", "B", "A", "B", "C" });
}
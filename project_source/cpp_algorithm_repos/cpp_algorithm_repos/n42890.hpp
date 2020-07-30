#include <cassert>
#include <string>
#include <vector>
#include <unordered_set>


using namespace std;

hash<string> hashing;

bool is_unique(vector<vector<string>>& relation, int columns)
{
    unordered_set<int> set;

    for (vector<string>& record : relation)
    {
        int tmp = 0;

        for (size_t i = 0; i < record.size(); i++)
        {
            if ((columns & (1 << i)) != 0)
            {
                tmp += hashing(record[i]);
                tmp <<= 1;
            }
        }

        if (set.find(tmp) == set.end())
        {
            set.insert(tmp);
        }
        else
        {
            return false;
        }
    }

    return true;
}

bool is_minimum(vector<int>& results, int columns)
{
    for (int result : results)
    {
        if ((result | columns) == columns)
        {
            return false;
        }
    }

    return true;
}


int solution(vector<vector<string>> relation)
{
    vector<int> results;
    size_t columns = relation[0].size();
    size_t limit = 1 << columns;

    for (size_t i = 1; i <= limit; i++)
    {
        if (is_minimum(results, i) && is_unique(relation, i))
        {
            results.push_back(i);
        }
    }

    return results.size();
}

void do_test()
{
    assert(2 == solution({ {"100", "ryan", "music", "2"}, {"200", "apeach", "math", "2"}, {"300", "tube", "computer", "3"}, {"400", "con", "computer", "4"}, {"500", "muzi", "music", "3"}, {"600", "apeach", "music", "2"} }));
}
#include <cassert>
#include <string>
#include <vector>
#include <list>

using namespace std;

inline void toLower(string& str)
{
    for (char& ch : str)
    {
        if (ch >= 'A' && ch <= 'Z')
        {
            ch += 32;
        }
    }
}

list<string>::iterator contain(list<string>& list, string& name)
{
    auto begin = list.begin();
    auto end = list.end();

    while (begin != end)
    {
        if ((*begin) == name)
        {
            return begin;
        }
         
        ++begin;
    }

    // not found
    return end;
}

int solution(int cacheSize, vector<string> cities)
{
    list<string> cacheList;
    int cost = 0;


    for (string& city : cities)
    {
        // to change into lower
        toLower(city);

        auto find = contain(cacheList, city);

        if (find != cacheList.end())
        {
            cost += 1;
            cacheList.erase(find);
        }
        else
        {
            cost += 5;
        }

        cacheList.push_back(city);

        if (cacheList.size() > cacheSize)
        {
            cacheList.pop_front();
        }
    }
    

    return cost;
}

void do_test()
{
    assert(50 == solution(3, {"Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"}));
    assert(20 == solution(0, {"A", "A", "A", "A"}));
}
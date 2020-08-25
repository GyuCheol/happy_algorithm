#include <iostream>
#include <string>
using namespace std;

bool check(string& s, int start, int end)
{
    int len = (end - start) / 2;

    for (int i = 0; i <= len; i++)
    {
        int left = start + i;
        int right = end - 1 - i;

        if (s[left] != s[right])
        {
            return false;
        }
    }

    return true;
}

int solution(string s)
{
    int answer = 1;

    for (int i = 0; i < s.size(); i++)
    {
        for (int j = answer + 1; j <= s.size() - i; j++)
        {
            if (check(s, i, i + j))
            {
                answer = j;
            }
        }
    }
    
    return answer;
}

void do_test()
{

}
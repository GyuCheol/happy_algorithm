#include <iostream>
#include <string>
using namespace std;

// call 메모리도 절약하기 위한 처절한 몸부림
inline bool check(string& s, int start, int end)
{
    int len = (end - start) / 2;

    for (int i = 0; i <= len; i++)
    {
        if (s[start + i] != s[end - 1 - i])
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

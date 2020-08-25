#include <iostream>
#include <math.h>

using namespace std;

// Top-down
int search(int n, int plus)
{
    int cnt = 0;
    int l = log(n) / log(3);
    int p = l * 2;

    if (n < 1 || p < plus)
    {
        return 0;
    }
    else if (n == 3 && plus == 2)
    {
        return 1;
    }

    if (n % 3 == 0 && plus >= 2)
    {
        cnt += search(n / 3, plus - 2);
    }

    cnt += search(n - 1, plus + 1);


    return cnt;
}

int solution(int n)
{
    return search(n - 2, 2);
}

void do_test()
{
    cout << solution(5) << endl;
    cout << solution(15) << endl;
    cout << solution(41) << endl;
    cout << solution(24) << endl;
    cout << solution(900000000) << endl;
    cout << solution(2147483647) << endl;
}
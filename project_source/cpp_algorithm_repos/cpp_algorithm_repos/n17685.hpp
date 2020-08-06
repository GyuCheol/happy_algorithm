#include <string>
#include <vector>
#include <algorithm>

using namespace std;

size_t getLengthIncluded(const string& a, const string& b)
{
    size_t compare = 0;

    while (compare < a.size() && a[compare] == b[compare])
    {
        ++compare;
    }

    return compare;
}

int solution(vector<string> words)
{
    vector<size_t> length(words.size());

    sort(words.begin(), words.end());

    for (size_t i = 0; i < words.size() - 1; i++)
    {
        string& a = words[i];
        string& b = words[i + 1];

        size_t compare = getLengthIncluded(a, b);

        length[i] = max(length[i], compare + (compare == a.size() ? 0 : 1));
        length[i + 1] = compare + 1;
    }

    size_t sum = 0;
    
    for (size_t i : length) {
        sum += i;
    }

    return sum;
}

void do_test()
{
    solution({ "war", "warrior", "word", "world" });
    solution({ "abc", "def", "hij", "k" });
    solution({ "go", "gone", "guild" });
}
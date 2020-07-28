#include <iostream>
#include <string>
#include <vector>
#include <regex>
#include <algorithm>

using namespace std;

const int INTERVAL = 'z' - 'Z';

regex re("([^\\d]+)(\\d+).*");


void toLower(string& str)
{
    for (char& ch : str)
    {
        if (ch >= 'A' && ch <= 'Z')
        {
            ch += INTERVAL;
        }
    }
}

class FileName
{
public:
    string originName_;
    string head_;
    int number_;

    FileName(string& str)
    {
        smatch match;

        regex_match(str, match, re);

        originName_ = str;
        head_ = match[1].str();
        number_ = stoi(match[2].str());

        toLower(head_);
    }

};

bool operator<(const FileName& a, const FileName& b)
{
    // head 비교 후, head가 같을 때만 number 비교 
    return a.head_ < b.head_ || (a.head_ == b.head_ && a.number_ < b.number_);
}

vector<string> solution(vector<string> files)
{
    vector<FileName> fileNames;
    vector<string> answer;

    answer.reserve(files.size());
    fileNames.reserve(files.size());
    
    for (size_t i = 0; i < files.size(); i++)
    {
        fileNames.push_back(FileName(files[i]));
    }

    stable_sort(fileNames.begin(), fileNames.end());

    for (FileName& file : fileNames)
    {
        answer.push_back(file.originName_);
    }

    return answer;
}

void do_test()
{

    vector<string> answer = solution({"img1", "ImG3.jpg", "imG2.zip", "img000.xyz"});

    for (string s : answer)
    {
        cout << s << endl;
    }

}
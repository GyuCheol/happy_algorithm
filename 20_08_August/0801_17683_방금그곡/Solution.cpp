#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

class MusicInfo
{
public:
    int play_time_;
    string title_;
    string melodies_;
    string stretched_melodies_;

    MusicInfo(int play_time, string title, string melodies)
        : play_time_(play_time), title_(title), melodies_(melodies)
    {
        stringstream ss;
        
        size_t cnt = (play_time + 1) / melodies.size();

        for (size_t i = 0; i < cnt; i++)
        {
            ss << melodies;
        }

        ss << melodies.substr(0, (play_time + 1) % melodies.size());

        stretched_melodies_ = ss.str();
    }

};

void replaceMelodies(string& m)
{
    string::iterator it = m.begin();

    while ((it + 1) != m.end())
    {
        if (*(it + 1) == '#')
        {
            m.erase(it + 1);

            switch (*it)
            {
            case 'C':
                (*it) = 'M';
                break;
            case 'D':
                (*it) = 'N';
                break;
            case 'E':
                (*it) = 'O';
                break;
            case 'F':
                (*it) = 'P';
                break;
            case 'G':
                (*it) = 'Q';
                break;
            case 'A':
                (*it) = 'R';
                break;
            }
        }
        else
        {
            ++it;
        }

    }
}

bool compare(const MusicInfo& a, const MusicInfo& b)
{
    return a.play_time_ > b.play_time_;
}

int getTimeValue(string info)
{
    int hour = stoi(info.substr(0, 2));
    int minute = stoi(info.substr(3, 5));

    return (hour * 60) + minute;
}

string solution(string m, vector<string> musicinfos)
{
    vector<MusicInfo> infoList;

    infoList.reserve(musicinfos.size());

    replaceMelodies(m);

    for (string& info : musicinfos)
    {
        int play_time = getTimeValue(info.substr(6, 5)) - getTimeValue(info.substr(0, 5));
        int comma_pos = info.find(',', 12);
        string title = info.substr(12, comma_pos - 12);
        string melodies = info.substr(comma_pos + 1, info.size() - comma_pos);

        replaceMelodies(melodies);

        infoList.push_back(MusicInfo(play_time, title, melodies));
    }

    stable_sort(infoList.begin(), infoList.end(), compare);

    for (MusicInfo& info : infoList)
    {
        if (info.stretched_melodies_.find(m, 0) != -1)
        {
            return info.title_;
        }
    }

    return "(None)";
}

void do_test()
{
    // cout << solution("AC#DE#ABC", { "12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF" }) << endl;
    // cout << solution("ABC#", { "12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF" }) << endl;
    cout << solution("ABCDEFG", {"12:00,12:14,HELLO,CDEFGAB", "13:00,13:35,WORLD,ABCDEFG"}) << endl;
}
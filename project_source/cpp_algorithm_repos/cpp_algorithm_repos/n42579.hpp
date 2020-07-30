#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Play
{
public:
    int id_;
    int play_;

    Play(int id, int play)
    {
        id_ = id;
        play_ = play;
    }
};

class Genre
{
public:
    string name_;
    int play_total_;
    vector<Play> play_list_;

    Genre(string name)
        : play_total_(0)
    {
        name_ = name;
    }

    void add_play(Play play)
    {
        play_list_.push_back(play);
        play_total_ += play.play_;
    }

};

bool compareGenre(Genre* a, Genre* b)
{
    return b->play_total_ < a->play_total_;
}

bool comparePlay(Play& a, Play& b)
{
    return (a.play_ == b.play_) ? a.id_ < b.id_ : b.play_ < a.play_;
}

vector<int> solution(vector<string> genres, vector<int> plays)
{
    unordered_map<string, Genre> genre_map;
    vector<Genre*> genreList;

    for (size_t i = 0; i < genres.size(); i++)
    {
        string& name = genres[i];
        unordered_map<string, Genre>::iterator genre = genre_map.find(name);

        if (genre == genre_map.end())
        {
            genre_map.insert(pair<string, Genre>(name, Genre(name)));
            genre = genre_map.find(name);
            genreList.push_back(&genre->second);
        }
        
        genre->second.add_play(Play(i, plays[i]));
    }

    vector<int> answer;
    sort(genreList.begin(), genreList.end(), compareGenre);

    for (Genre* genre : genreList)
    {
        sort(genre->play_list_.begin(), genre->play_list_.end(), comparePlay);

        for (size_t i = 0; i < min((size_t) 2, genre->play_list_.size()); i++)
        {
            answer.push_back(genre->play_list_[i].id_);
        }
    }

    return answer;
}

void do_test()
{
    solution({"classic", "pop", "classic", "classic", "pop"}, {500, 600, 150, 800, 2500});
}

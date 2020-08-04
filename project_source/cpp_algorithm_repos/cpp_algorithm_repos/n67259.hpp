#include <string>
#include <vector>
#include <queue>
#include <limits>
#include <iostream>

using namespace std;

int DIRECTION[4][2] = { {0, -1}, {0, 1}, {-1, 0}, {1, 0} };

class Step
{
public:
    int x_;
    int y_;
    int dir_;
    size_t cost_;

    Step(int x, int y, int dir, size_t cost) : x_(x), y_(y), dir_(dir), cost_(cost) {}
};

class Solution
{
private:
    queue<Step> queue_;
    vector<vector<int>> board_;
    int len_;
    // 동적 배열 활용 연습겸 재작성 len_ * len_ * 4 크기
    size_t ***costs_;
    // vector<vector<vector<int>>> costs_;
    

public:
    Solution(vector<vector<int>> board) 
        : board_(board), len_(board.size())
    {
        costs_ = new size_t**[len_];

        for (int i = 0; i < len_; ++i)
        {
            costs_[i] = new size_t*[len_];

            for (int j = 0; j < len_; ++j)
            {
                costs_[i][j] = new size_t[4] {0xffffffff, 0xffffffff, 0xffffffff, 0xffffffff};
            }
        }
    }

    ~Solution()
    {
        // 역으로 메모리 소멸
        for (int i = 0; i < len_; ++i)
        {
            for (int j = 0; j < len_; ++j)
            {
                delete[] costs_[i][j];
            }

            delete[] costs_[i];
        }

        delete[] costs_;
    }

    void search(Step step)
    {
        
        if (step.x_ < 0 || step.x_ >= len_ || step.y_ < 0 || step.y_ >= len_ || board_[step.y_][step.x_] != 0)
        {
            return;
        }

        if (step.cost_ < costs_[step.y_][step.x_][step.dir_])
        {
            costs_[step.y_][step.x_][step.dir_] = step.cost_;
            queue_.push(step);
        }

    }

    int get_min_cost()
    {
        search(Step(1, 0, 3, 100));
        search(Step(0, 1, 1, 100));

        while (queue_.empty() == false)
        {
            Step step = queue_.front();

            queue_.pop();

            for (size_t d = 0; d < 4; ++d)
            {
                search(Step(step.x_ + DIRECTION[d][0], step.y_ + DIRECTION[d][1], d, step.cost_ + (d == step.dir_ ? 100 : 600)));
            }
        }
        
        size_t m = costs_[len_ - 1][len_ - 1][0];

        for (size_t i = 1; i < 4; i++)
        {
            m = min(m, costs_[len_ - 1][len_ - 1][i]);
        }
        
        return m;
    }


};
int solution(vector<vector<int>> board)
{
    return Solution(board).get_min_cost();
}

void do_test()
{
    cout << numeric_limits<int>().max() << endl;

    // cout << solution({ {0, 0, 0}, {0, 0, 0}, {0, 0, 0} }) << endl;
    cout << solution({ {0, 0, 0, 0, 0, 0}, {0, 1, 1, 1, 1, 0}, {0, 0, 1, 0, 0, 0}, {1, 0, 0, 1, 0, 1}, {0, 1, 0, 0, 0, 1}, {0, 0, 0, 0, 0, 0} }) << endl;
    
}
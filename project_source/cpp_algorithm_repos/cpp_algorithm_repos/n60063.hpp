#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

static const int HORIZONTAL = 0;
static const int VERTICAL = 1;
static const int DIRECTION[4][2] = { {0, -1}, {0, 1}, {-1, 0}, {1, 0} };
static const int ROTAION[2][4][4] = {
    // 가로모드
    {
        {0, 0, 1, 1}, 
        {0, -1, 1, -1},
        {1, -1, 0, -1},
        {1, 0, 0, 1}
    },
    // 세로모드
    {
        {0, 0, 1, 1},
        {-1, 0, -1, 1},
        {-1, 1, -1, 0},
        {0, 1, 1, 0}
    }
};

class Step
{
public:
    size_t x_;
    size_t y_;
    int step_;
    int mode_;

    Step(size_t x, size_t y, int step, int mode) : x_(x), y_(y), step_(step), mode_(mode) {}
};

class Solution
{
private:
    vector<vector<int>> board_;
    vector<vector<vector<int>>> visited_;
    queue<Step> queue;
    size_t len_;

    bool check_another_block(size_t x, size_t y, int mode)
    {
        size_t nx = x + (mode == HORIZONTAL ? 1 : 0);
        size_t ny = y + (mode == VERTICAL ? 1 : 0);

        return can_move(nx, ny);
    }

    bool can_move(size_t x, size_t y)
    {
        return 0 <= x && x < len_ && 0 <= y && y < len_ && board_[y][x] == 0;
    }

    bool can_visit(size_t x, size_t y, int mode)
    {
        return visited_[y][x][mode] == 0;
    }

public:
    Solution(vector<vector<int>>& board) : board_(board), len_(board.size())
    { 
        visited_.resize(len_);

        for (size_t i = 0; i < len_; i++)
        {
            visited_[i].resize(len_);

            for (size_t j = 0; j < len_; j++)
            {
                visited_[i][j].resize(2);
            }
        }
    }

    int get_answer()
    {
        visited_[0][0][HORIZONTAL] = 1;
        queue.push(Step(0, 0, 0, HORIZONTAL));

        while (queue.empty() == false)
        {
            Step step = queue.front();

            queue.pop();

            // 지점에 도착한 경우
            if ((step.mode_ == HORIZONTAL && step.x_ == (len_ - 2) && step.y_ == (len_ - 1)) || 
                (step.mode_ == VERTICAL && step.x_ == (len_ - 1) && step.y_ == (len_ - 2)))
            {
                return step.step_;
            }
            
            // 상하좌우
            for (size_t i = 0; i < 4; i++)
            {
                size_t nx = step.x_ + DIRECTION[i][0];
                size_t ny = step.y_ + DIRECTION[i][1];

                if (can_move(nx, ny) && check_another_block(nx, ny, step.mode_) && can_visit(nx, ny, step.mode_))
                {
                    visited_[ny][nx][step.mode_] = 1;
                    queue.push(Step(nx, ny, step.step_ + 1, step.mode_));
                }
            }

            // 회전
            for (size_t i = 0; i < 4; i++)
            {
                size_t nx = step.x_ + ROTAION[step.mode_][i][0];
                size_t ny = step.y_ + ROTAION[step.mode_][i][1];
                size_t rx = step.x_ + ROTAION[step.mode_][i][2];
                size_t ry = step.y_ + ROTAION[step.mode_][i][3];
                int mode = step.mode_ ^ 1;

                if (can_move(rx, ry) && can_move(nx, ny) && check_another_block(nx, ny, mode) && can_visit(nx, ny, mode))
                {
                    visited_[ny][nx][mode] = 1;
                    queue.push(Step(nx, ny, step.step_ + 1, mode));
                }
            }
            
        }

        return -1;

    }
};

int solution(vector<vector<int>> board)
{
    return Solution(board).get_answer();
}

void do_test()
{
    cout << solution({ {0, 0, 0}, {0, 0, 0}, {0, 0, 0} }) << endl;
}
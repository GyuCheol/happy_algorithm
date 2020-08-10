#include <string>
#include <vector>
#include <stack>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    vector<stack<int>> stacks(board.size());
    stack<int> result;
    int cnt = 0;

    for (size_t i = 0; i < board.size(); ++i)
    {
        for (int j = board.size() - 1; j >= 0; --j)
        {
            if (board[j][i] > 0)
            {
                stacks[i].push(board[j][i]);
            }
        }
    }

    for (int move : moves)
    {
        int tmp = move - 1;

        if (stacks[tmp].empty())
        {
            continue;
        }

        int top = stacks[tmp].top();

        stacks[tmp].pop();

        if (result.empty() == false && result.top() == top)
        {
            cnt += 2;
            result.pop();
        }
        else
        {
            result.push(top);
        }
    }

    return cnt;
}


void do_test()
{

}
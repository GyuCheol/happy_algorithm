#include <string>
#include <vector>
#include <queue>

using namespace std;

class Step
{
public:
    int node_;
    int distance_;

    Step(int node, int distance) : node_(node), distance_(distance) {}
};

int solution(int n, vector<vector<int>> edge)
{
    vector<int> distance(n + 1);
    vector<vector<int>> graph(n + 1);
    queue<Step> queue;
    int maximum = 0;

    for (vector<int>& e : edge)
    {
        graph[e[0]].push_back(e[1]);
        graph[e[1]].push_back(e[0]);
    }

    distance[1] = 1;
    queue.push(Step(1, 1));

    while (queue.empty() == false)
    {
        Step step = queue.front();

        queue.pop();

        for (int to : graph[step.node_])
        {
            if (distance[to] == 0)
            {
                distance[to] = step.distance_ + 1;
                maximum = max(maximum, distance[to]);
                queue.push(Step(to, distance[to]));
            }
        }
    }

    int count = 0;

    for (int i = 1; i <= n; ++i)
    {
        if (distance[i] == maximum)
        {
            ++count;
        }
    }

    return count;
}

void do_test()
{
    solution(6, {{3, 6}, {4, 3}, {3, 2}, {1, 3}, {1, 2}, {2, 4}, {5, 2}});
}
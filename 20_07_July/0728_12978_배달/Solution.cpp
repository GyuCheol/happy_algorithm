#include <cassert>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Edge
{
public:
    const int to_;
    const int cost_;
    
    Edge(int to, int cost) : to_(to), cost_(cost) {}
};

class Node
{
public:
    int minimumCost_;
    vector<Edge> edges;

    Node() : minimumCost_(0x7fffffff) {}
};



int solution(int N, vector<vector<int>> road, int K)
{
    vector<Node> nodes(N + 1);
    queue<Node*> queue;

    for (vector<int> r : road)
    {
        int from = r[0];
        int to = r[1];
        int cost = r[2];

        nodes[from].edges.push_back(Edge(to, cost));
        nodes[to].edges.push_back(Edge(from, cost));
    }

    nodes[1].minimumCost_ = 0;
    queue.push(&nodes[1]);

    while (queue.empty() == false)
    {
        Node* node = queue.front();

        queue.pop();

        for (Edge e : node->edges)
        {
            int tmpCost = node->minimumCost_ + e.cost_;

            if (tmpCost < nodes[e.to_].minimumCost_)
            {
                nodes[e.to_].minimumCost_ = tmpCost;
                queue.push(&nodes[e.to_]);
            }
        }

    }

    int cnt = 0;

    for (int i = 1; i <= N; i++)
    {
        if (nodes[i].minimumCost_ <= K)
        {
            ++cnt;
        }
    }

    return cnt;
}

void do_test()
{

    assert(solution(5, { {1,2,1},{2,3,3},{5,2,2},{1,4,2},{5,3,1},{5,4,2} }, 3) == 4);

}
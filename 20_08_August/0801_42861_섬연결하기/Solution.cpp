#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;

class DisjointSet
{
private:
    vector<unordered_set<int>> sets;

public:
    DisjointSet(int n)
    {
        sets.reserve(n);

        for (int i = 0; i < n; i++)
        {
            sets.push_back(unordered_set<int> {i});
        }

    }

    int get_sets_count()
    {
        return sets.size();
    }

    unordered_set<int>* find(int n)
    {
        for (unordered_set<int>& set : sets)
        {
            if (set.find(n) != set.end())
            {
                return &set;
            }
        }

        return nullptr;
    }
    
    void union_sets(unordered_set<int>* a, unordered_set<int>* b)
    {
        a->insert(b->begin(), b->end());
        
        vector<unordered_set<int>>::iterator it = sets.begin();

        while (it != sets.end())
        {
            if (&(*it) == b)
            {
                sets.erase(it);
                break;
            }

            ++it;
        }

    }

};

struct edge
{
    int from, to, cost;

    edge(int f, int t, int c) : from(f), to(t), cost(c) {}
};

struct cmp
{
    bool operator()(edge& a, edge& b) {
        return a.cost > b.cost;
    }
};

int solution(int n, vector<vector<int>> costs)
{
    DisjointSet set(n);
    priority_queue<edge, vector<edge>, cmp> pq;
    int total = 0;

    for (vector<int>& cost : costs)
    {
        pq.push(edge(cost[0], cost[1], cost[2]));
    }

    while (set.get_sets_count() > 1)
    {
        edge e = pq.top();
        unordered_set<int>* setA = set.find(e.from);
        unordered_set<int>* setB = set.find(e.to);

        if (setA != setB)
        {
            set.union_sets(setA, setB);
            total += e.cost;
        }

        pq.pop();
    }

    return total;
}

void do_test()
{
    cout << solution(4, {{0, 1, 1}, {0, 2, 2}, {1, 2, 5}, {1, 3, 1}, {2, 3, 8}});
}
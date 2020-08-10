#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

bool solution(int n, vector<vector<int>> path, vector<vector<int>> order)
{
    vector<vector<int>> graph(n);
    vector<vector<int>> chained(n);
    vector<int> visited(n);
    vector<int> required(n);
    queue<int> q;

    // required 값 모두 -1 초기화
    fill(required.begin(), required.end(), -1);

    for (vector<int>& p : path)
    {
        graph[p[0]].push_back(p[1]);
        graph[p[1]].push_back(p[0]);
    }

    for (vector<int>& o : order) {
        required[o[1]] = o[0];
        chained[o[0]].push_back(o[1]);
    }

    if (required[0] != -1)
    {
        return false;
    }

    visited[0] = 1;
    q.push(0);

    while (!q.empty())
    {
        int node = q.front();

        q.pop();

        for (int to : graph[node])
        {

            if (visited[to] == 0)
            {
                if (required[to] != -1 && visited[required[to]] != 1)
                {
                    visited[to] = 2;
                    continue;
                }

                visited[to] = 1;
                q.push(to);

                for (int c : chained[to])
                {
                    if (visited[c] == 2)
                    {
                        visited[c] = 1;
                        q.push(c);
                    }
                }

            }

        }

    }

    int cnt = 0;

    for (int v : visited) 
    {
        if (v == 1)
        {
            ++cnt;
        }
    }

    return cnt == n;
}

void do_test()
{

}
#include <vector>

using namespace std;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int n, int m, vector<vector<int>> edge_list, int k, vector<int> gps_log)
{
    int size = n + 1;
    vector<vector<int>> graph(size);

    for (vector<int>& edge : edge_list)
    {
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    int start = gps_log[0];
    int end = gps_log[gps_log.size() - 1];

    int answer = 0;
    

    return answer;
}

void do_test()
{

}
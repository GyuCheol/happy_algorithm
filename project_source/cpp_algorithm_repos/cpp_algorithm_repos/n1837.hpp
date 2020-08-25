#include <vector>
#include <cstring>

using namespace std;

const int INF = 0x3F3F3F3F;

int solution(int n, int m, vector<vector<int>> edge_list, int k, vector<int> gps_log) {
	int answer = 0, u, v, i, j;
	vector<vector<int>> adj(n);
	int dp[100][200], adjA[200][200] = {};

	for (vector<int>& e : edge_list) {
		u = e[0], v = e[1];
		u--, v--;
		adj[u].push_back(v);
		adj[v].push_back(u);
		adjA[u][v] = adjA[v][u] = 1;
	}
	for (i = 0; i < n; i++) {
		adj[i].push_back(i);
		adjA[i][i] = 1;
	}
	memset(dp, 0x3F, sizeof dp);
	for (i = 0; i < k; i++) gps_log[i]--;
	dp[0][gps_log[0]] = 0;
	for (i = 1; i < k; i++) {
		for (j = 0; j < n; j++)
			if (dp[i - 1][j] != INF) {
				for (int& v : adj[j])
					dp[i][v] = min(dp[i][v], dp[i - 1][j] + (v != gps_log[i]));
			}
	}
	answer = dp[k - 1][gps_log[k - 1]];
	return answer == INF ? -1 : answer;
}
void do_test()
{
	solution(7, 10, { {1, 2}, {1, 3}, {2, 3}, {2, 4}, {3, 4}, {3, 5}, {4, 6}, {5, 6}, {5, 7}, {6, 7} }, 6, { 1, 2, 3, 3, 6, 7 });
}
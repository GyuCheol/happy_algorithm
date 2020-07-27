#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2)
{
	vector<string> answer;
	stringstream ss;
	
	answer.reserve(n);

	for (int i = 0; i < n; i++)
	{
		int tmp = arr1[i] | arr2[i];

		for (int j = n - 1; j >= 0; j--)
		{
			ss << ((tmp & (1 << j)) != 0 ? '#' : ' ');
		}

		answer.push_back(ss.str());
		ss.str("");
	}

    return answer;
}

void do_test()
{
	vector<string> answer = solution(5, { 9, 20, 28, 18, 11 }, { 30, 1, 21, 17, 28 });

	vector<string>::iterator it = answer.begin();

	while (it != answer.end()) {
		cout << *it << endl;
		++it;
	}
}
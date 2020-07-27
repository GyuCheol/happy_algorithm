#include <iostream>
#include <string>
#include <vector>
#include <sstream>

/*
문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/17681?language=cpp

각 arr1, arr2의 값을 비트 연산 or(|)을 하면 각 라인의 결과를 얻을 수 있다.
그 후, n길이 만큼 ' '과 '#'을 만들어하니 2로 나누어 2진수 변환된 값에 따라 문자열을 만들면 된다.

string이 immutable한 다른 언어와는 다르게 cpp는 string 내부 값을 변경할 수가 있다.
그렇지만 stringstream을 이용하여 풀이.

*/

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
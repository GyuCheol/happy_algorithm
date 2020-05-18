// Compiler (C++, java, C#) IDE
// JAVA IDE Visual Studio 3배는 무거움
// IDE 중에서는 IDE 자체가 너무 무겁..
// Eclipse, Intelli J, Android Studio

// IDE 벗어나서, Editor (Interpreter)
// Visual Code, PyCharm, Notepad++, ATOM

#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

struct TruckData
{
    int weight;
    int step;
};

int solution(int bridge_length, int weight, vector<int> truck_weights)
{
    // vector = python[]
    queue<int> truck_queue;
    vector<TruckData> trucks_on_bridge;

    for (int weight : truck_weights)
    {
        truck_queue.push(weight);
    }

    int answer = 0;

    while (truck_queue.size() > 0 || trucks_on_bridge.size() > 0)
    {
        answer++;

        // 지원씨의 고비 1단계
        auto it = trucks_on_bridge.begin();

        while (it != trucks_on_bridge.end())
        {
            it->step++;

            if (it->step > bridge_length)
            {
                it = trucks_on_bridge.erase(it);
            }
            else
            {
                it++;
            }
        }
        // 여기까지!

        if (truck_queue.size() > 0)
        {
            int t = truck_queue.front();
            int sum = 0;

            for (auto truck : trucks_on_bridge)
            {
                sum += truck.weight;
            }
            
            if (weight >= (sum + t))
            {
                truck_queue.pop();
                trucks_on_bridge.push_back({t, 1});
            }

        }

    }

    return answer;
}

int main()
{
    cout << solution(2, 10, {7, 4, 5, 6});

    return 0;
}



#include <vector>
#include <cassert>
#include <queue>

using namespace std;

class Truck
{
private:
    int weight_;
    int start_time_;

public:
    Truck(int weight, int time);
    int GetWeight();
    int GetStartTime();

};

Truck::Truck(int weight, int time)
    : weight_(weight), start_time_(time) { }

inline int Truck::GetWeight()
{
    return weight_;
}

inline int Truck::GetStartTime()
{
    return start_time_;
}


int solution(int bridge_length, int weight, vector<int> truck_weights)
{
    int seconds = 0;
    int totalWeights = 0;
    queue<int> truckQueue;
    queue<Truck*> movingQueue;

    for (int w : truck_weights)
    {
        truckQueue.push(w);
    }

    while (truckQueue.empty() == false || movingQueue.empty() == false)
    {
        
        if (movingQueue.empty() == false && (seconds - movingQueue.front()->GetStartTime()) == bridge_length)
        {
            totalWeights -= movingQueue.front()->GetWeight();
            delete movingQueue.front();
            movingQueue.pop();
        }

        if (truckQueue.empty() == false && (totalWeights + truckQueue.front()) <= weight)
        {
            int w = truckQueue.front();
            totalWeights += w;
            movingQueue.push(new Truck(w, seconds));
            truckQueue.pop();
        }

        seconds += 1;
    }
    

    return seconds;
}

void do_test()
{

    assert(solution(2, 10, { 7, 4, 5, 6 }) == 8);
}
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Node
{
public:
    int x_;
    int y_;
    int value_;
    Node* left_;
    Node* right_;

    Node(int x, int y, int value) : x_(x), y_(y), value_(value), left_(nullptr), right_(nullptr) { }

    void travel_preorder(vector<int>& routine)
    {
        routine.push_back(value_);

        if (left_ != nullptr)
        {
            left_->travel_preorder(routine);
        }

        if (right_ != nullptr)
        {
            right_->travel_preorder(routine);
        }
    }

    void travel_postorder(vector<int>& routine)
    {
        
        if (left_ != nullptr)
        {
            left_->travel_postorder(routine);
        }

        if (right_ != nullptr)
        {
            right_->travel_postorder(routine);
        }

        routine.push_back(value_);
    }

};

class Tree
{
private:
    vector<Node> nodes;
    Node* root;

public:
    Tree(int size) : root(nullptr)
    {
        // vector 내의 포인터 위치가 바뀌는 것을 막기 위해 메모리를 미리 확보한다.
        nodes.reserve(size); 
    };

    void add_node(Node node)
    {
        nodes.push_back(node);
        Node* ptr = &nodes[nodes.size() - 1];

        if (root == nullptr)
        {
            root = ptr;
            return;
        }

        Node* tmp = root;

        while (true)
        {
            if (node.x_ < tmp->x_)
            {
                if (tmp->left_ == nullptr)
                {
                    tmp->left_ = ptr;
                    return;
                }
                else
                {
                    tmp = tmp->left_;
                }
            }
            else
            {
                if (tmp->right_ == nullptr)
                {
                    tmp->right_ = ptr;
                    return;
                }
                else
                {
                    tmp = tmp->right_;
                }
            }
        }

    }

    vector<int> get_preorder()
    {
        vector<int> routine;

        routine.reserve(nodes.size());

        if (root != nullptr)
        {
            root->travel_preorder(routine);
        }

        return routine;
    }

    vector<int> get_postorder()
    {
        vector<int> routine;

        routine.reserve(nodes.size());

        if (root != nullptr)
        {
            root->travel_postorder(routine);
        }

        return routine;
    }

};

bool compareNodes(const Node& a, const Node& b)
{
    return (a.y_ == b.y_) ? a.x_ < b.x_ : a.y_ > b.y_;
}

vector<vector<int>> solution(vector<vector<int>> nodeinfo) 
{
    vector<Node> nodes;
    Tree tree(nodeinfo.size());

    nodes.reserve(nodeinfo.size());

    for (size_t i = 0; i < nodeinfo.size(); i++)
    {
        nodes.push_back(Node(nodeinfo[i][0], nodeinfo[i][1], i + 1));
    }

    sort(nodes.begin(), nodes.end(), compareNodes);

    for (Node& nodes : nodes)
    {
        tree.add_node(nodes);
    }

    return { tree.get_preorder(), tree.get_postorder() };
}

void do_test()
{
    
    solution({{5, 3}, {11, 5}, {13, 3}, {3, 5}, {6, 1}, {1, 3}, {8, 6}, {7, 2}, {2, 2}});

}
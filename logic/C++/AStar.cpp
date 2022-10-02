/**
 * To compile in Windows use g++ -o AStar AStar.cpp -lpsapi
 * To compile in Linux use g++ -o AStar AStar.cpp
 */
#include <iostream>
#include <queue>
#include <vector>
#include <set>
#include <math.h>
#include "Utils.h"

using namespace std;

class Compare{
    pair<int, int> _target;
public:
    Compare(pair<int, int> target){
        _target = target;
    }
    bool operator() (const Node a, const Node b){
        float aDistance = sqrt( pow(_target.second - a.position.second, 2) + pow(a.position.first - _target.first, 2));
        float bDistance = sqrt( pow(_target.second - b.position.second, 2) + pow(b.position.first - _target.first, 2));

        return aDistance > bDistance;
    }
};

typedef priority_queue<Node, vector<Node>, Compare> Heap;

Node AStar(vector<vector<char>>& map, vector<pair<int, int>>& traverse, Node start, Node end, bool& failure){
    if (IsFinish(map, start.position, end.position)){
        failure = false;
        return start;
    }

    Heap frontier(Compare(end.position));
    frontier.push(start);
    set<pair<int, int>> reached;
    reached.insert(start.position);
    while (!frontier.empty()){
        Node current = frontier.top();
        frontier.pop();
        traverse.push_back(current.position);
        if(IsFinish(map, current.position, end.position)){
            failure = false;
            return current;
        }
        vector<Node> childs = Expand(map, current);
        for(int i = 0; i < childs.size(); i++){
            pair<int, int> position = childs[i].position;
            if (!reached.count(position)){
                reached.insert(position);
                frontier.push(childs[i]);
            }
        }
    }

    failure = true;
    return start;
}

Node AStarWithTree(vector<vector<char>>& maze, vector<pair<int, int>>& traverse, Node start, Node end, bool& failure, vector<pair<int, int>>& tree){
    if (IsFinish(maze, start.position, end.position)){
        failure = false;
        tree.push_back(start.position);
        return start;
    }
    map<int, pair<int, int>> IDs;
    map<int, int> index;
    vector<int> idsTree(2000, -1);
    index.insert({0,0});
    IDs.insert({0, start.position});
    Heap frontier(Compare(end.position));
    frontier.push(start);
    set<pair<int, int>> reached;
    reached.insert(start.position);
    start.id = 0;
    idsTree[0] = 0;
    int currIndex = 1;
    while (!frontier.empty()){
        Node current = frontier.top();
        int fatherIndex = index[current.id];
        frontier.pop();
        traverse.push_back(current.position);
        if(IsFinish(maze, current.position, end.position)){
            failure = false;
            GetTree(idsTree, IDs, tree);
            return current;
        }
        vector<Node> childs = Expand(maze, current);
        for(int i = 0; i < childs.size(); i++){
            pair<int, int> position = childs[i].position;
            if (!reached.count(position)){
                childs[i].id = currIndex;
                currIndex++;
                idsTree[4*fatherIndex + i + 1] = childs[i].id;
                index.insert({childs[i].id, 4*fatherIndex + i + 1});
                IDs.insert({childs[i].id, position});
                reached.insert(position);
                frontier.push(childs[i]);
            }
        }
    }

    failure = true;
    return start;
}

int main(int argc, char **argv) {
    Solver AStar_Solver(argv[1], "AStar", &AStar, &AStarWithTree);
    return 0;
}

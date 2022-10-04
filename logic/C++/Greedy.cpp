/**
 * To compile in Windows use g++ -o Greedy Greedy.cpp -lpsapi
 * To compile in Linux use g++ -o Greedy Greedy.cpp
 */
#include <iostream>
#include <stack>
#include <vector>
#include <set>
#include "Utils.h"

using namespace std;

Node Greedy(vector<vector<char>>& map, vector<pair<int, int>>& traverse, Node start, Node end, bool& failure){
    if (IsFinish(map, start.position, end.position)){
        failure = false;
        return start;
    }

    stack<Node> frontier;
    frontier.push(start);
    set<pair<int, int>> reached;
    reached.insert(start.position);
    while (!frontier.empty()){
        Node current = frontier.top();
        frontier.pop();
        traverse.push_back(current.position);
        if (IsFinish(map, current.position, end.position)){
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

Node GreedyWithTree(vector<vector<char>>& maze, vector<pair<int, int>>& traverse, Node start, Node end, bool& failure, vector<pair<int, int>>& tree){
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
    start.id = 0;
    idsTree[0] = 0;
    int currIndex = 1;
    stack<Node> frontier;
    frontier.push(start);
    set<pair<int, int>> reached;
    reached.insert(start.position);
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
    Solver Greedy_Solver(argv[1], "Greedy", &Greedy, &GreedyWithTree);
    return 0;
}

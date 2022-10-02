/**
 * To compile in Windows use g++ -o DLS DLS.cpp -lpsapi
 * To compile in Linux use g++ -o DLS DLS.cpp
 */
#include <iostream>
#include <stack>
#include <vector>
#include <set>
#include <math.h>
#include "Utils.h"

using namespace std;

class DLSNode{
public:
    pair<int, int> position;
    vector<char> path;
    int depth;
    int id;
    DLSNode (int x, int y){
        position = make_pair(x, y);
    }
};

vector<DLSNode> Expand(vector<vector<char>>& map, DLSNode current){
    vector<DLSNode> neighbors;
    pair<int, int> currPosition = current.position;
    DLSNode newNode(0, 0);
    if ((currPosition.second + 1 < map[currPosition.first].size()) && (map[currPosition.first][currPosition.second + 1] != 'w')){
        newNode.position = make_pair(currPosition.first, currPosition.second + 1);
        newNode.path = current.path;
        newNode.path.push_back('R'); // Right
        newNode.depth = current.depth + 1;
        neighbors.push_back(newNode);
    }
    if ((currPosition.second - 1 >= 0) && (map[currPosition.first][currPosition.second - 1] != 'w')){
        newNode.position = make_pair(currPosition.first, currPosition.second - 1);
        newNode.path = current.path;
        newNode.path.push_back('L'); // Left
        newNode.depth = current.depth + 1;
        neighbors.push_back(newNode);
    }
    if ((currPosition.first + 1 < map.size()) && (map[currPosition.first + 1][currPosition.second] != 'w')){
        newNode.position = make_pair(currPosition.first + 1, currPosition.second);
        newNode.path = current.path;
        newNode.path.push_back('D'); // Down
        newNode.depth = current.depth + 1;
        neighbors.push_back(newNode);
    }
    if ((currPosition.first - 1 >= 0) && (map[currPosition.first - 1][currPosition.second] != 'w')){
        newNode.position = make_pair(currPosition.first - 1, currPosition.second);
        newNode.path = current.path;
        newNode.path.push_back('U'); // Up
        newNode.depth = current.depth + 1;
        neighbors.push_back(newNode);
    }

    return neighbors;
}

DLSNode DLS(vector<vector<char>>& map, vector<pair<int, int>>& traverse, DLSNode start, DLSNode end, int maxDepth, bool& failure){
    if (IsFinish(map, start.position, end.position)){
        failure = false;
        return start;
    }

    stack<DLSNode> frontier;
    frontier.push(start);
    set<pair<int, int>> reached;
    reached.insert(start.position);
    while (!frontier.empty()){
        DLSNode current = frontier.top();
        frontier.pop();
        traverse.push_back(current.position);
        if (IsFinish(map, current.position, end.position)){
            failure = false;
            return current;
        }
        vector<DLSNode> childs = Expand(map, current);
        for(int i = 0; i < childs.size(); i++){
            pair<int, int> position = childs[i].position;
            if (childs[i].depth > maxDepth){
                failure = true;
                return start;
            }else if (!reached.count(position)){
                reached.insert(position);
                frontier.push(childs[i]);
            }
        }
    }

    failure = true;
    return start;
}

DLSNode DLSWithTree(vector<vector<char>>& maze, vector<pair<int, int>>& traverse, DLSNode start, DLSNode end, int maxDepth, bool& failure, vector<pair<int, int>>& tree){
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
    stack<DLSNode> frontier;
    frontier.push(start);
    set<pair<int, int>> reached;
    reached.insert(start.position);
    while (!frontier.empty()){
        DLSNode current = frontier.top();
        int fatherIndex = index[current.id];
        frontier.pop();
        traverse.push_back(current.position);
        if(IsFinish(maze, current.position, end.position)){
            failure = false;
            GetTree(idsTree, IDs, tree);
            return current;
        }
        vector<DLSNode> childs = Expand(maze, current);
        for(int i = 0; i < childs.size(); i++){
            pair<int, int> position = childs[i].position;
            if (childs[i].depth > maxDepth){
                failure = true;
                return start;
            }else if (!reached.count(position)){
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

DLSNode IDS(vector<vector<char>>& map, vector<pair<int, int>>& traverse, DLSNode start, DLSNode end, int maxDepth, bool& failure){
    int depth;
    for(depth = 0; depth <= maxDepth; depth++){
        DLSNode result = DLS(map, traverse, start, end, depth, failure);
        if (!failure){
            return result;
        }
    }

    return end;
}

DLSNode IDSWithTree(vector<vector<char>>& map, vector<pair<int, int>>& traverse, DLSNode start, DLSNode end, int maxDepth, bool& failure, vector<pair<int, int>>& tree){
    int depth;
    vector<pair<int, int>> currTree;
    for(depth = 0; depth <= maxDepth; depth++){
        DLSNode result = DLSWithTree(map, traverse, start, end, depth, failure, currTree);
        if (!failure){
            tree = currTree;
            return result;
        }
        currTree.clear();
    }

    return end;
}

int main(int argc, char **argv) {
    vector<vector<char>> map = GetMap(argv[1]);
    int maxDepth = stoi(argv[2]);
    DLSNode start(0, FindCellIndex(map[0]));
    DLSNode end(map.size() - 1, FindCellIndex(map[map.size() - 1]));
    start.depth = 0;
    bool failure;
    vector<pair<int,int>> traverse;
    vector<pair<int, int>> tree;
    auto startTime = std::chrono::system_clock::now();
    DLSNode fin(0,0);
    if (map.size() > 5){
        fin = IDS(map, traverse, start, end, maxDepth, failure);
    }else{
        fin = IDSWithTree(map, traverse, start, end, maxDepth, failure, tree);
    }
    auto endTime = std::chrono::system_clock::now();
    int totalTime = std::chrono::duration_cast<std::chrono::nanoseconds>(endTime - startTime).count();
    if(!failure){
        WriteSolutionPath(fin.path, "DLS_path");
        WriteTraverse(traverse, "DLS_traverse");
        WriteMemoryAndTime(totalTime, "DLS_stats");
        if (map.size() <= 5){
            WriteTree(tree, "DLS_tree");
        }
    }else{
        cout << "FAILED" << '\n';
    }
    return 0;
}

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

int main(int argc, char **argv) {
    vector<vector<char>> map = GetMap(argv[1]);
    int maxDepth = stoi(argv[2]);
    DLSNode start(0, FindCellIndex(map[0]));
    DLSNode end(map.size() - 1, FindCellIndex(map[map.size() - 1]));
    start.depth = 0;
    bool failure;
    vector<pair<int,int>> traverse;
    DLSNode fin = IDS(map, traverse, start, end, maxDepth, failure);
    if(!failure){
        WriteSolutionPath(fin.path, "DLS_path");
        WriteTraverse(traverse, "DLS_traverse");
    }else{
        cout << "FAILED" << '\n';
    }
    return 0;
}

#include <vector>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#ifndef _UTILS_H
#define _UTILS_H

class Node{
public:
    vector<char> path;
    pair<int, int> position;
    Node(int x = 0, int y = 0) {
        position = make_pair(x, y);
    }
};

bool IsFinish(vector<vector<char>> map, pair<int, int> currPosition, pair<int, int> target){
    return currPosition == target;
}

vector<Node> Expand(vector<vector<char>>& map, Node current){
    vector<Node> neighbors;
    pair<int, int> currPosition = current.position;
    Node newNode(0,0);
    if ((currPosition.second + 1 < map[currPosition.first].size()) && (map[currPosition.first][currPosition.second + 1] != 'w')){
        newNode.position = make_pair(currPosition.first, currPosition.second + 1);
        newNode.path = current.path;
        newNode.path.push_back('R'); // Right
        neighbors.push_back(newNode);
    }
    if ((currPosition.second - 1 >= 0) && (map[currPosition.first][currPosition.second - 1] != 'w')){
        newNode.position = make_pair(currPosition.first, currPosition.second - 1);
        newNode.path = current.path;
        newNode.path.push_back('L'); // Left
        neighbors.push_back(newNode);
    }
    if ((currPosition.first + 1 < map.size()) && (map[currPosition.first + 1][currPosition.second] != 'w')){
        newNode.position = make_pair(currPosition.first + 1, currPosition.second);
        newNode.path = current.path;
        newNode.path.push_back('D'); // Down
        neighbors.push_back(newNode);
    }
    if ((currPosition.first - 1 >= 0) && (map[currPosition.first - 1][currPosition.second] != 'w')){
        newNode.position = make_pair(currPosition.first - 1, currPosition.second);
        newNode.path = current.path;
        newNode.path.push_back('U'); // Up
        neighbors.push_back(newNode);
    }

    return neighbors;
}

vector<vector<char>> GetMap(string mazeName){
    ifstream myFile(mazeName);
    string line;
    vector<vector<char>> map;
    vector<char> row;
    if (myFile.is_open()){
        while(getline(myFile, line)){
            for(int j = 0; j < line.length(); j+=2) {
                row.push_back(line[j]);
            }
            map.push_back(row);
            row.clear();
        }
        myFile.close();
    } else{
        cout << "F" << '\n';
    }

    return map;
}

void WriteSolutionPath(vector<char> path, string name){
    ofstream solutionPath;
    solutionPath.open("output/" + name + ".txt");
    for(int i = 0; i < path.size() - 1; i++){
        solutionPath << path[i] << ' ';
    }
    solutionPath << path[path.size() - 1] << '\n';
    solutionPath.close();
}

void WriteTraverse(vector<pair<int, int>> traverse, string name){
    ofstream traversePath;
    traversePath.open("output/" + name + ".txt");
    for(int i = 0; i < traverse.size() - 1; i++){
        traversePath << "(" << traverse[i].first << ',' << traverse[i].second << ") ";
    }
    traversePath << "(" << traverse[traverse.size() - 1].first << ',' << traverse[traverse.size() - 1].second << ")\n";
    traversePath.close();
}

void PrintMap(vector<vector<char>> map){
    for(int i = 0; i < map.size(); i++) {
        cout << " ";
        for(int j = 0; j < map[i].size(); j++){
            cout << map[i][j] << " ";
        }
        cout << '\n';
    }
}
#endif
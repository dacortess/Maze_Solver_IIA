#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <chrono>

using namespace std;

#ifndef _UTILS_H
#define _UTILS_H

#if defined(_WIN32)
    #include "windows.h"
    #include "psapi.h"

    double GetVirtualMemory(){
        PROCESS_MEMORY_COUNTERS_EX pmc;
        GetProcessMemoryInfo(GetCurrentProcess(), (PROCESS_MEMORY_COUNTERS*)&pmc, sizeof(pmc));
        SIZE_T virtualMemUsedByMe = pmc.PrivateUsage;
        return virtualMemUsedByMe;
    }

    double GetPhysicalMemory(){
        SIZE_T physMemUsedByMe = pmc.WorkingSetSize;
        return physMemUsedByMe;
    }
#else
    #include "sys/types.h"
    #include "sys/sysinfo.h"
    #include "stdlib.h"
    #include "stdio.h"
    #include "string.h"
    #include "sys/times.h"

    static clock_t lastCPU, lastSysCPU, lastUserCPU;
    static int numProcessors;

    int parseLine(char* line){
        // This assumes that a digit will be found and the line ends in " Kb".
        int i = strlen(line);
        const char* p = line;
        while (*p <'0' || *p > '9') p++;
        line[i-3] = '\0';
        i = atoi(p);
        return i;
    }

    double GetPhysicalMemory(){ //Note: this value is in KB!
        FILE* file = fopen("/proc/self/status", "r");
        int result = -1;
        char line[128];

        while (fgets(line, 128, file) != NULL){
            if (strncmp(line, "VmRSS:", 6) == 0){
                result = parseLine(line);
                break;
            }
        }
        fclose(file);
        return result;
    }

    double GetVirtualMemory(){ //Note: this value is in KB!
        FILE* file = fopen("/proc/self/status", "r");
        int result = -1;
        char line[128];

        while (fgets(line, 128, file) != NULL){
            if (strncmp(line, "VmSize:", 7) == 0){
                result = parseLine(line);
                break;
            }
        }
        fclose(file);
        return result;
    }

    vector<double> GetMemoryUsage(){
        vector<double> memory(2);
        memory[0] = GetVirtualMemory();
        memory[1] = GetPhysicalMemory();
        return memory;
    }
#endif

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

int FindCellIndex(vector<char> row){
    for(int i = 0; i < row.size(); i++){
        if (row[i] == 'c'){
            return i;
        }
    }

    cout << "NOT FOUND OPEN CELL \n";
    return 0;
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

void WriteMemoryAndTime(int time, string name){
    vector<double> memory = GetMemoryUsage();
    ofstream stats;
    stats.open("output/" + name + ".txt");
    stats << memory[0] << ' '; //Virutal Memory used in Kb
    stats << memory[1] << ' '; //Physical Memory used inKb
    stats << time << '\n'; // Total time in ms
    stats.close();
}
#endif
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
#include <cmath>

using namespace std;

#ifndef _UTILS_H
#define _UTILS_H

// Functions to determine the amount of virtual and phsysical memory used by the current process
#if defined(_WIN32) // If working on Windows
    #include "windows.h"
    #include "psapi.h"

    double GetVirtualMemory(){
        PROCESS_MEMORY_COUNTERS_EX pmc;
        GetProcessMemoryInfo(GetCurrentProcess(), (PROCESS_MEMORY_COUNTERS*)&pmc, sizeof(pmc));
        SIZE_T virtualMemUsedByMe = pmc.PrivateUsage;
        return virtualMemUsedByMe;
    }

    double GetPhysicalMemory(){
        PROCESS_MEMORY_COUNTERS_EX pmc;
        GetProcessMemoryInfo(GetCurrentProcess(), (PROCESS_MEMORY_COUNTERS*)&pmc, sizeof(pmc));
        SIZE_T physMemUsedByMe = pmc.WorkingSetSize;
        return physMemUsedByMe;
    }

    vector<double> GetMemoryUsage(){
        vector<double> memory(2);
        memory[0] = GetVirtualMemory();
        memory[1] = GetPhysicalMemory();
        return memory;
    }
#else // Else we assume the user is working with Linux/Unix
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

/**
 * @brief Data structure to represent the state of the agent
 * 
 */
class Node{
public:
    /**
     * @brief Path followed to reach the current state. It's given as a sequence of instructions
     * in char format, namely: 'D'(Down), 'U'(Up), 'L'(Left) and 'D'(Down)
     * 
     */
    vector<char> path;

    /**
     * @brief Current position of the agent in the maze. It's given in x-y coordinates, where the
     * northwest position of the maze represents the (0,0) coordinate
     * 
     */
    pair<int, int> position;

    /**
     * @brief Construct a new Node object
     * 
     * @param x The x coordinate of the agent
     * @param y The y coordinate of the agent
     */
    Node(int x = 0, int y = 0) {
        position = make_pair(x, y);
    }
};

/**
 * @brief Checks if the agent has reached the target
 * 
 * @param map The maze to solve
 * @param currPosition Current position of the agent in the maze
 * @param target Position of the target in the maze
 * @return true If the agent has reached the target, 
 * @return false otherwise
 */
bool IsFinish(vector<vector<char>> map, pair<int, int> currPosition, pair<int, int> target){
    return currPosition == target;
}

/**
 * @brief Expands the current node to find its successors
 * 
 * @param map Maze to solve
 * @param current Current node representing the state of the agent
 * @return vector<Node> with the current node successors
 */
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

/**
 * @brief Read a the map from a given .csv file and return it as a vector<vector<char>> type
 * 
 * @param mazeName The path of the file containing the maze
 * @return vector<vector<char>> The maze in a 2-dimensional char vector where there's a 'c' for
 * a cell and a 'w' for a wall
 */
vector<vector<char>> GetMap(string mazePath){
    ifstream myFile(mazePath);
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

/**
 * @brief Finds a cell in a row of the maze
 * 
 * @param row A row of the maze
 * @return int - The position where there's a cell 'c'. If not cell is found
 * it returns 0 and an error message
 */
int FindCellIndex(vector<char> row){
    for(int i = 0; i < row.size(); i++){
        if (row[i] == 'c'){
            return i;
        }
    }

    cout << "NOT FOUND OPEN CELL \n";
    return 0;
}

/**
 * @brief Writes the path found in the maze in a .txt file with the given name
 * 
 * @param path Sequence of char instructions(D,U,L,R) representing the path to solve
 * the maze 
 * @param name Name of the file to save the path found
 */
void WriteSolutionPath(vector<char> path, string name){
    ofstream solutionPath;
    solutionPath.open("output/" + name + ".txt");
    for(int i = 0; i < path.size() - 1; i++){
        solutionPath << path[i] << ' ';
    }
    solutionPath << path[path.size() - 1] << '\n';
    solutionPath.close();
}

/**
 * @brief Writes the traverse made by the agent to found the path in the maze
 * 
 * @param traverse Sequence of x-y coordinates traversed to find the path in the maze 
 * @param name Name of the file to save the path found
 */
void WriteTraverse(vector<pair<int, int>> traverse, string name){
    ofstream traversePath;
    traversePath.open("output/" + name + ".txt");
    for(int i = 0; i < traverse.size() - 1; i++){
        traversePath << "(" << traverse[i].first << ',' << traverse[i].second << ") ";
    }
    traversePath << "(" << traverse[traverse.size() - 1].first << ',' << traverse[traverse.size() - 1].second << ")\n";
    traversePath.close();
}

/**
 * @brief Helper function to print the maze represented as a 2-dimensional char vector
 * 
 * @param map 2-dimensional char vector representing the maze
 */
void PrintMap(vector<vector<char>> map){
    for(int i = 0; i < map.size(); i++) {
        cout << " ";
        for(int j = 0; j < map[i].size(); j++){
            cout << map[i][j] << " ";
        }
        cout << '\n';
    }
}

/**
 * @brief Writes the VRAM, RAM and execution time used to solve the maze in a .txt file with the given name
 * 
 * @param time Time taken to solve the maze in ms
 * @param name Name of the file to save the memory and time statistics
 */
void WriteMemoryAndTime(double time, string name){
    vector<double> memory = GetMemoryUsage();
    ofstream stats;
    stats.open("output/" + name + ".txt");
    stats << std::llround(memory[0]) << ' '; //Virtual Memory used in Kb
    stats << std::llround(memory[1]) << ' '; //Physical Memory used inKb
    stats << time << '\n'; // Total time in ms
    stats.close();
}
#endif
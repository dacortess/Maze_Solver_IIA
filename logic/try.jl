using DataStructures
using LinearAlgebra

struct Node
    state
    parent
    value
    action
end

open("files/maze_50x50.csv", "r") do maze
    num_of_line = 0
    while !eof(maze)
        current_line = readline(maze)
        num_of_line += 1
        println(current_line)
    end
end

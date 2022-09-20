using DataStructures
using LinearAlgebra

mutable struct Node
    state
    parent
    value
    action
end

maze_array = []
open("files/maze_5x5.csv", "r") do maze
    while !eof(maze)
        push!(maze_array, split(readline(maze), ","))
    end
end


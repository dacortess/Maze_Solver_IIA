using DataStructures
using LinearAlgebra
using StructEquality

@def_structequal mutable struct Node
    state
    parent
    value
    action
end

maze_array = []
open("/home/stiven/Documentos/Universidad/Inteligencia artificial/Tareas/maze_solver_iia/logic/files/maze_50x50.csv", "r") do maze
    while !eof(maze)
        push!(maze_array, split(readline(maze), ","))
    end
end


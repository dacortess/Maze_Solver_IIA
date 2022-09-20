using DataStructures
include("bestfirstsearch.jl")

result = BestFirstSearch(maze_array, "DepthFirstSearch", length(maze_array)*length(maze_array))
println(result)

using DataStructures
include("bestfirstsearch.jl")

result = BestFirstSearch(maze_array, "BreadthFirstSearch", 1)
if result == nothing
    println("Not solution found")
else
    println(result)
end

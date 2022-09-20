using DataStructures
include("bestfirstsearch.jl")

for i in 1:length(maze_array)
    result = BestFirstSearch(maze_array, "DepthFirstSearch", i)
    if result != "cutoff"
        println(result)
    end
end


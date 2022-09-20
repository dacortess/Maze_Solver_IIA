using DataStructures 
include("reader.jl") 

function add(algorithm, structure, element)
    if algorithm == "BreadthFirstSearch"
        enqueue!(structure, element)
    elseif algorithm == "DepthFirstSearch"
        push!(structure, element)
    end
end
function remove(algorithm, structure)
    element = nothing
    if algorithm == "BreadthFirstSearch"
        element = dequeue!(structure)
    elseif algorithm == "DepthFirstSearch"
        element = pop!(structure)
    end
    return element 
end

function expand(maze, node)
    position = node.state
    neighbors = []
    row = position[1]
    column = position[2]
    if maze[row+1][column] == "c" && (node.parent === nothing || node.parent.state!=(row+1,column))
        new_node = Node((row+1, column), node, maze[row+1][column], node.action+=1)
        push!(neighbors, new_node)
    end
    if position!=(1,2) && maze[row-1][column] == "c" && node.parent.state!=(row-1,column) 
        new_node = Node((row-1, column), node, maze[row-1][column], node.action+=1)
        push!(neighbors, new_node)
    end
    if maze[row][column+1] == "c" && node.parent.state!=(row,column+1)
        new_node = Node((row, column+1), node, maze[row][column+1], node.action+=1)
        push!(neighbors, new_node)
    end
    if maze[row][column-1] == "c" && node.parent.state!=(row,column-1)
        new_node = Node((row, column-1), node, maze[row+1][column-1], node.action+=1)
        push!(neighbors, new_node)
    end
    return neighbors
end

function BestFirstSearch(maze, algorithm, depth)
    row = 1
    column = 2
    start = Node((row,column), nothing, maze[row][column], 1)
    if algorithm == "BreadthFirstSearch"
        frontier = Queue{Node}()
    elseif algorithm == "DepthFirstSearch"
        frontier = Stack{Node}()
    else
        frontier = PriotityQueue()
    end
    reached = []
    push!(reached, start.state)
    add(algorithm, frontier, start)
    result = nothing
    while !isempty(frontier)
        current_node = remove(algorithm, frontier)
        if current_node.state == (length(maze), length(maze)-1)
            result = current_node
            return result
        end
        if algorithm == "DepthFirstSearch" && depth>current_node.action
            result == "cutoff"
            return result
        end
        expand_view = expand(maze, current_node)
        for child in expand_view
            if algorithm == "BreadthFirstSearch"
                possible_position = child.state
                if !(possible_position in reached)
                    push!(reached, child.state)
                    add(algorithm, frontier, child)
                end
            end
            if algorithm == "DepthFirstSearch"
                add(algorithm, frontier, child)
            end
        end
    end
    return result
end

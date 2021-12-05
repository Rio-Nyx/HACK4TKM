from collections import defaultdict
rem=60

# Class to represent a graph
class Graph:

    def __init__(self,locations):
        self.locations = locations

    # A utility function to find the
    # vertex with minimum dist value, from
    # the set of vertices still in queue
    def minDistance(self, dist, queue):
        # Initialize min value and min_index as -1
        minimum = float("Inf")
        min_index = -1

        # from the dist array,pick one which
        # has min value and is till in queue
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index

    # Function to print shortest path
    # from source to j
    # using parent array
    def printPath(self, parent, j):

        # Base Case : If j is source
        if parent[j] == -1:
            print(self.locations[str(j)],end=' -> ')
            return
        self.printPath(parent, parent[j])
        print(self.locations[str(j)],end=' -> ')


    # A utility function to print
    # the constructed distance
    # array
    def printSolution(self, dist, parent):
        src = 0
        print("Vertex \t\tDistance from Source\tPath")
        for i in range(1, len(dist)):
            if (dist[i] < rem):
                print("\n%s --> %s \t\t%d \t\t\t\t\t" % (self.locations[str(src)], self.locations[str(i)], dist[i]),end=' '),
                self.printPath(parent, i)

    '''Function that implements Dijkstra's single source shortest path
    algorithm for a graph represented using adjacency matrix
    representation'''

    def dijkstra(self, graph, src):

        row = len(graph)
        col = len(graph[0])

        # The output array. dist[i] will hold
        # the shortest distance from src to i
        # Initialize all distances as INFINITE
        dist = [float("Inf")] * row

        # Parent array to store
        # shortest path tree
        parent = [-1] * row

        # Distance of source vertex
        # from itself is always 0
        dist[src] = 0

        # Add all vertices in queue
        queue = []
        for i in range(row):
            queue.append(i)

        # Find shortest path for all vertices
        while queue:

            # Pick the minimum dist vertex
            # from the set of vertices
            # still in queue
            u = self.minDistance(dist, queue)

            # remove min element
            queue.remove(u)

            # Update dist value and parent
            # index of the adjacent vertices of
            # the picked vertex. Consider only
            # those vertices which are still in
            # queue
            for i in range(col):
                '''Update dist[i] only if it is in queue, there is
                an edge from u to i, and total weight of path from
                src to i through u is smaller than current value of
                dist[i]'''
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u

        # print the constructed distance array
        self.printSolution(dist, parent)


def get_three_tuple(distance_json):
    places = len(distance_json.get('id').items())
    ids = distance_json.get('id')
    id_keys = list(ids.keys())
    #print(id_keys)
    three_tuple = {}
    for i in id_keys:
        place_id = distance_json.get('id')[i]
        name = distance_json.get('Name')[i]
        x = distance_json.get('X')[i]
        y = distance_json.get('Y')[i]
        three_tuple[name] = (place_id,x,y)
    return three_tuple

def manhatten(a,b):
    return (abs(a[1]-a[2]) + abs(b[1] - b[2]))

def get_graph(graph_json,distance_map):
    edges_id = list(graph_json.get('id').keys())
    #print(edges_id)
    graph = []
    n = len(distance_map)
    for i in range(n):
        graph.append([])
        for j in range(n):
            graph[i].append(0)


    for i in edges_id:
        start_loc = graph_json.get('Start')[i]
        start_cord = distance_map[start_loc]
        end_loc = graph_json.get('End')[i]
        end_cord   = distance_map[end_loc]
        graph[start_cord[0]-1][end_cord[0]-1] = manhatten(start_cord,end_cord)
        graph[end_cord[0] - 1][start_cord[0] - 1] = manhatten(start_cord, end_cord)
        #print(f'{start_loc} to {end_loc} -> {graph[start_cord[0]-1][end_cord[0]-1]} units')
    return graph
import requests


def get_short_path(remaining_dist):
    rem=remaining_dist
    graph_json=requests.request('GET','https://pastebin.com/raw/Aningtgq').json()
    distance_json = requests.request('GET', 'https://pastebin.com/raw/CjNmqD0L').json()
    '''print(x.json())
    graph_json_file = 'https://pastebin.com/raw/Aningtgq'
    distance_json_file = 'https://pastebin.com/raw/CjNmqD0L'
    with open(graph_json_file,'r') as f:
        graph_json = json.loads(f.read())
    with open(distance_json_file,'r') as f:
        distance_json = json.loads(f.read())'''
    distance_map = get_three_tuple(distance_json)
    print(distance_map)
    #print(graph_json)
    #print(distance_json)
    locations= distance_json.get('Name')

    gp=get_graph(graph_json,distance_map)
    #print(gp)
    '''for i in range(len(gp)):
        for j in range(len(gp)):
            if gp[i][j]==-1:
                gp[i][j]=0
            print(gp[i][j],end=' ')
        print("\n")'''
    g = Graph(locations)
    g.graph=gp
    g.dijkstra(g.graph,0)

get_short_path(100)
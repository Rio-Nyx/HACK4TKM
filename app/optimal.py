# Python3 implementation to find minimum
# spanning tree for adjacency representation.
from sys import maxsize

INT_MAX = maxsize
V = 20

ad = [[-1 for j in range(30)] for i in range(30)]


def isValidEdge(u, v, inMST):
    if u == v:
        return False
    if inMST[u] == False and inMST[v] == False:
        return False
    elif inMST[u] == True and inMST[v] == True:
        return False
    return True


def primMST(cost):
    inMST = [False] * V

    # Include first vertex in MST
    inMST[0] = True

    # Keep adding edges while number of included
    # edges does not become V-1.
    edge_count = 0
    mincost = 0
    while edge_count < V - 1:

        # Find minimum weight valid edge.
        minn = INT_MAX
        a = -1
        b = -1
        for i in range(V):
            for j in range(V):
                if cost[i][j] < minn:
                    if isValidEdge(i, j, inMST):
                        minn = cost[i][j]
                        a = i
                        b = j

        if a != -1 and b != -1:
            print("Edge %d: (%d, %d) cost: %d" %(edge_count, a, b, minn))
            ad[a][b]=minn
            ad[b][a]=minn
            edge_count += 1
            mincost += minn
            inMST[b] = inMST[a] = True

    print("Minimum cost = %d" % mincost)




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

def compute(graph_link,loaction_link):
    graph_json = requests.request('GET', 'https://pastebin.com/raw/Aningtgq').json()
    distance_json = requests.request('GET', 'https://pastebin.com/raw/CjNmqD0L').json()
    graph_json = requests.request('GET', graph_link).json()
    distance_json = requests.request('GET', loaction_link).json()

    distance_map = get_three_tuple(distance_json)
    print(distance_map)
    # print(graph_json)
    # print(distance_json)
    locations = distance_json.get('Name')

    gp = get_graph(graph_json, distance_map)

    for i in range(len(gp)):
        for j in range(len(gp)):
            if(gp[i][j]==0):
                gp[i][j]=INT_MAX

    """cost = [[INT_MAX, 2, INT_MAX, 6, INT_MAX],
            [2, INT_MAX, 3, 8, 5],
            [INT_MAX, 3, INT_MAX, INT_MAX, 7],
            [6, 8, INT_MAX, INT_MAX, 9],
            [INT_MAX, 5, 7, 9, INT_MAX]]"""
    cost=gp
    print(len(gp))

    # Print the solution
    primMST(gp)

    # This code is contributed by
    # sanjeev2552
    for i in range(20):
        for j in range(20):
            if(ad[i][j]!=-1):
                print(f"edge {i} -- {j}  length-{ad[i][j]}")

    print("hiiiii")

    minimum=30
    chargin_stations=[]
    visited=[0 for i in range(20)]
    def dfs(loc,sum,prev_edge):
        visited[loc]=1
        print(f"sum {sum} current loc {loc} previous edge  {prev_edge}")
        if sum >minimum:
            a=prev_edge[0]
            b=prev_edge[1]
            dist=max(ad[a][b]//minimum,1)
            chargin_stations.append([a,b,dist])
            sum=0
        for i in range(20):

            if(ad[loc][i]!=-1 and visited[i]==0):
                print((loc, i))
                dfs(i,sum+ad[loc][i],[loc,i])



    dfs(0,0,[0,0])

    charge=[]
    for i in range(len(chargin_stations)):
        start = locations[str(chargin_stations[i][0])]
        end = locations[str(chargin_stations[i][1])]
        print(f"road from {start} to {end} has {chargin_stations[i][2]} charging stations")
        charge.append(f"road from {start} to {end} has {chargin_stations[i][2]} charging stations")
    return charge

compute('https://pastebin.com/raw/Aningtgq','https://pastebin.com/raw/CjNmqD0L')
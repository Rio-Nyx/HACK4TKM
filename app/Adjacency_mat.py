#!/usr/bin/env python

import json
import sys
rem=50
l=[]

class Graph():

    def __init__(self, vertices,locations):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.locations= locations

    def printSolution(self, dist):
        print("Vertex tDistance from Source")
        for node in range(self.V):
            if dist[node]<rem:
                print(self.locations[str(node)], "t", dist[node])
                l.append([self.locations[str(node)],dist[node]])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):

        # Initialize minimum distance for next node
        min = sys.maxsize
        min_index=-1
        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and  dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)




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
            graph[i].append( -1)


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
    for i in range(len(gp)):
        for j in range(len(gp)):
            if gp[i][j]==-1:
                gp[i][j]=0
            print(gp[i][j],end=' ')
        print("\n")
    g = Graph(len(gp),locations)
    g.graph=gp
    g.dijkstra(0)

    #print(gp)

def get_shortest_palces():
    return l


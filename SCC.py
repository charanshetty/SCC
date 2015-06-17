#Author charan Shetty
# Date 15-6-2015
import sys
import time
import resource
from itertools import groupby
from collections import defaultdict

source = str(sys.argv[1])
#N = 27
# N = 9


class Track(object):

    """Keeps note of current_time,current_source and set of explored nodes and  thier
    finishing times"""

    def __init__(self):
        self.leader = {}
        self.explored = set([])
        self.current_time = 0
        self.current_source = None
        self.finish_time = {}

    def __str__(self):
        return str(self.current_time)


def dfs(graph_dict, node, track):
    """DFS algorithm on graph_dict """

    stack = [node]
    while not (len(stack) == 0):
        vertex = stack.pop()
        # print("explored" + str(track.explored))
        if vertex not in track.explored:
            track.explored.add(vertex)
            stack = stack + [vertex]
            # print(graph_dict[vertex])
            for w in graph_dict[vertex]:
                if w not in track.explored:
                    stack = stack + [w]
        else:
            if vertex not in track.finish_time:
                track.current_time += 1
                track.finish_time[vertex] = track.current_time
                track.leader[vertex] = track.current_source


def loop_DFS(graph, nodes, track):
    # print(graph)
    """Running dfs until all the nodes are explored """
    for node in nodes:
        if node not in track.explored:
            track.current_source = node
            dfs(graph, node, track)


def stronglyConnectedComponent(graph, reverse_graph, nodesrev):
    """computing stronglyConnectedComponent on both original and reversed graphs """
    out = defaultdict(list)
    track = Track()
    # dfs on reversed graph
    loop_DFS(reverse_graph, nodesrev, track)
    sorted_nodes = sorted(track.finish_time,
                          key=track.finish_time.get, reverse=True)  # get nodes sorted on finish time

    # print(track.current_time)
    track.current_time = 0
    track.current_source = None
    track.explored = set()
    track.finish_time = {}
    loop_DFS(graph, sorted_nodes, track)
    for lead, vertex in groupby(sorted(track.leader, key=track.leader.get), key=track.leader.get):
        out[lead] = list(vertex)
    return out


def getGraph():
    '''Read the graph from input file'''
    G = defaultdict(lambda: [])
    Grev = defaultdict(lambda: [])
    fin = open(source)
    for line in fin:
        v1 = int(line.split()[0])
        v2 = int(line.split()[1])
        G[v1].append(v2)
        Grev[v2].append(v1)
    fin.close()
    return G, Grev

g, grev = getGraph()
# print(len(g))
nodesrev = []
for key, value in grev.items():
    nodesrev.append((key))


out = stronglyConnectedComponent(g, grev, nodesrev)

count = 0
for key, value in out.items():
    # if len(value) > 1 :
    #    print(len(value))
    count += 1

print(count)

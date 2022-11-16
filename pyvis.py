#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rdflib.extras.external_graph_libs import *
from rdflib import Graph
from pyvis import network as pvnet

def plot(G, name='out.html', height='800px', width='1500px'):
    g = G.copy()

    net = pvnet.Network(notebook=True, directed=True, height=height, width=width)
    opts = '''
        var options = {
        "physics": {
            "forceAtlas2Based": {
            "gravitationalConstant": -100,
            "centralGravity": 0.11,
            "springLength": 100,
            "springConstant": 0.09,
            "avoidOverlap": 1
            },
            "minVelocity": 0.75,
            "solver": "forceAtlas2Based",
            "timestep": 0.22
        }
        }
    '''

    #net.set_options(opts)
    net.from_nx(g)
    return net.show(name)


g = Graph().parse("./finos.ttl", format="turtle")
G = rdflib_to_networkx_multidigraph(g)
plot(G)
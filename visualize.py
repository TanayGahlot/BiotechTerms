#oggpnosn 
#hkhr

import networkx as nx
import json

fob = open("biotechTerms.json")
terms = json.load(fob)
graph = nx.Graph()

for term in terms:
	for connectedTerm in term["linksTo"]:
		graph.add_edge(term["title"], connectedTerm)

nx.write_gexf(graph, "sampleGraph.gexf")


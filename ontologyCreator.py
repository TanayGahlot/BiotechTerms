#oggpnosn
#hkhr

#creating layers of ontology data 

import networkx as nx 
import json

fob = open("biotechTerms.json")
data = json.load(fob)
graph = nx.Graph()

for record in data:
	for term in record["linksTo"]:
		graph.add_edge(record["title"],term)

btw = nx.betweenness_centrality(graph)
btw_sorted = sorted(btw, key = lambda x:-1*btw[x])

length = len(data)
interval = length/6;

document = {}

for i in range(6):
	document["class "+str(i)] = btw_sorted[i*interval:(i+1)*interval]

fob.close()
fob = open("intermediateOntology.json", "w")
json.dump(document, fob)
fob.close()



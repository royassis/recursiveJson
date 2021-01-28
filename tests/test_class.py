from recursiveJson.classes_related_code import Graph, build_graph_from_nested_dict_base
import json

g = Graph()
with open("sample.json", "r") as fp:
    data = json.load(fp)

build_graph_from_nested_dict_base(g.root, data)

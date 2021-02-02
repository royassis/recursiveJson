from utils import get_flat_part_from_dict, get_dict_value_by_key_type

class Node:
    def __init__(self, data):
        self.data = data
        self.next_list = []

        for k, v in data.items():
            setattr(self, k, v)

    def add(self, new_node):
        self.next_list.append(new_node)

class Graph:
    def __init__(self, data = {}):
        self.root = Node(data)

def build_graph_from_nested_dict_base(prev_node, nested_dict):
    dictlist = get_dict_value_by_key_type(nested_dict)
    plain_dict = get_flat_part_from_dict(nested_dict)

    current_node = Node(plain_dict)
    prev_node.add(current_node)

    if not dictlist:
        return

    for newdict in dictlist:
        build_graph_from_nested_dict_base(current_node, newdict)
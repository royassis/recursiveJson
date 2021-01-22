import pandas as pd


def get_data_part_from_dict(d):
    return {i: j for i, j in d.items() if type(j) != list}


def get_recursive_part_from_dict(d):
    for key, val in d.items():
        if type(val) == list:
            return val


def unravel_nested_dict_base(mylist, base_dict, added_dict):
    dictlist = get_recursive_part_from_dict(base_dict)
    plain_dict = get_data_part_from_dict(base_dict)

    if not dictlist:
        mylist.append(plain_dict | added_dict)
        return

    for newdict in dictlist:
        unravel_nested_dict_base(mylist, newdict, plain_dict | added_dict)

    return mylist


def unravel_nested_dict(data):
    result = unravel_nested_dict_base(list(), data, dict())
    return pd.DataFrame(result)


def tranverse_nested_dict():
    """TODO: impliment"""


def nested_dict_to_model_base(parent_primary_key, level_idx, result_container, base_dict):
    """TODO: think of a better implementation"""

    node_children_list = get_recursive_part_from_dict(base_dict)
    node_data = get_data_part_from_dict(base_dict)

    try:
        result_container[level_idx]
    except:
        result_container.append([])

    result_container[level_idx].append(node_data)

    level_size = len(result_container[level_idx])

    node_data.update({"primary_key": level_size})
    node_data.update({"foreign_key": parent_primary_key})

    if not node_children_list:
        return

    for child in node_children_list:
            nested_dict_to_model_base(level_size, level_idx + 1, result_container, child)

    return result_container


def nested_dict_to_model(nested_dict):
        dfs=[]
        multiple_dicts = nested_dict_to_model_base(0, 0, list(), nested_dict)
        for flat_dict in multiple_dicts:
            dfs.append(pd.DataFrame(flat_dict))

        return dfs
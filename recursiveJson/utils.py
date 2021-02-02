import pandas as pd


def get_data_part_from_dict(d):
    exlueder_parts = (list,dict)
    return {key: val for key, val in d.items() if not type(val) in exlueder_parts}

def get_dict_value_by_key_type(d, object_type):
    for key, val in d.items():
        if type(val) == object_type:
            return val

def unravel_nested_dict_base(mylist, base_dict, added_dict):
    dict_list = get_dict_value_by_key_type(base_dict, list)
    nested_dict = get_dict_value_by_key_type(base_dict, dict)
    plain_dict = get_data_part_from_dict(base_dict)

    if not dict_list and not nested_dict:
        mylist.append(plain_dict | added_dict)
        return

    if nested_dict:
        unravel_nested_dict_base(mylist, nested_dict, added_dict | plain_dict)

    if dict_list :
        for newdict in dict_list:
            unravel_nested_dict_base(mylist, newdict, added_dict | plain_dict)



    return mylist


def unravel_nested_dict(data):
    result = unravel_nested_dict_base(list(), data, dict())
    return pd.DataFrame(result)


def tranverse_nested_dict():
    """TODO: impliment"""


def nested_dict_to_model_base(parent_primary_key, level_idx, result_container, base_dict):
    """TODO: think of a better implementation"""

    node_children_list = get_dict_value_by_key_type(base_dict, list)
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
    dfs = []
    multiple_dicts = nested_dict_to_model_base(0, 0, list(), nested_dict)
    for flat_dict in multiple_dicts:
        dfs.append(pd.DataFrame(flat_dict))

    return dfs

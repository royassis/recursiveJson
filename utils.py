import pandas as pd


def get_flat_part_from_dict(d):
    return {i: j for i, j in d.items() if type(j) != list}


def get_recursive_part_from_dict(d):
    for key, val in d.items():
        if type(val) == list:
            return val


def unravel_nested_dict_base(mylist, base_dict, added_dict):
    dictlist = get_recursive_part_from_dict(base_dict)
    plain_dict = get_flat_part_from_dict(base_dict)

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


def nested_dict_to_model_base(new_primary_key, parent_primary_key, level_idx, result_container, base_dict):

    children_list = get_recursive_part_from_dict(base_dict)
    this_object = get_flat_part_from_dict(base_dict)

    this_object.update({"primary_key": new_primary_key})
    this_object.update({"foreign_key": parent_primary_key})

    try:
        result_container[level_idx]
    except:
        result_container.append([])

    result_container[level_idx].append(this_object)

    if not children_list:
        return

    child_idx = 0
    for child in children_list:
            nested_dict_to_model_base(child_idx, new_primary_key, level_idx + 1, result_container, child)
            child_idx = child_idx +1

    return result_container


def nested_dict_to_model(nested_dict):
        dfs=[]
        multiple_dicts = nested_dict_to_model_base(0, 0, 0, list(), nested_dict)
        for flat_dict in multiple_dicts:
            dfs.append(pd.DataFrame(flat_dict))

        return dfs
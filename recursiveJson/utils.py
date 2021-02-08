import pandas as pd


def get_flat_part_from_dict(d):
    exlueder_parts = (list, dict)
    return {key: val for key, val in d.items() if not type(val) in exlueder_parts}


def extract_dict_items_by_val_type(base_dict, object_type):
    results = {}
    for key, val in base_dict.items():
        if type(val) == object_type:
            results[key]=val
    return results


def add_prefix_to_dict_keys(my_dict, prefix):
    new_dict = {}
    prefix = prefix.strip()
    len_prefix = len(prefix)
    prefix = f"{prefix}"
    for key, val in my_dict.items():
        keys = []
        if len_prefix:
            keys.append(prefix)
        keys.append(key)
        new_key = "__".join(keys)
        new_dict[new_key] = val
    return new_dict


def filter_list(excluded_value, *args, **kwargs):
    return [arg for arg in args if not arg == excluded_value]


def join_keys(sep="_", *args, **kwargs):
    key_list = filter_list("", *args)
    return sep.join(key_list)


def unravel_nested_dict_base(mylist, base_dict, added_dict, parent_key):
    dict_with_values_as_list_of_dicts = extract_dict_items_by_val_type(base_dict, object_type=list)
    dict_with_values_as_dict = extract_dict_items_by_val_type(base_dict, object_type=dict)
    plain_dict = get_flat_part_from_dict(base_dict)

    # plain_dict = add_prefix_to_dict_keys(plain_dict, prefix=parent_key)

    if not dict_with_values_as_list_of_dicts and not dict_with_values_as_dict:
        mylist.append(plain_dict | added_dict)
        return

    if dict_with_values_as_dict:
        for key, nested_dict in dict_with_values_as_dict.items():
            nested_dict = add_prefix_to_dict_keys(nested_dict, prefix=key)
            unravel_nested_dict_base(mylist, nested_dict, added_dict | plain_dict, key)

    if dict_with_values_as_list_of_dicts:
        for key, list_of_dicts in dict_with_values_as_list_of_dicts.items():
            for nested_dict in list_of_dicts:
                nested_dict = add_prefix_to_dict_keys(nested_dict, prefix=key)
                unravel_nested_dict_base(mylist, nested_dict, added_dict | plain_dict, key)

    return mylist


def unravel_nested_dict(data):
    result = unravel_nested_dict_base(list(), data, dict(), "")
    return pd.DataFrame(result)


def tranverse_nested_dict():
    """TODO: impliment"""


def nested_dict_to_model_base(parent_primary_key, level_idx, result_container, base_dict):
    """TODO: think of a better implementation"""

    dict_with_values_as_list_of_dicts = extract_dict_items_by_val_type(base_dict, list)
    node_data = get_flat_part_from_dict(base_dict)

    try:
        result_container[level_idx]
    except:
        result_container.append([])

    result_container[level_idx].append(node_data)

    level_size = len(result_container[level_idx])

    node_data.update({"primary_key": level_size})
    node_data.update({"foreign_key": parent_primary_key})

    if not dict_with_values_as_list_of_dicts:
        return

    for key, list_of_dicts in dict_with_values_as_list_of_dicts.items():
        for nested_dict in list_of_dicts:
            nested_dict_to_model_base(level_size, level_idx + 1, result_container, nested_dict)

    return result_container


def nested_dict_to_model(nested_dict):
    dfs = []
    multiple_dicts = nested_dict_to_model_base(0, 0, list(), nested_dict)
    for flat_dict in multiple_dicts:
        dfs.append(pd.DataFrame(flat_dict))

    return dfs

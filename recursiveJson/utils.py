import pandas as pd


def get_flat_part_from_dict(d):
    exlueder_parts = (list, dict)
    return {key: val for key, val in d.items() if not type(val) in exlueder_parts}


def extract_dict_items_by_val_type(base_dict, object_types):
    results = {}
    for key, val in base_dict.items():
        if any([isinstance(val, i) for i in object_types]):
            results[key] = val
    return results


def filter_out_dict_items_by_key_name(my_dict, excluded_values):
    new_dict = {}
    for key, val in my_dict.items():
        if not any(key in excluded_value for excluded_value in excluded_values):
            new_dict[key] = val

    return new_dict


def add_prefix_to_dict_keys(my_dict, prefix, sep="__"):
    new_dict = {}
    len_prefix = len(prefix)
    for key, val in my_dict.items():
        items = []
        if len_prefix:
            items.append(prefix)
        items.append(key)
        key_with_prefix = sep.join(items)
        new_dict[key_with_prefix] = val
    return new_dict


def filter_list(excluded_value, *args, **kwargs):
    return [arg for arg in args if not arg == excluded_value]


def join_keys(sep="_", *args, **kwargs):
    key_list = filter_list("", *args)
    return sep.join(key_list)


def get_parts(base_dict):
    dict_with_values_as_dicts = extract_dict_items_by_val_type(base_dict, object_types=(dict,))
    dict_with_values_as_list_of_dicts = extract_dict_items_by_val_type(base_dict, object_types=(list,))
    dict_not_data = filter_out_dict_items_by_key_name(dict_with_values_as_list_of_dicts, ["data"])
    dict_data = base_dict.get("data")
    plain_dict = get_flat_part_from_dict(base_dict)

    return plain_dict, dict_not_data, dict_data, dict_with_values_as_dicts


def unravel_nested_dict_base(mylist, base_dict, added_dict):
    plain_dict, dict_not_data, dict_data, dict_with_values_as_dicts = get_parts(base_dict)

    if not dict_not_data and not dict_data:
        mylist.append(plain_dict | added_dict)
        return

    if dict_not_data:
        for key, nested_dict in dict_not_data.items():
            # nested_dict = add_prefix_to_dict_keys(nested_dict, prefix=key)
            unravel_nested_dict_base(mylist, nested_dict, added_dict | plain_dict)

    if dict_data:
        for another_dict in dict_data:
            # nested_dict = add_prefix_to_dict_keys(nested_dict, prefix=key)
            unravel_nested_dict_base(mylist, another_dict, added_dict | plain_dict)

    return mylist


def unravel_nested_dict(data):
    result = unravel_nested_dict_base(list(), data, dict())
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


def get_leaves(item, key=None):
    if isinstance(item, dict):
        leaves = []
        for i in item.keys():
            leaves.extend(get_leaves(item[i], i))
        return leaves
    elif isinstance(item, list):
        leaves = []
        for i in item:
            leaves.extend(get_leaves(i, key))
        return leaves
    else:
        return [(key, item)]


def my_get_leaves(key=None, item=None):
    if not isinstance(item, (dict, list)):
        return [(key, item)]

    leaves = []
    for i in item:
        tupe = (i, item[i]) if isinstance(item, dict) else (key, i)
        leaves.extend(my_get_leaves(*tupe))

    return leaves

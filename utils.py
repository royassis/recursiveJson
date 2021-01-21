import pandas as pd


def get_flat_dict(d):
    return {i: j for i, j in d.items() if type(j) != list}


def get_dict_list(d):
    for key, val in d.items():
        if type(val) == list:
            return val


def unravel_nested_dict_base(mylist, base_dict, added_dict):
    dictlist = get_dict_list(base_dict)
    plain_dict = get_flat_dict(base_dict)

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


def nested_dict_to_model_base(level_indc, dict_list_all_frames, base_dict):
    """TODO: Add foreign and primary keys to parents and children"""
    dictlist = get_dict_list(base_dict)
    plain_dict = get_flat_dict(base_dict)

    try:
        dict_list_all_frames[level_indc]
    except:
        dict_list_all_frames.append([])

    dict_list_all_frames[level_indc].append(plain_dict)

    if not dictlist:
        return

    for newdict in dictlist:
            nested_dict_to_model_base(level_indc+1,dict_list_all_frames, newdict)

    return dict_list_all_frames


def nested_dict_to_model(nested_dict):
        dfs=[]
        multile_dicts = nested_dict_to_model_base(0, list(), nested_dict)
        for flat_dict in multile_dicts:
            dfs.append(pd.DataFrame(flat_dict))

        return dfs
from copy import deepcopy


def recursive_dict_merge(dict1, dict2):
    """
    Recursively merges two dicts:
    If a field in both dicts is a dict itself, then it's not replaced,
    but updated recursively.

    Does not update dicts in place. Returns result as new dict.
    """
    res = deepcopy(dict1)
    for k, v in dict2.items():
        cv = dict1.get(k)
        if isinstance(cv, dict) and isinstance(v, dict):
            nv = recursive_dict_merge(cv, v)
        else:
            nv = v
        res[k] = nv
    return res

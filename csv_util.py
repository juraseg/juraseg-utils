"""
CSV utils
"""

import csv
from operator import itemgetter


def is_iterable(obj):
    """
    Predicate to check if `obj` is an iterable
    """
    try:
        an_iter = iter(obj)
        return True
    except TypeError:
        return False


def lens(*objs):
    """
    Return lengths of arguments
    """
    return tuple([len(obj) for obj in objs])


def load_csv_data(filename):
    """
    Generator returning rows of CSV filen given by `filename`
    """
    with open(filename) as f:
        for row in csv.DictReader(f):
            yield row


def get_fields(data, key):
    """
    Get field or fields given by `key`, which can be a string or list of strings
    """
    if is_iterable(key) and not isinstance(key, basestring):
        getter = itemgetter(*key)
    else:
        getter = itemgetter(key)
    return [getter(row) for row in data]


def decode_row(row, encoding='utf-8'):
    """
    Decode row values from string to unicode
    """
    new_row = {}
    for k in row:
        new_row[k] = row[k]
        if isinstance(new_row[k], str):
            new_row[k] = new_row[k].decode(encoding)
    return new_row


def encode_row(row, encoding='utf-8'):
    """
    Encode row values from unicode to string
    """
    new_row = {}
    for k in row:
        new_row[k] = row[k]
        if isinstance(new_row[k], unicode):
            new_row[k] = new_row[k].decode(encoding)
    return new_row


def diff_csv_files(filename1, filename2, id_field='identifier'):
    """
    Compare data in `filename1` and `filename2` using `id_field`.
    Return 3 lists:
    1) rows found in both files
    2) rows found in `filename1` and not found in `filename2`
    3) rows found in `filename2` and not found in `filename1`
    """
    data1 = list(load_csv_data(filename1))
    ids1 = set(get_fields(data1, id_field))
    data2 = list(load_csv_data(filename2))
    ids2 = set(get_fields(data2, id_field))
    diff1to2 = ids1 - ids2
    diff2to1 = ids2 - ids1
    simil = ids1.intersection(ids2)
    diff1to2 = [row for row in data1 if row[id_field] in diff1to2]
    diff2to1 = [row for row in data2 if row[id_field] in diff2to1]
    simil = [row for row in data2 if row[id_field] in simil]
    return simil, diff1to2, diff2to1

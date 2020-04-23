def list_or_tuple_tojson(obj):
    ret = '['
    for i in obj[:-1]:
        ret += indict_to_json(i) + ', '
    ret += indict_to_json(obj[-1])
    ret += ']'
    return ret


def indict_to_json(obj: dict):
    ret = ""

    if isinstance(obj, dict):
        ret = into_json(obj)

    elif isinstance(obj, list) or isinstance(obj, tuple):
        ret = list_or_tuple_tojson(obj)

    elif isinstance(obj, bool):
        if obj:
            ret = "true"
        else:
            ret = "false"

    elif isinstance(obj, int) or isinstance(obj, float) or isinstance(obj, complex):
        ret = str(obj)

    elif isinstance(obj, str):
        ret = '"{}"'.format(str(obj))

    elif obj is None:
        ret = 'null'

    return ret


def into_json(obj: object):
    json = "{"
    if isinstance(obj, dict):
        dict1 = obj
    for key, value in list(dict1.items()):
        if key != list(dict1.keys())[-1]:
            json += '"{}": {}'.format(str(key), indict_to_json(value)) + ', '
        else:
            json += '"{}": {}'.format(str(key), indict_to_json(value))

    json += "}"
    return json


def to_json(obj: object):
    return into_json(obj)

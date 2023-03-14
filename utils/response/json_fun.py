from utils.response.res_code import Code


def to_json_data(code=Code.OK, errmsg='', data=None, **kwargs):
    json_dict = {'code': code, 'errmsg': errmsg, 'data': data}

    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        json_dict.update(kwargs)

    return json_dict

def filter_by_state(list_of_dict: list[dict], state: str ='EXECUTED') -> list[dict]:
    """Фильтрация списка по ключу 'state'"""
    new_list_of_dict = []
    for dict_ in list_of_dict:
        if dict_.get('state') == state:
            new_list_of_dict.append(dict_)

    return new_list_of_dict
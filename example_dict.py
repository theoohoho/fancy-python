# verify dict key
def validate_dict_key(incoming_obj: dict):
    """
    validate obj key at least match both key1 and key2
    """
    incoming_obj.keys() >= {"key1", "key2"}


def sort_dict_by_value(input: dict) -> None:
    """
    sorted can sort iterable data, that include list, dict, tuple, set...
    """

    sorted(input, key=input["attr1"])

    ls = [123, 12, 45678, 1234567]
    # list itme 長度排序
    sorted(ls, key=len)
    # list item 數值排序
    sorted(ls.items(), key=lambda item: item[1])
    lsd = [{"a": 123, "b": 456}, {"a": 456, "b": 789}]
    sorted(lsd.items(), key=lambda item: item[1])

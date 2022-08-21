import re
from typing import Iterator, Union, List, Any
from werkzeug.exceptions import BadRequest
from os import PathLike, path


def check_count_args(
    *args: tuple,
    **kwargs: Union[Union[str, bytes, PathLike[str], PathLike[bytes]], int]
) -> None:
    """Проверяет заполнены ли важные поля"""
    if kwargs["cmd1"] and kwargs["val1"] is None:
        raise BadRequest("Введите значения")
    if kwargs["file_name"] is None:
        raise BadRequest("Обязательно нужно ввести название файла")
    if path.exists(kwargs["file_path"]) is False:
        raise BadRequest("Нет такого файла")


def foo(f: Iterator, cmd: str, val: str) -> List[Any]:
    """Функция работы с командами и значениями"""
    if cmd == "filter":
        res = list(filter(lambda x: val in x, f))
        return res
    if cmd == "map":
        res = list([x.split()[int(val)] for x in f])
        return res
    if cmd == "unique":
        res = list(set(f))
        return res
    if cmd == "sort":
        reverse = val == "desc"
        res = list(sorted(f, reverse=reverse))
        return res
    if cmd == "limit":
        res = list(f)[: int(val)]
        return res
    if cmd == "regex":
        regex = re.compile(val)
        res = list(filter(lambda x: regex.search(x), f))
        return res
    return []

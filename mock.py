from collections import namedtuple
from itertools import groupby


Mock = namedtuple('MockerData', ['method', 'url', 'status', 'headers', 'body'])


def get_mock_from_file(mock_file_name):
    """
    Read mock receipt from file and return Mock instance
    :param mock_file_name: file with mocker receipt
    :return: iterator with mocker data
    """
    with open(mock_file_name, 'r') as fp:
        raw = fp.readlines()

    return Mock(
        *(''.join(v) for k, v in groupby(raw, lambda key: False if key == '\n' else True) if k)
    )


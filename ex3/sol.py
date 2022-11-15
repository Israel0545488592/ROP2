from typing import Iterable

''' custom list as child of python's list'''

class MyList(list):

    def __init__(self, iterable: Iterable):
        super().__init__(item for item in iterable)

    def __getitem__(self, indecies):

        if isinstance(indecies, slice):
            return super().__getitem__(indecies)
        if isinstance(indecies, int):
            indecies = [indecies]

        item = super().__getitem__(indecies[0])

        for i in indecies[1:]:  item = item[i]

        return item

    def __setitem__(self, indecies, item):

        if isinstance(indecies, int):
            super().__setitem__(indecies, item)
            return

        cont = super().__getitem__(indecies[0])

        for i in indecies[1: -1]:  cont = cont[i]

        cont[indecies[-1]] = item

    def __repr__(self) -> str:
        return super().__repr__()
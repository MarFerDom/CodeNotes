from typing import Protocol

class farmAnimal(Protocol):
    '''A farm animal'''

    def do(self) -> None:
        '''A farm animal does ???'''
import importlib
import factory
from typing import Protocol


class moduleInterface(Protocol):
    def register() -> None:
        '''Register classes in module'''

def load(name: str) -> moduleInterface:
    '''loads the plugins'''

    return importlib.import_module(name)

def load_register(plugin_names: 'list[str]') -> None:
    '''for each plug-in name, load and register in factory'''

    for name in plugin_names:
        plugin = load(name)
        plugin.register()